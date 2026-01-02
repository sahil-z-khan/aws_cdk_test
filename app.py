#!/usr/bin/env python3
import aws_cdk as cdk
from aws_infra.sqs import SQS
from aws_infra.iam import IAM
from aws_infra.cloudfront import CloudFront
from models.enum.aws import AWS


app = cdk.App()

env_default = cdk.Environment(
    account=AWS.ACCOUNT_ID.value,
    region=AWS.US_EAST_1.value,
)
us_east_1 = cdk.Environment(
    account=AWS.ACCOUNT_ID.value,
    region=AWS.US_EAST_1.value,
)
us_west_2 = cdk.Environment(
    account=AWS.ACCOUNT_ID.value,
    region=AWS.US_WEST_2.value,
)


SQS(app, "SQSQueue", env=us_east_1, stack_name="sqs-queue-stack")
IAM(app, "IamStack", env=us_east_1, stack_name="iam-stack")
CloudFront(app, "CloudFrontStack", env=us_east_1, stack_name="cloudfront-stack")

app.synth()
