# Created a Log Analytics workspace and set up diagnostic settings for Activity Log

az monitor log-analytics workspace create `
    --resource-group RG-SecureAccess `
    --workspace-name LA-SecureAccess `
    --location eastus

# Verified the diagnostic settings
az monitor diagnostic-settings list --resource "/subscriptions/5d4b8df0-f30a-4bc3-b350-1ace90d201b8" -o table

# Triggered a loggable action
az storage account update `
  --name publicstoragedemo9139 `
  --resource-group RG-SecureAccess `
  --tags test=trigger

# Ran a query in the Log Analytics Workspace
AzureActivity
| where TimeGenerated > ago(6hr)
| limit 10
