"""Capture the javac errors of the deliberately broken Calculator from the sheet.

The file demo-errors/CalculatorAmbiguity.java does not compile, which is the
point of Part 2 of the workshop. javac is run with an English locale so the
messages match the explanation in the document.
"""
import subprocess

JAVAC = r"C:\ComPackageSet\openjdk-21.0.2_windows-x64_bin\jdk-21.0.2\bin\javac.exe"

result = subprocess.run(
    [JAVAC, "-J-Duser.language=en", "-J-Duser.country=US", "-Xlint:-options",
     "--release", "8", r"demo-errors\CalculatorAmbiguity.java"],
    capture_output=True, text=True, encoding="utf-8", errors="replace")

text = (result.stdout or "") + (result.stderr or "")
with open(r"output\CalculatorAmbiguity_compile_errors.txt", "w", encoding="utf-8") as f:
    f.write(text)

print(text)
