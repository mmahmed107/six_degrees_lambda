terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

locals {

  lambda_name         = format("%s_%s", var.lambda_name, var.cloud_id)
  trust_policy_file   = "trust-policy.json"
  logging_policy_file = "logging-policy.json"
  iam_for_lambda      = format("iam_%s", local.lambda_name)
  logging_policy_name = format("lambda-log-writer-%s", local.lambda_name)
}

# Configuration of required role and policy as defined in JSON files

data "local_file" "trust_policy" {
  filename = local.trust_policy_file
}

data "local_file" "logging_policy" {
  filename = local.logging_policy_file
}


resource "aws_iam_role" "iam_for_lambda" {

  name               = local.iam_for_lambda
  assume_role_policy = data.local_file.trust_policy.content
}

resource "aws_iam_policy" "lambda_logging" {
  name   = local.logging_policy_name
  path   = "/"
  policy = data.local_file.logging_policy.content
}

# Creation of the AWS Lambda function and deploying the Python src files

module "mod_lambda" {
  source        = "./module"
  lambda_source = abspath("../src")
  lambda_name   = local.lambda_name
  aws_region    = var.aws_region
  iam_role_name = aws_iam_role.iam_for_lambda.name
  policy_arn    = [aws_iam_policy.lambda_logging.arn]

  depends_on = [
    aws_iam_role.iam_for_lambda,
    aws_iam_policy.lambda_logging
  ]
}
