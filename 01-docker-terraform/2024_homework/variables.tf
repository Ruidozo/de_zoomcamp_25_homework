variable "location" {
  description = "The location/region for the resources"
  default     = "US"
}

variable "project" {
  description = "The project ID"
  default     = "de-zoomcamp-25"
}

variable "google_bigquery_dataset" {
  description = "My Big Query Dataset name"
  default     = "de_zoomcamp25_dataset"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "gcs_bucket_name" {
  description = "Bucket Name"
  type = string
  default     = "de-zoomcamp-25-bucket"
}

variable "google_credentials" {
    description = "Google Cloud credentials file"
    default     = "keys/my-creds.json"
}