variable "project" {
  description = "Project"
  default     = "adroit-medium-379911"
}

variable "region" {
  description = "Region for Project"
  default     = "europe-west3"

}

variable "credentials" {
  description = "My Credentials"
  default     = "./keys/creds.json"

}

variable "gcp_location" {
  description = "My geographic Location"
  default     = "EU"
}

variable "gcp_bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "mage_demo"
}

variable "gcp_bucket_name" {
  description = "My Storage Bucket  Name"
  default     = "adroit-medium-379911-terraform-demo-bucket"
}

variable "gcp_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}