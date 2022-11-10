resource "aws_redshift_cluster" "example" {
  cluster_identifier = "tf-daniel-tika-cluster"
  database_name      = "daniedatabase"
  master_username    = var.redshift-admin-user
  master_password    = var.redshift-admin-master_password
  node_type          = "dc2.large"
  cluster_type       = "single-node"
}