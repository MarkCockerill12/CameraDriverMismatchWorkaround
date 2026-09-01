#Requires -RunAsAdministrator
$ErrorActionPreference = "SilentlyContinue"

Write-Host "=== Setting up Virtual Camera Anchor ===" -ForegroundColor Cyan

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$dll64 = Join-Path $scriptDir "UnityCapture\UnityCapture-master\Install\UnityCaptureFilter64.dll"
$dll32 = Join-Path $scriptDir "UnityCapture\UnityCapture-master\Install\UnityCaptureFilter32.dll"

Write-Host "Unregistering any old/broken camera links..." -ForegroundColor Yellow
# Try to unregister from the old path if it exists
$oldDll64 = "C:\Users\Mark\coding\Laptop\scripts\UnityCapture\UnityCapture-master\Install\UnityCaptureFilter64.dll"
$oldDll32 = "C:\Users\Mark\coding\Laptop\scripts\UnityCapture\UnityCapture-master\Install\UnityCaptureFilter32.dll"
if (Test-Path $oldDll64) { & "$env:SystemRoot\System32\regsvr32.exe" /u /s $oldDll64 }
if (Test-Path $oldDll32) { & "$env:SystemRoot\System32\regsvr32.exe" /u /s $oldDll32 }

# Unregister new path just in case
if (Test-Path $dll64) { & "$env:SystemRoot\System32\regsvr32.exe" /u /s $dll64 }
if (Test-Path $dll32) { & "$env:SystemRoot\System32\regsvr32.exe" /u /s $dll32 }

Write-Host "Anchoring virtual camera to new folder..." -ForegroundColor Yellow
if (Test-Path $dll64) { 
    & "$env:SystemRoot\System32\regsvr32.exe" /s $dll64 
    Write-Host "64-bit anchor registered." -ForegroundColor Green
} else {
    Write-Host "Error: Could not find $dll64" -ForegroundColor Red
}

if (Test-Path $dll32) { 
    & "$env:SystemRoot\System32\regsvr32.exe" /s $dll32 
    Write-Host "32-bit anchor registered." -ForegroundColor Green
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Camera successfully linked to this folder!" -ForegroundColor Green
Read-Host "Press Enter to close"
