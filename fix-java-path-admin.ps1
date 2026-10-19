# 修复 `java -version` 显示 1.8 的问题（需要管理员权限运行）
# 原因：系统 PATH 中 Oracle 的 java8path / javapath 排在 JDK 21 的 bin 之前。
# 做法：把 JDK 21 的 bin 移到系统 PATH 最前面（保留 Java 8，可随时改回），备份后写入。

$ErrorActionPreference = 'Stop'
$jdkBin = 'C:\ComPackageSet\openjdk-21.0.2_windows-x64_bin\jdk-21.0.2\bin'
$stamp  = Get-Date -Format 'yyyyMMdd-HHmmss'
$backup = "$env:USERPROFILE\Desktop\machine-PATH-backup-$stamp.txt"

if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()
        ).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host '❌ 请右键“以管理员身份运行 PowerShell”，再执行本脚本。' -ForegroundColor Red
    exit 1
}

$old = [Environment]::GetEnvironmentVariable('Path', 'Machine')
$old -split ';' | Set-Content -Path $backup -Encoding UTF8
Write-Host "原系统 PATH 已备份到: $backup"

$entries = ($old -split ';') | Where-Object { $_ -and $_.Trim() -ne '' }
$entries = $entries | Where-Object { $_.TrimEnd('\') -ne $jdkBin.TrimEnd('\') }
$new = (@($jdkBin) + $entries) -join ';'

[Environment]::SetEnvironmentVariable('Path', $new, 'Machine')
Write-Host '✅ 已把 JDK 21 的 bin 移到系统 PATH 最前面。' -ForegroundColor Green

Write-Host ''
Write-Host '生效验证：请【新开】一个 cmd / PowerShell 窗口，运行：'
Write-Host '    java  -version     # 应显示 21.0.2'
Write-Host '    javac -version     # 应显示 21.0.2'
Write-Host ''
Write-Host '如需还原：Set-Content 前备份文件里的内容写回 Machine 级 Path 即可（或再跑一次本目录下的还原提示）。'
