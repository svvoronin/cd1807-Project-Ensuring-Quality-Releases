variable "application_type" {}
variable "resource_type" {}
variable "location" {}
variable "resource_group" {}
variable "subnet_id" {}
variable "public_ip_address_id" {}

variable "admin_username" {
  description = "User name for the admin account on the VMs"
  default     = "adminuser"
}

variable "admin_password" {
  description = "Default password for admin account"
  default     = "@adminPassword@"
}
