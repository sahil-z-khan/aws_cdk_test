import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_infra.cloudfront import CloudFront


def test_cloudfront_distribution_created():
    app = core.App()
    stack = CloudFront(app, "CloudFrontStackTest")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::CloudFront::Function", 1)
    template.resource_count_is("AWS::CloudFront::Distribution", 1)
    template.has_resource_properties(
        "AWS::CloudFront::Distribution",
        {
            "DistributionConfig": assertions.Match.object_like(
                {
                    "DefaultCacheBehavior": assertions.Match.object_like(
                        {
                            "ViewerProtocolPolicy": "redirect-to-https",
                            "FunctionAssociations": assertions.Match.array_with(
                                [
                                    assertions.Match.object_like(
                                        {"EventType": "viewer-request"}
                                    )
                                ]
                            ),
                        }
                    ),
                    "Origins": assertions.Match.array_with(
                        [
                            assertions.Match.object_like(
                                {"DomainName": "example.com"}
                            )
                        ]
                    ),
                }
            )
        },
    )
