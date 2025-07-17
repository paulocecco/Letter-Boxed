if __name__ == "__main__":
    boxes = {
        1: set("SHO"),
        2: set("NMA"),
        3: set("LYF"),
        4: set("PID")
    }

    # Find all valid 3-word chains
    find_word_chains(steps=3, boxes=boxes)
