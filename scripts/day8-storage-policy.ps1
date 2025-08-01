# Assign policy to audit public network access on storage accounts

az policy assignment create `
  --name "AuditStoragePublicAccess" `
  --display-name "Audit public network access on storage accounts" `
  --policy "/providers/Microsoft.Authorization/policyDefinitions/e56962a6-4747-49cd-b67b-bf8b01975c4c" `
  --params "{ \"listOfAllowedLocations\": { \"value\": [\"eastus\"] } }" `
  --scope "/subscriptions/5d4b8df0-f30a-4bc3-b350-1ace90d201b8/resourceGroups/RG-SecureAccess"
