from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
)
from constructs import Construct


class SQS(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        sqs.Queue(
            self,
            id="SQSQueue",
            queue_name="sahils_sqs_queue",
            visibility_timeout=Duration.seconds(300),
        )
