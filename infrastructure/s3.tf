resource "aws_s3_bucket" "datalake" {
  bucket ="etl-rais-desafio-mod1"

  tags = {
    MOD1  = "DESAFIO"
    CURSO = "EDC"
  }
}