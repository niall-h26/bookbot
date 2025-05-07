def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(text):
    char_totals = {}
    text = text.lower()
    for char in text:
        if char in char_totals:
            char_totals[char] += 1
        else:
            char_totals[char] = 1
    return char_totals

def sort_chars(char_totals):
    sorted_chars = []
    for char in char_totals:
        if char.isalpha():
            sorted_chars.append({"char": char, "num": char_totals[char]})
    sorted_chars.sort(key=lambda x: x["num"], reverse=True)
    return sorted_chars