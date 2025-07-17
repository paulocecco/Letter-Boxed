from collections import defaultdict
import nltk
from nltk.corpus import words

# Ensure NLTK dictionary is downloaded
nltk.download('words', quiet=True)

def find_word_chains(steps, boxes, print_results=True):
    """
    Find valid English word chains of given step length using custom letter boxes.

    Rules:
    - Each word must use only letters from the given boxes.
    - No two consecutive letters may come from the same box.
    - Words must form a chain (last letter of one is first of the next).
    - All box letters must be used at least once in the full chain.

    Parameters:
        steps (int): Number of words in the chain (e.g. 3).
        boxes (dict[int, set[str]]): A mapping of box numbers to sets of uppercase letters.
        print_results (bool): Whether to print results to console.

    Returns:
        list[list[str]]: A list of valid word chains, each as a list of words.
    """

    # Map letters to their box
    letter_to_box = {letter: box for box, letters in boxes.items() for letter in letters}
    all_letters = set(letter_to_box.keys())

    # Load and pre-filter valid words
    ENGLISH_WORDS = set(w.lower() for w in words.words() if len(w) >= 2)

    def is_valid_word(word):
        word = word.upper()
        if any(c not in letter_to_box for c in word):
            return False
        for i in range(1, len(word)):
            if letter_to_box[word[i]] == letter_to_box[word[i - 1]]:
                return False
        return True

    valid_words = [w.lower() for w in ENGLISH_WORDS if is_valid_word(w)]

    # Group words by starting letter
    start_letter_dict = defaultdict(list)
    for w in valid_words:
        start_letter_dict[w[0]].append(w)

    # Recursive DFS to find chains
    solutions = []

    def search_chain(current_chain, used_letters):
        if len(current_chain) == steps:
            if all_letters.issubset(used_letters):
                solutions.append(list(current_chain))
            return

        last_word = current_chain[-1]
        next_start = last_word[-1]

        for next_word in start_letter_dict.get(next_start, []):
            updated_used = used_letters.union(set(next_word.upper()))
            current_chain.append(next_word)
            search_chain(current_chain, updated_used)
            current_chain.pop()

    # Start search
    for word in valid_words:
        search_chain([word], set(word.upper()))

    if print_results:
        print(f"\n🔍 Found {len(solutions)} valid {steps}-word chains:\n")
        for chain in solutions:
            print(" → ".join(w.upper() for w in chain))

    return solutions
