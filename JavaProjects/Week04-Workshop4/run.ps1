# BIT235 Week 4 - compile and run every program, saving the real output.
$ErrorActionPreference = "Stop"
$javac = "C:\ComPackageSet\openjdk-21.0.2_windows-x64_bin\jdk-21.0.2\bin\javac.exe"
Set-Location $PSScriptRoot

& $javac -Xlint:-options --release 8 *.java
if ($LASTEXITCODE -ne 0) { throw "compile failed" }
Write-Host "compile ok"

function Run-One([string]$class, [string]$outFile, [string]$stdinText) {
    if ($stdinText) {
        $stdinText | & java $class | Out-File -FilePath (Join-Path "output" $outFile) -Encoding utf8
    } else {
        & java $class | Out-File -FilePath (Join-Path "output" $outFile) -Encoding utf8
    }
}

Run-One "DisplayWelcome"          "Q1_DisplayWelcome.txt"
Run-One "DisplayNumber"           "Q2_DisplayNumber.txt"
Run-One "DiceRoll"                "Q3_DiceRoll.txt"
Run-One "RandomNumber"            "Q4_RandomNumber.txt"
Run-One "ShorthandArray"          "A1_ShorthandArray.txt"
Run-One "StandardArray"           "A2_StandardArray.txt"
Run-One "ForLoopTraversal"        "A3_ForLoopTraversal.txt"
Run-One "ForEachTraversal"        "A4_ForEachTraversal.txt"
Run-One "SearchValue"             "A5_SearchValue.txt"
Run-One "ReverseTraversal"        "A6_ReverseTraversal.txt"
Run-One "FillArrayAtRuntime"      "A7_FillArrayAtRuntime.txt"  "Wilma`nFred`nBarney`nBetty`nPebbles"
Run-One "IndexAccessCommaList"    "A8_IndexAccessCommaList.txt"
Run-One "CalculateTotal"          "E1_CalculateTotal.txt"
Run-One "BubbleSort"              "E2_BubbleSort.txt"
Run-One "BinaryVsLinearSearch"    "E3_BinaryVsLinearSearch.txt"
Run-One "MainApp"                 "O1_MainApp.txt"
Run-One "StudentsApp"             "O2_StudentsApp.txt"

Get-ChildItem output\*.txt | ForEach-Object {
    Write-Host ("--- {0} ---" -f $_.Name)
    Get-Content $_.FullName -Encoding utf8 | Out-String | Write-Host
}
