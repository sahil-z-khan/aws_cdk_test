import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_infra.sqs import SQSQueue


def test_sqs_queue_created():
    app = core.App()
    stack = SQSQueue(app, "aws-cdk-test")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {"VisibilityTimeout": 300})
