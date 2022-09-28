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


# Test Function "plus"
resource "aws_lambda_function" "aws_function" {
  function_name    = "plus3"
  filename         = "function.zip"
  runtime          = "python3.9"
  handler          = "function.lambda_handler"
  source_code_hash = filebase64sha256("function.zip")
  role             = aws_iam_role.lambda_exec3.arn
}

resource "aws_iam_role" "lambda_exec3" {
  name = "github_actions_deploy3"
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
  role       = aws_iam_role.lambda_exec3.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
