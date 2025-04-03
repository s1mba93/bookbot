from stats import get_word_count, get_letter_dict, get_sorted_chars, get_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
        
    


def main():
    
    try:
        sys.argv[1]
    except IndexError as i:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    letter_count = get_letter_dict(book_text)
    order_dict = get_sorted_chars(letter_count)
    
    get_report(book_path, word_count, letter_dict=order_dict)
    
    
main()