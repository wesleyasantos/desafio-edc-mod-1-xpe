resource "aws_s3_bucket" "datalake" {
  bucket = "dl-desafio-mod1-tf"

  tags = {
    MOD1   = "DESAFIO"
    CURSO = "EDC"
  }
}