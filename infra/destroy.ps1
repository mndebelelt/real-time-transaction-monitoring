param(
    [string]$ResourceGroupName = "rttm-rg"
)

Write-Host "Deleting resource group $ResourceGroupName ..."
az group delete `
  --name $ResourceGroupName `
  --yes `
  --no-wait