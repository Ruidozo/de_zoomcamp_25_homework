Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.demo_dataset will be created
  + resource "google_bigquery_dataset" "demo_dataset" {
      + creation_time               = (known after apply)
      + dataset_id                  = "de_zoomcamp25_dataset"
      + default_collation           = (known after apply)
      + default_table_expiration_ms = 3600000
      + delete_contents_on_destroy  = false
      + effective_labels            = {
          + "env"                        = "dev"
          + "goog-terraform-provisioned" = "true"
        }
      + etag                        = (known after apply)
      + id                          = (known after apply)
      + is_case_insensitive         = (known after apply)
      + labels                      = {
          + "env" = "dev"
        }
      + last_modified_time          = (known after apply)
      + location                    = "US"
      + max_time_travel_hours       = (known after apply)
      + project                     = "de-zoomcamp-25"
      + self_link                   = (known after apply)
      + storage_billing_model       = (known after apply)
      + terraform_labels            = {
          + "env"                        = "dev"
          + "goog-terraform-provisioned" = "true"
        }

      + access {
          + domain         = (known after apply)
          + group_by_email = (known after apply)
          + iam_member     = (known after apply)
          + role           = (known after apply)
          + special_group  = (known after apply)
          + user_by_email  = (known after apply)

          + dataset {
              + target_types = (known after apply)

              + dataset {
                  + dataset_id = (known after apply)
                  + project_id = (known after apply)
                }
            }

          + routine {
              + dataset_id = (known after apply)
              + project_id = (known after apply)
              + routine_id = (known after apply)
            }

          + view {
              + dataset_id = (known after apply)
              + project_id = (known after apply)
              + table_id   = (known after apply)
            }
        }
    }

  # google_storage_bucket.bucket will be created
  + resource "google_storage_bucket" "bucket" {
      + effective_labels            = {
          + "goog-terraform-provisioned" = "true"
        }
      + force_destroy               = false
      + id                          = (known after apply)
      + location                    = "US"
      + name                        = "de-zoomcamp-25-bucket"
      + project                     = (known after apply)
      + project_number              = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = {
          + "goog-terraform-provisioned" = "true"
        }
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }

          + condition {
              + age                   = 365
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }

      + soft_delete_policy {
          + effective_time             = (known after apply)
          + retention_duration_seconds = (known after apply)
        }

      + versioning {
          + enabled = (known after apply)
        }

      + website {
          + main_page_suffix = (known after apply)
          + not_found_page   = (known after apply)
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.demo_dataset: Creating...
google_storage_bucket.bucket: Creating...
google_bigquery_dataset.demo_dataset: Creation complete after 1s [id=projects/de-zoomcamp-25/datasets/de_zoomcamp25_dataset]
google_storage_bucket.bucket: Creation complete after 2s [id=de-zoomcamp-25-bucket]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.