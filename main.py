import sys
print(sys.argv)
from stats import count_words, count_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # print(f.read())
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]




    books_text = get_book_text(book_path)
    count = count_words(books_text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    
    dict_print = count_chars(books_text)

    print("--------- Character Count -------")

    for item in dict_print:
        if item["name"].isalpha():
            print(item["name"] + ": " + str(item["num"]))

    print("============= END ===============")
    

if __name__ == "__main__":
    main()