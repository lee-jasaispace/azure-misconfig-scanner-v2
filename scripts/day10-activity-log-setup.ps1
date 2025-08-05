# Created a Log Analytics workspace 

az monitor log-analytics workspace create `
    --resource-group RG-SecureAccess `
    --workspace-name LA-SecureAccess `
    --location eastus
