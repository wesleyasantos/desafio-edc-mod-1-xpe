resource "aws_s3_bucket" "datalake" {
  bucket = "dados-rais-2020-edc"

  tags = {
    MOD1   = "DESAFIO"
    CURSO = "EDC"
  }
}