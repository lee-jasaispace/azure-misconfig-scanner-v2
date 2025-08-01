# Assign policy to audit NICs with public IPs

az policy assignment create `
  --name "AuditNICsWithPublicIPs" `
  --display-name "Network interfaces should not have public IPs" `
  --policy "/providers/Microsoft.Authorization/policyDefinitions/83a86a26-fd1f-447c-b59d-e51f44264114" `
  --scope "/subscriptions/5d4b8df0-f30a-4bc3-b350-1ace90d201b8/resourceGroups/RG-SecureAccess"
