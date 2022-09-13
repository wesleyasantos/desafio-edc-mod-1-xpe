resource "aws_s3_bucket" "datalake" {
  # Parâmetros de config do recurso escolhido
  bucket = "datalake-tf-test"

  tags = {
    IES   = "TESTE"
    CURSO = "IAC"
  }
}