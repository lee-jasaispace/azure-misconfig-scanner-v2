# PowerShell script for Day 1 setup

# Create resource group
az group create --name RG-SecureAccess --location eastus

# Create virtual network and subnet
az network vnet create --resource-group RG-SecureAccess --name MyVnet --subnet-name MySubnet
