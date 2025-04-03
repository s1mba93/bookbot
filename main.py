def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents


def get_word_count(filepath):
    file_contents = None
    word_count = 0
    with open(filepath) as f:
        file_contents = f.read()
    
    file_contents = file_contents.split()
    for word in file_contents:
        word_count += 1
        
    return f"{word_count} words found in the document" 


def main():
    #print(get_book_text("books/frankenstein.txt"))
    
    print(get_word_count("books/frankenstein.txt"))


main()