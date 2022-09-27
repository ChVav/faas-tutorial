terraform {
  required_providers {
    aws = ">= 4.10"
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.2.0"
    }
  }

}
provider "aws" {
	# WRITE YOUR REGION
}

data "archive_file" "lambda_terraform_test" {

	# SPECIFY DEPLOYMENT PACKAGE
}

# Test Function "plus"
resource "aws_lambda_function" "aws_function" {

	# SPECIFY DEPLOYMENT PARAMETERS - Recap what was needed for TASK 1

}

resource "aws_iam_role" "lambda_exec" {

	# CREATE A ROLE IF NEEDED
}

resource "aws_iam_role_policy_attachment" "lambda_policy" {

	# SPECIFY A ROLE

}
