# BIT235 Workshop 3 - Programming Structures in Java

Week 3 workshop for BIT235 Object Oriented Programming (Melbourne Polytechnic).

Student: Chen Zhihan (S1580887)

## Contents

Part 1 - StringBuffer

| File | Task |
| --- | --- |
| `WelcomeMessage.java` | Builds a personalised welcome message with StringBuffer |
| `PalindromeCheck.java` | Reads a word with Scanner and checks it with StringBuffer.reverse() |

Part 2 - Casting

| File | Task |
| --- | --- |
| `NationalDebt.java` | USA national debt as a long, narrowed to an int and to a byte |
| `CastingPrecision.java` | PI (10 dp) double -> float, and 23.99 / 23.00 stored as doubles |
| `AgeStringToInt.java` | String "21" converted with Integer.parseInt() |
| `BooleanToString.java` | boolean status converted with String.valueOf() |

Part 3 - Conditional logic and loops

| File | Task |
| --- | --- |
| `GreetingByTime.java` | Exercise 1(a): "Good day" / "Good evening" from an hour 1-24 |
| `MultiplesOfFive.java` | Exercise 1(b): multiples of 5 between 10 and 95 |
| `SumOneToTen.java` | Exercise 1(c): sum of 1..10 with a while loop |
| `SmallestOfThree.java` | Exercise 2: smallest of three numbers |
| `NumberToLetter.java` | Exercise 3: 0-35 mapped to 0-9 and A-Z |
| `SumOfSquares.java` | Exercise 4A: sum of the squares of the first 100 integers |
| `PerfectSquares.java` | Exercise 4B: perfect squares between 1 and 100 |
| `FramingCost.java` | Exercise 6: picture framing cost calculator |

## How to run

```
javac --release 8 *.java
java WelcomeMessage
powershell -NoProfile -ExecutionPolicy Bypass -File .\run.ps1
```

`run.ps1` compiles every program and stores each run in `output/`.
The filled-in workshop document is `doc/BIT235_Workshop3_S1580887.docx`.
