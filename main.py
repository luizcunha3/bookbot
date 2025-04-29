from stats import get_number_of_words, get_letter_count, pretty_print
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    arguments = sys.argv
    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
        words = get_book_text(path_to_book)
        num_words = get_number_of_words(words)
        chars_dict = get_letter_count(words)
        pretty_print(path_to_book, num_words, chars_dict)
main()