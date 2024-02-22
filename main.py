def main():
    filename = "books/frankenstein.txt"
    file_contents = get_file_contents(filename)
    print(file_contents)
    print(f.closed)

def get_file_contents(filename):
    with open(filename) as f:
        file_contents = f.read()
    return file_contents
