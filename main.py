from stats import (
    get_num_words,
    get_chars_dict,
    get_sorted_list
)

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(book_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict_ in sorted_list:
        if dict_['character'].isalpha():
            print(f"{dict_['character']}: {dict_['count']}")
    print("============= END ===============")
    

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = get_sorted_list(chars_dict)
    print_report(book_path, num_words, sorted_list)


main()