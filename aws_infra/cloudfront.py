from aws_cdk import (
    Stack,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
)
from constructs import Construct


class CloudFront(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        cf_function = self._create_function()
        origin = self._create_origin()
        self._create_distribution(origin, cf_function)

    def _create_function(self) -> cloudfront.Function:
        # Base template CloudFront Function that adds a header
        return cloudfront.Function(
            self,
            "BaseCfFunction",
            function_name="BaseCfFunction",
            code=cloudfront.FunctionCode.from_inline(
                """
                    function handler(event) {
                        var request = event.request;
                        request.headers['x-powered-by'] = { value: 'cdk-cloudfront' };
                        return request;
                    }
                """.strip()
            ),
        )

    def _create_origin(self) -> origins.HttpOrigin:
        # Simple HTTP origin; replace example.com with your backend or S3 website endpoint
        return origins.HttpOrigin("example.com")

    def _create_distribution(
        self, origin: origins.IOrigin, cf_function: cloudfront.Function
    ) -> None:
        cloudfront.Distribution(
            self,
            "CloudFrontDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origin,
                compress=True,
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                function_associations=[
                    cloudfront.FunctionAssociation(
                        event_type=cloudfront.FunctionEventType.VIEWER_REQUEST,
                        function=cf_function,
                    )
                ],
            ),
        )
