variable "resource_group_name" {
  type        = string
  description = "Назва ресурсної групи в Azure"
  default     = "hr-analytics-rg"
}

variable "location" {
  type        = string
  description = "Фізичний регіон датацентру"
  default     = "West Europe"
}

variable "admin_username" {
  type        = string
  description = "Ім'я адміністратора для сервера"
  default     = "azureuser"
}
