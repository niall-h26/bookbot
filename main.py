from stats import count_words, count_characters

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    num_characters = count_characters(text)
    print(f"{num_words} words found in the document")
    print(num_characters)

main()