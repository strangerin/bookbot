import sys
from stats import count_words, count_letters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #book_path = input("Enter the path to the book: ")
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print_text_report(letter_count, word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_text_report(letter_count, word_count):
    sorted_letters = sorted(letter_count.items())
    print(f"--- Begin report of {sys.argv[1]} ---")
    total_words = word_count
    #print(f"{total_words} words found in the document\n")
    print(f"Found {total_words} total words")
    for char, count in sorted_letters:
        print(f"{char}: {count}")
        #print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


main()
