# Week05 workshop - compile everything and save the real console output.
# Run from the project folder:  powershell -ExecutionPolicy Bypass -File run.ps1

$ErrorActionPreference = "Stop"
$javac = "C:\ComPackageSet\openjdk-21.0.2_windows-x64_bin\jdk-21.0.2\bin\javac.exe"

New-Item -ItemType Directory -Force output | Out-Null

# 1) compile the project (JDK 21 compiler, Java 8 bytecode)
& $javac -Xlint:-options --release 8 *.java

# 2) run each program and capture its real output
& java OverloadDemo            | Out-File output\OverloadDemo.txt -Encoding utf8
& java Calculator              | Out-File output\Calculator.txt -Encoding utf8
& java PrinterDemo             | Out-File output\PrinterDemo.txt -Encoding utf8
& java CalculatorAmbiguityFixed | Out-File output\CalculatorAmbiguityFixed.txt -Encoding utf8
& java MainDriver              | Out-File output\MainDriver.txt -Encoding utf8
& java ExtensionDriver         | Out-File output\ExtensionDriver.txt -Encoding utf8

# 3) the sheet version of the ambiguous Calculator does not compile on purpose:
#    capture the javac errors (python keeps the file clean UTF-8, English locale)
$oldEap = $ErrorActionPreference
$ErrorActionPreference = "Continue"
python capture_errors.py | Out-Null
$ErrorActionPreference = $oldEap

Write-Host "done"
