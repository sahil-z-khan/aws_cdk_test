import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_infra.route53 import Route53


def test_route53_record_created():
    app = core.App()
    stack = Route53(app, "Route53StackTest")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Route53::RecordSet", 1)
    template.has_resource_properties(
        "AWS::Route53::RecordSet",
        {
            "Name": "app.example.com.",
            "Type": "A",
            "HostedZoneId": "Z1234567890ABCDEF",
            "ResourceRecords": ["203.0.113.10"],
        },
    )
