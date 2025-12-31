# Create an IAM user for CLI access

How to create and configure a dedicated IAM user for AWS CLI usage.

## Create the user
1. Sign in to the AWS console with an admin account and open IAM: https://console.aws.amazon.com/iam/
2. Go to **Users** → **Create user**.
3. Enter a username (e.g., `cli-deployer`).
4. Under **Access type**, enable **Access key - Programmatic access**.

## Set permissions
Choose the least privilege policy your workflow needs:
- For CDK experimentation, use **AdministratorAccess** (broad; tighten later).
- For narrower access, create/attach a custom policy with only required services/actions.

## Finish and capture credentials
1. Complete the wizard and **download the `.csv`** with the Access key ID and Secret access key.
2. Store the secret securely (password manager). You cannot view the secret again.

## Configure AWS CLI
Set the credentials and default region for a named profile:
```bash
aws configure --profile cli-deployer
# enter Access key ID
# enter Secret access key
# enter default region (e.g., us-east-1)
# default output format (json is fine)
```
Use the profile when running CLI/CDK:
```bash
export AWS_PROFILE=cli-deployer
```

## Security hygiene
- Do not use the root account for CLI/API access.
- Enable MFA on the admin account that manages this user.
- Rotate or delete unused access keys; keep only one active key when possible.
- Consider short-lived credentials (SSO or IAM Identity Center) for production use.
