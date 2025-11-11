# Script to configure Azure Web App settings using values from .env file

# Variables
$RESOURCE_GROUP="rg-rag-projects"
$APP_SERVICE_PLAN="basic-rag-appservice"
$WEB_APP_NAME="basic-rag-ui"
$LOCATION="eastus"
$ENV_FILE_PATH=".env"

# Function to read .env file and convert to hashtable
function Get-EnvVariables {
    param (
        [string]$envPath
    )
    $envVars = @{}
    if (Test-Path $envPath) {
        Get-Content $envPath | ForEach-Object {
            if ($_ -match '^([^=]+)=(.*)$') {
                $envVars[$matches[1]] = $matches[2]
            }
        }
    }
    else {
        Write-Error "Environment file not found at: $envPath"
        exit 1
    }
    return $envVars
}

# Read environment variables
Write-Host "Reading environment variables from $ENV_FILE_PATH..."
$envVars = Get-EnvVariables $ENV_FILE_PATH

# Validate required environment variables
$requiredVars = @(
    "AZURE_SEARCH_ENDPOINT",
    "AZURE_SEARCH_KEY",
    "AZURE_SEARCH_INDEX",
    "AOAI_DEPLOYMENT",
    "AOAI_KEY",
    "AOAI_ENDPOINT",
    "AOAI_API_VERSION",
    "AOAI_EMBEDDING_MODEL"
)

foreach ($var in $requiredVars) {
    if (-not $envVars.ContainsKey($var)) {
        Write-Error "Missing required environment variable: $var"
        exit 1
    }
}

# Create Resource Group if it doesn't exist
Write-Host "Creating/Verifying Resource Group..."
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create App Service Plan if it doesn't exist
Write-Host "Creating/Verifying App Service Plan..."
az appservice plan create `
    --name $APP_SERVICE_PLAN `
    --resource-group $RESOURCE_GROUP `
    --sku B1 `
    --is-linux

# Create Web App if it doesn't exist
Write-Host "Creating/Verifying Web App..."
az webapp create `
    --name $WEB_APP_NAME `
    --resource-group $RESOURCE_GROUP `
    --plan $APP_SERVICE_PLAN `
    --runtime "PYTHON:3.11"

# Prepare app settings command with values from .env
$settings = @(
    "AZURE_SEARCH_ENDPOINT=""$($envVars['AZURE_SEARCH_ENDPOINT'])""",
    "AZURE_SEARCH_KEY=""$($envVars['AZURE_SEARCH_KEY'])""",
    "AZURE_SEARCH_INDEX=""$($envVars['AZURE_SEARCH_INDEX'])""",
    "AOAI_DEPLOYMENT=""$($envVars['AOAI_DEPLOYMENT'])""",
    "AOAI_KEY=""$($envVars['AOAI_KEY'])""",
    "AOAI_ENDPOINT=""$($envVars['AOAI_ENDPOINT'])""",
    "AOAI_API_VERSION=""$($envVars['AOAI_API_VERSION'])""",
    "AOAI_EMBEDDING_MODEL=""$($envVars['AOAI_EMBEDDING_MODEL'])""",
    "SCM_DO_BUILD_DURING_DEPLOYMENT=""true""",
    "PYTHON_ENV=""production"""
)

# Configure Web App Settings
Write-Host "Configuring Web App Settings..."
$settingsString = $settings -join " "
$command = "az webapp config appsettings set --resource-group $RESOURCE_GROUP --name $WEB_APP_NAME --settings $settingsString"
Invoke-Expression $command

Write-Host "Web App configuration completed successfully!"
Write-Host "Web App URL: https://$WEB_APP_NAME.azurewebsites.net"

# Additional helpful information
Write-Host "`nUseful commands:"
Write-Host "View app settings: az webapp config appsettings list --resource-group $RESOURCE_GROUP --name $WEB_APP_NAME"
Write-Host "View logs: az webapp log tail --resource-group $RESOURCE_GROUP --name $WEB_APP_NAME"
Write-Host "Restart app: az webapp restart --resource-group $RESOURCE_GROUP --name $WEB_APP_NAME"
