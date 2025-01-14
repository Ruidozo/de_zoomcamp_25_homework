# Configure the Google Cloud provider
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.14.1"
    }
  }
}

provider "google" {
  project     = var.project
  region      = var.location
  credentials = var.google_credentials
}

# Create a Google Cloud Storage bucket
resource "google_storage_bucket" "bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  storage_class = "STANDARD"
  lifecycle_rule {
    condition {
      age = 365
    }
    action {
      type = "Delete"
    }
  }
}

# Create a Google BigQuery dataset
resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id                  = "de_zoomcamp25_dataset"
  location                    = var.location
  default_table_expiration_ms = 3600000
  labels = {
    env = "dev"
  }
}