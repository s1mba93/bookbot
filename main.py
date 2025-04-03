from stats import get_word_count

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents


def main():
    #print(get_book_text("books/frankenstein.txt"))
    
    print(get_word_count("books/frankenstein.txt"))


main()