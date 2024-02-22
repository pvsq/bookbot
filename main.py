def main():
    filename = "books/frankenstein.txt"
    file_contents = get_file_contents(filename)
    word_count = count_words(file_contents)
    print(f"{word_count} words found")

def get_file_contents(filename):
    with open(filename) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count
