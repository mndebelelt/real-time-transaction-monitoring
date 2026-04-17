param(
    [Parameter(Mandatory = $true)]
    [string]$PublicIp,

    [string]$SshKeyPath = "$HOME\.ssh\rttm_vm_key",

    [string]$SshUser = 'azureuser'
)

if (-not (Test-Path $SshKeyPath)) {
    Write-Error "SSH key not found at $SshKeyPath"
    exit 1
}

$remoteCommands = @(
    'sudo apt update',
    'sudo apt install -y docker.io docker-compose-plugin',
    'sudo systemctl enable --now docker',
    'cd ~/real-time-transaction-monitoring/docker',
    'docker compose up -d',
    'cd ~/real-time-transaction-monitoring',
    'pip3 install -r requirements.txt'
)

$remoteCommand = $remoteCommands -join ' ; '
$sshKeyPathEscaped = $SshKeyPath -replace '\\', '/'

Write-Host "Bootstrapping remote VM at $PublicIp using SSH key $SshKeyPath"

$sshArgs = @('-i', $sshKeyPathEscaped, "$SshUser@$PublicIp", $remoteCommand)

$process = Start-Process -FilePath ssh -ArgumentList $sshArgs -NoNewWindow -Wait -PassThru

if ($process.ExitCode -ne 0) {
    Write-Error "Remote bootstrap failed with exit code $($process.ExitCode)"
    exit $process.ExitCode
}

Write-Host 'Remote VM bootstrap complete.'
Write-Host "Next steps: open one SSH session and run 'python3 -m app.producer.run_producer'"
Write-Host "and in another session run 'python3 -m app.consumer.run_consumer'"
