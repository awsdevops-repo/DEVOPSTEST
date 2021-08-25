terraform {
  backend "s3" {
    # Create bucket and provide the bucketname below
    bucket = "mybucket"
    key    = "path/to/my/key"
    region = "us-east-1"
  }
}
