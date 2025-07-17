# Letter-Boxed
Have you ever played (Letter Boxed) [https://www.nytimes.com/puzzles/letter-boxed] at New York Times games and struggle? Then, this script is just for you.

## This game has the following rules
* **Letter Arrangement:** The letters are presented in a square, with four sets of three letters on each side. 
* **Word Formation:** Players create words by connecting letters sequentially. 
* **Side Restriction:** A crucial rule is that you cannot use letters from the same side of the square consecutively. 
* **Word Length:** Each word must have a minimum of three letters. 
* **Chain Connection:** The last letter of one word becomes the first letter of the next word. 
* **Goal:** The objective is to use all the letters provided in the fewest possible words. 
* **No Proper Nouns or Abbreviations:** Only standard dictionary words are allowed; acronyms and proper nouns are no

## Features

- Customizable number of steps (e.g. 3-word or 5-word chains)
- Fully recursive search with full dictionary validation
- Uses [NLTK's English word list](https://www.nltk.org/)
- Clean, modular function interface

## Example

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
