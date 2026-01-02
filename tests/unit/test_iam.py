import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_infra.iam import IAM


def test_iam_role_and_policies_created():
    app = core.App()
    stack = IAM(app, "IamStackTest")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::IAM::Role",
        {"RoleName": "lambda-role"},
    )
    template.has_resource_properties(
        "AWS::IAM::Policy",
        {"PolicyName": "lambda-policy"},
    )
    template.has_resource_properties(
        "AWS::IAM::ManagedPolicy",
        {"ManagedPolicyName": "existing-role-extra-permissions"},
    )
