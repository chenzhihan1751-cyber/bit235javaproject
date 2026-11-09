# BIT235 Week 5 - OOP Concepts and Method Overloading

Workshop work for BIT235 Object Oriented Programming (Melbourne Polytechnic).
Student: Chen Zhihan, S1580887.

## What is here

Method overloading sheet (Workshop - Method Overloading in Java.docx):

| File | Purpose |
| --- | --- |
| `OverloadDemo.java` | Part 1, the code from the sheet, run to show which overload is picked |
| `CalculatorAmbiguityFixed.java` | Part 2, the calls that compile (the other two are explained) |
| `demo-errors/CalculatorAmbiguity.java` | Part 2, the sheet version that does **not** compile |
| `Calculator.java` | Part 3, three overloaded `multiply` methods |
| `PrinterDemo.java` | Part 4, `Printer` with the extra `print(double)` overload |
| `capture_errors.py` | runs javac on the broken file and saves the compiler output |

OOP Concepts sheet (Workshop - OOP Concepts.pdf / Extension):

| File | Purpose |
| --- | --- |
| `ZooKeeper.java` | steps 1-3 and 17-20 (one keeper, many enclosures) |
| `Enclosure.java` | steps 4-5 (keeper field, assignKeeper, displayDetails) |
| `Cage.java`, `Aquarium.java`, `Aviary.java` | step 9, subclasses with their own fields |
| `MainDriver.java` | steps 3-20, printed in order |
| `EnclosureManager.java` | extension, central controller from the sheet |
| `ExtensionDriver.java` | extension, the driver from page 3 of the sheet |

## How to run

```
javac -Xlint:-options --release 8 *.java
java OverloadDemo
java Calculator
java PrinterDemo
java CalculatorAmbiguityFixed
java MainDriver
java ExtensionDriver
```

or `powershell -ExecutionPolicy Bypass -File run.ps1`, which also writes every
console output into `output/` and captures the javac errors of
`demo-errors/CalculatorAmbiguity.java`.

## Documents

`doc/BIT235_Week5_MethodOverloading_S1580887.docx`,
`doc/BIT235_Week5_OOPConcepts_S1580887.docx` and
`doc/BIT235_Week5_OOPConceptsExtension_S1580887.docx` contain the answers, the
source and the VS Code screenshots of the real runs (`doc/screenshots/`).
