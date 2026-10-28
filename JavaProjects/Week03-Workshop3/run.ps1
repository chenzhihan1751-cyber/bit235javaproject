# Compile and run every Workshop 3 program, saving each run to output\<Class>.txt
$ErrorActionPreference = "Stop"
$javac = "C:\ComPackageSet\openjdk-21.0.2_windows-x64_bin\jdk-21.0.2\bin\javac.exe"
$java  = "C:\ComPackageSet\openjdk-21.0.2_windows-x64_bin\jdk-21.0.2\bin\java.exe"
$here  = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

Get-ChildItem *.class -ErrorAction SilentlyContinue | Remove-Item -Force
& $javac --release 8 *.java
if ($LASTEXITCODE -ne 0) { throw "javac failed" }
Write-Host "compile OK"

function Run-One {
    param([string]$Class, [string]$Out, [string[]]$InputLines = @())
    $text = ($InputLines -join "`r`n")
    if ($InputLines.Count -gt 0) { $text += "`r`n" }
    $text | & $java $Class | Out-File -FilePath (Join-Path $here "output\$Out.txt") -Encoding utf8
    Write-Host ("ran " + $Class)
}

# Part 1
Run-One "WelcomeMessage" "WelcomeMessage"
Run-One "PalindromeCheck"  "PalindromeCheck_racecar" @("Racecar")
Run-One "PalindromeCheck"  "PalindromeCheck_hello"   @("hello")
# Part 2
Run-One "NationalDebt"    "NationalDebt"
Run-One "CastingPrecision" "CastingPrecision"
Run-One "AgeStringToInt"  "AgeStringToInt"
Run-One "BooleanToString" "BooleanToString"
# Part 3
Run-One "GreetingByTime"  "GreetingByTime_day"     @("9")
Run-One "GreetingByTime"  "GreetingByTime_evening" @("20")
Run-One "MultiplesOfFive" "MultiplesOfFive"
Run-One "SumOneToTen"     "SumOneToTen"
Run-One "SmallestOfThree" "SmallestOfThree"        @("12", "5", "8")
Run-One "NumberToLetter"  "NumberToLetter_A"       @("10")
Run-One "NumberToLetter"  "NumberToLetter_digit"   @("7")
Run-One "SumOfSquares"    "SumOfSquares"
Run-One "PerfectSquares"  "PerfectSquares"
Run-One "FramingCost"     "FramingCost"            @("20", "15", "regular", "white", "yes", "4")

Write-Host "all done"
Get-ChildItem output\*.txt | Select-Object Name, Length | Format-Table -AutoSize
