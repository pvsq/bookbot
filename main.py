def main():
    filename = "books/frankenstein.txt"
    file_contents = get_file_contents(filename)
    word_count = count_words(file_contents)
    letter_count_dict = count_letters(file_contents)
    print("Count of each letter in text:")
    print(letter_count_dict)

def get_file_contents(filename):
    with open(filename) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_letters(text):
    letter_count_dict = {}
    for i in range(0, len(text)):
        letter = text[i].lower()
        if letter not in letter_count_dict:
            letter_count_dict[letter] = 0
        letter_count_dict[letter] += 1
    return letter_count_dict

main()
