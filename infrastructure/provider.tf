provider "aws" {
  region = var.aws_region
}

# Centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {
    bucket = "state-terraform-test-ws"
    key    = "state/edc-xpe/mod1/terraform.tfstate"
    region = "us-east-2"
  }
}