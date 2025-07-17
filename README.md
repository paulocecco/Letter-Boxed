# Letter-Boxed Solver

Have you ever played [Letter Boxed](https://www.nytimes.com/puzzles/letter-boxed) from the New York Times and struggled to solve it? This script helps you find valid word chains based on a custom version of the game with programmable letter boxes.

---

## 🧩 Game Rules (Modeled After Letter Boxed)

- **Letter Arrangement:** Letters are divided into four sides (boxes), each containing **three letters**.
- **Word Formation:** Words are formed by connecting letters **sequentially**, one letter at a time.
- **Side Restriction:** You **cannot use two consecutive letters from the same box**.
- **Word Length:** Each word must be **at least 3 letters long**.
- **Word Chaining:** The **last letter of one word** must be the **first letter of the next**.
- **Goal:** Use **all 12 letters** from the boxes in the fewest number of words.
- **Dictionary Check:** Only **real English words** are allowed—no proper nouns, abbreviations, or made-up words.

---

## Features

- Fully recursive and exhaustive word chain solver
- Set a **custom number of steps** (e.g. 3-word or 5-word chains)
- All words are validated using the [NLTK English word list](https://www.nltk.org/)
- Clean, reusable function interface

---

## Example Usage

```python
from word_chain_solver import find_word_chains

boxes = {
    1: set("SHO"),
    2: set("NMA"),
    3: set("LYF"),
    4: set("PID")
}

# Find all valid 3-word chains
find_word_chains(steps=3, boxes=boxes)
```

# Requirements
Install `nltk` dependencies via:

```python
pip install nltk
```

Also, be sure to run this once in your script to download the word list:
```python
import nltk
nltk.download('words')
```

---

## Key Fixes & Improvements

Feel free to fork, star, or submit a pull request if you want to improve performance, integrate a GUI, or extend support for alternative word lists.
