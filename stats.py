def get_word_count(book_text):
    word_count = book_text.split()
    
    return len(word_count)


def get_letter_dict(book_text):
    letter_count = {}
        
    file_contents = book_text.lower()
    for letter in file_contents:
        if letter == " ":
            pass           
        elif letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    return letter_count

def sort_on(dct):
    return dct["num"]

def get_sorted_chars (num_dict):
    sorted_list = []
    
    for char in num_dict:
        sorted_list.append({"char": char, "num": num_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)    
    
    return sorted_list

def get_report(book_path, word_count, letter_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in letter_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")