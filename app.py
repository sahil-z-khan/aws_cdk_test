#!/usr/bin/env python3
import os
import aws_cdk as cdk
from aws_infra.sqs import SQS

app = cdk.App()
env_default = cdk.Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
)

SQS(app, "SQSQueue", env=env_default, stack_name="sqs-queue-stack")

app.synth()
