import sys
from stats import count_words, count_characters, sort_chars

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    try:
        text = get_book_text(sys.argv[1])
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = count_words(text)
    num_characters = count_characters(text)
    sorted_chars = sort_chars(num_characters)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
    

main()