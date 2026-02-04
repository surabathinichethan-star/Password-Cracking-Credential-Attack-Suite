# Password Cracking & Credential Attack Suite
# Module: Dictionary Generator
# Author: Your Name

import itertools

def generate_wordlist(name, year):
    mutations = []

    base_words = [
        name,
        name.lower(),
        name.upper(),
        name.capitalize()
    ]

    symbols = ["", "@", "!", "#"]
    numbers = ["", year, "123", "2024"]

    leet_map = {
        "a": "@",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "$"
    }

    # Basic combinations
    for word in base_words:
        for sym in symbols:
            for num in numbers:
                mutations.append(f"{word}{sym}{num}")

    # Leet speak variations
    for word in base_words:
        leet_word = word
        for char in leet_map:
            leet_word = leet_word.replace(char, leet_map[char])
        mutations.append(leet_word)

    return set(mutations)


def save_wordlist(wordlist, filename):
    with open(filename, "w") as file:
        for word in wordlist:
            file.write(word + "\n")


if __name__ == "__main__":
    print("=== Dictionary Generator ===")

    name = input("Enter name: ").strip()
    year = input("Enter birth year: ").strip()

    wordlist = generate_wordlist(name, year)

    output_file = "../data/wordlist.txt"
    save_wordlist(wordlist, output_file)

    print(f"[+] Wordlist generated successfully!")
    print(f"[+] Total passwords created: {len(wordlist)}")
    print(f"[+] Saved to {output_file}")
