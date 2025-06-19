terraform {
  backend "remote" {
    organization = "example-organization"  # Replace with your Terraform Cloud organization
    workspaces {
      name = "example-workspace"  # Replace with your workspace name in Terraform Cloud
    }
  }
}

# Example resource
resource "null_resource" "example" {
  triggers = {
    value = "This resource does nothing!"
  }
}
