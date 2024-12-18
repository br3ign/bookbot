book_path = "books/frankenstein.txt"
file_contents = ""

def count_words(file):
    word_count = 0
    for word in file.split():
        word_count += 1
    return word_count

def count_characters(file):
    global char_counter
    char_dict = {}
    
    for word in file.split():
        lowered_string = word.lower()
        for char in lowered_string:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    
    return char_dict

def sort_on(ch_dict):
    return ch_dict["count"]

def report():
    word_count = count_words(file_contents)
    char_counter = count_characters(file_contents)

    character = []
    for char in char_counter:
        if char.isalpha():
            character.append({"name":char,"count":char_counter[char]})
    
    character.sort(reverse=True, key=sort_on)

    print(f"--- Begin report or {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for c in character:
        print(f"The '{c["name"]}' character was found {c["count"]} times.")
    
    print(f"--- End report ---")

def main():
    global file_contents
    with open(book_path) as f:
        file_contents = f.read()
        f.close()
    
    report()

main()
