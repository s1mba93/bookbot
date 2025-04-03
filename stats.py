def get_word_count(filepath):
    file_contents = None
    word_count = 0
    with open(filepath) as f:
        file_contents = f.read()
    
    file_contents = file_contents.split()
    for word in file_contents:
        word_count += 1
        
    return f"{word_count} words found in the document" 


def get_letter_count(filepath):
    file_contents = None
    letter_count = {}
    with open(filepath) as f:
        file_contents = f.read()
    
    file_contents = file_contents.lower()
    for letter in file_contents:
        if type(letter) == "int":
            str(letter)
            
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    return letter_count