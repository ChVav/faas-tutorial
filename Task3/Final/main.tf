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
  region = "us-east-1"
}

data "archive_file" "lambda_terraform_test" {
  type = "zip"

  source_file = "${path.module}/function.py"
  output_path = "${path.module}/function.zip"
}

# Test Function "plus"
resource "aws_lambda_function" "aws_function" {
  function_name    = "plus"
  filename         = lambda_terraform_test.output_path
  runtime          = "python3.9"
  handler          = "function.lambda_handler"
  source_code_hash = filebase64sha256(lambda_terraform_test.output_path)
  role             = aws_iam_role.lambda_exec.arn
  #layers = ["arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p39-pillow:1"] #for face recognition
}

resource "aws_iam_role" "lambda_exec" {
  name = "github_actions_deploy"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Sid    = ""
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
