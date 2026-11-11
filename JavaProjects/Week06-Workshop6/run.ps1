# BIT235 Workshop 6 - build and run every exercise
# Usage: powershell -ExecutionPolicy Bypass -File run.ps1
$ErrorActionPreference = "Stop"
$javac = "C:\ComPackageSet\openjdk-21.0.2_windows-x64_bin\jdk-21.0.2\bin\javac.exe"
$proj  = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $proj
New-Item -ItemType Directory -Force -Path output | Out-Null

& $javac -Xlint:-options --release 8 *.java

& java SongList             | Out-File output\SongList.txt             -Encoding utf8
& java SongListSorted       | Out-File output\SongListSorted.txt       -Encoding utf8
& java ReverseWordSentence  | Out-File output\ReverseWordSentence.txt  -Encoding utf8
& java DecodeMessage        | Out-File output\DecodeMessage.txt        -Encoding utf8
& java ParagraphSearch "keyword search" "needle" "banana" |
    Out-File output\ParagraphSearch.txt -Encoding utf8
& java IdentifyPartsDemo    | Out-File output\IdentifyPartsDemo.txt    -Encoding utf8
& java BoxesDriver          | Out-File output\BoxesDriver.txt          -Encoding utf8

Get-ChildItem output\*.txt | ForEach-Object {
    Write-Host "===== $($_.Name) ====="
    Get-Content $_.FullName -Encoding UTF8
}
