param(
    [string]$ResourceGroupName = "rttm-rg",
    [string]$Location = "southafricanorth"
)

Write-Host "Creating resource group..."
az group create `
  --name $ResourceGroupName `
  --location $Location

Write-Host "Deploying Bicep template..."
az deployment group create `
  --resource-group $ResourceGroupName `
  --template-file ./main.bicep `
  --parameters ./parameters.dev.json