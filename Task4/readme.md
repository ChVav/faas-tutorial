# Task 4: Automatize the deployment of a Lambda function with GitHub Actions and Terraform

After developing an Infrastructure-as-Code (IaC) script to describe your infrastructure and deploy the function with Terraform, in this task you will automatize even further the deployment process. 

You need to create a workflow with GitHub Actions on your GitHub repository in order to automatize the deployment of the function on each commit of your code. Instead of running IaC scripts manually, you will configure GitHub Actions to run the Terraform script that you developed in Task 3.

## Prerequisites

- GitHub account and some repository (you can clone this repository)
- function code or deployment package (zip)


## Steps

- create the GitHub Actions workflow in YAML (main.yaml)
- push it into .github/workflows
- push the new version of the function

