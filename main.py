def main():
    filename = "books/frankenstein.txt"
    file_contents = get_file_contents(filename)
    word_count = count_words(file_contents)
    letter_count_dict = count_letters(file_contents)

    letter_count = []
    for l in letter_count_dict:
        letter_count.append({"char":l, "count":letter_count_dict[l]})

    print_report(filename, word_count, letter_count)


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


def print_report(filename, word_count, letter_count):
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document\n")

    letter_count.sort(reverse=True, key=sort_on_letter_count)

    for lc in letter_count:
        if lc["char"].isalpha():
            print(f"The '{lc["char"]}' character was found {lc["count"]} times")
    print("--- End report --")


def sort_on_letter_count(lc_dict):
    return lc_dict["count"]


main()
