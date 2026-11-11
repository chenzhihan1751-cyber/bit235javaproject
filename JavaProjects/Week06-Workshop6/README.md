# BIT235 Workshop 6 - Java Collections & OOP Concepts

Melbourne Polytechnic BIT235 Object Oriented Programming (FMP), 2026 Oct.
Student: Chen Zhihan, S1580887.

Repository: https://github.com/chenzhihan1751-cyber/bit235javaproject

## Exercises

| # | File | Difficulty | What it does |
|---|------|-----------|--------------|
| 1 | `SongList.java` | Easy | 10 songs in one array, artists in a second array, printed together |
| 2 | `SongListSorted.java` | Hard | Exercise 1 plus a bubble sort, so the songs print in alphabetical order |
| 3 | `ReverseWordSentence.java` | Medium | Reverses the letters inside every word, keeping spaces and punctuation |
| 4 | `DecodeMessage.java` | Easy | Decodes "G tgsl Qefe." with the substitution key from the question |
| 5 | `ParagraphSearch.java` | Medium | Searches 10 paragraphs for a phrase, reports index and paragraph |
| 6 | `IdentifyMyParts.java`, `IdentifyPartsDemo.java` | Easy | Class vs instance variables and the real output of the question's code |
| 7 | `Boxes.java`, `BoxesDriver.java` | Medium | Draws a square box (max 10 x 10) with `-` top/bottom and `|` sides |

## Build and run

```powershell
powershell -ExecutionPolicy Bypass -File run.ps1
```

Compiles everything with `javac --release 8` and writes one text file per
exercise into `output/`.

Individual runs:

```
java SongList
java SongListSorted
java ReverseWordSentence
java DecodeMessage
java DecodeMessage "Qefe s kfvb."
java ParagraphSearch "keyword search" "needle" "banana"
java IdentifyPartsDemo
java BoxesDriver
```

## Notes

- Exercise 2 sorts two parallel arrays, so the artist is swapped together with
  its song; otherwise the pairs break.
- Exercise 3 uses only a `char[]` and two indexes - no `split()`, no
  `StringBuilder` - because the question asks for loops and arrays.
- Exercise 4 stores the substitution key as two 26 character strings, so a
  different coded message only needs a different String, not new code.
- Exercise 6: `x` is `static` (one copy per class, shared), `y` is an instance
  variable (one copy per object). `a.x = 1; b.x = 2;` both write the same field,
  so every `x` prints 2.
- Exercise 7: `Boxes` refuses sizes outside 1..10 and keeps the previous size.
