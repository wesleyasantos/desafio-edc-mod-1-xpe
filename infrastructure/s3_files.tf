resource "aws_s3_bucket_object" "lambda_function" {
  bucket = aws_s3_bucket.datalake.id
  key    = "pyspark/lambda_function.py"
  acl    = "private"
  source = "../etl/lambda_function.py"
  etag   = filemd5("../etl/lambda_function.py")
}

resource "aws_s3_bucket_object" "spark_processing" {
  bucket = aws_s3_bucket.datalake.id
  key    = "pyspark/spark_processing.py"
  acl    = "private"
  source = "../etl/spark_processing.py"
  etag   = filemd5("../etl/spark_processing.py")
}