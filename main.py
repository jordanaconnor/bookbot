from stats import count_words

frankenstein_path = "books/frankenstein.txt"

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # print(f.read())
        file_contents = f.read()
    return file_contents

def main():
    books_text = get_book_text(frankenstein_path)
    count = count_words(books_text)
    print(f"Found {count} total words")

if __name__ == "__main__":
    main()