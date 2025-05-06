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