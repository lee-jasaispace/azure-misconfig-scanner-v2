# Policy definition for AuditKeyVaultPublicAccess
az policy assignment create `
	--name "AuditKeyVaultPublicAccess" `
	--display-name "Audit public network access on Key Vaults" `
	--policy "405c5871-3e91-4644-8a63-58e19d68ff5b" `
	--scope "/subscriptions/5d4b8df0-f30a-4bc3-b350-1ace90d201b8 /resourceGroups/RG-SecureAccess"

# To test the policy definition, created a misconfigured key vault
az keyvault create `
  --name $vaultName `
  --resource-group RG-SecureAccess `
  --location eastus `
  --public-network-access Enabled

# Confirmed the compliance state and "fixed" the misconfig
