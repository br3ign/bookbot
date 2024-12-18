book_path = "books/frankenstein.txt"


def main():
    with open(book_path) as f:
        file_contents = f.read()
    
    #print(file_contents)
    count_words(file_contents)
    count_characters(file_contents)

def count_words(file):
    word_count = 0
    for word in file.split():
        word_count += 1
    
    #print(word_count)

def count_characters(file):
    char_dict = {}
    counter = 0
    for word in file.split():
        lowered_string = word.lower()
        for char in lowered_string:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    
    print(char_dict)


main()

