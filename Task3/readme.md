# Task 3: Deploy a Lambda function with Terraform.

Infrastructure as a Code is a technique to code your infrastructure and use a tool that deploys that infrastructure, instead of manual deployment.

Before doing this task, go back to Task 1 and recap which information was needed while creating a function:

- Provider (Terraform supports multiple providers, you need to select it)
- region
- function parameters, such as
    - name 
    - memory
    - handler
    - runtime
    - role

You need to run terraform init and then terraform deploy.