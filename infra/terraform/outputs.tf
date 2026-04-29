output "public_ip_address" {
  value       = azurerm_linux_virtual_machine.vm.public_ip_address
  description = "Ваша публічна IP-адреса. Скопіюйте її та вставте в браузер разом з портом: http://<ця_адреса>:5000"
}
