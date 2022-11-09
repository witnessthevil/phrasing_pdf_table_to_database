resource "aws_s3_bucket" "danie-bucket" {
  bucket_prefix = var.bucket_prefix
  force_destroy = true
}

resource "aws_s3_bucket_versioning" "my_project_versioning" {
  bucket = aws_s3_bucket.danie-bucket.id 
  versioning_configuration {
    status = "Enabled"
  }
}