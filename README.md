
# AWS CDK Python project

End-to-end flow for getting this project deployed to your AWS account.

## Prerequisites
- AWS account with permissions to bootstrap and deploy CloudFormation stacks.
- AWS CLI installed and configured with credentials: `aws configure` or environment variables such as `AWS_PROFILE`.
- AWS CDK CLI installed: `npm install -g aws-cdk` (requires Node.js).
- Python 3.x available (recommended 3.11+).

## Install and configure AWS CLI
1) Install AWS CLI (v2 recommended) using the OS-specific steps from the AWS docs: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
2) Verify install: `aws --version`
3) Configure credentials and default region: `aws configure` (docs: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
4) If you use profiles, set `AWS_PROFILE=<your-profile>` before running CDK commands.
5) Need a dedicated CLI user? See [IAM_CLI_USER.md](/misc/IAM_CLI_USER.md).

## Initialize a new CDK Python app
If you are starting fresh, create a directory and initialize the project:
```bash
mkdir my-cdk-app && cd my-cdk-app
cdk init app --language python
```
Then follow the setup steps below from within that directory.

## Project setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Bootstrap the account (run once per account/region)
The CDK toolkit needs bootstrap resources in your target account/region.
```bash
cdk bootstrap aws://<ACCOUNT_ID>/<REGION>
```

## Provision the resources
```bash
cdk synth   # inspect the generated CloudFormation
cdk diff    # optional: see changes vs deployed stack
cdk deploy  # create/update the stack in the configured account/region
```
After deployment you can tear everything down with:
```bash
cdk destroy
```

## Useful commands
- `cdk ls`    list all stacks in the app
- `cdk docs`  open CDK documentation
