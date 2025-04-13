from stats import word_count , char_counter , char_count_sort
import sys

if len(sys.argv) != 2 :
    print("Usage: Python3 min.py <path_to_book>")

book = sys.argv[1]

def get_book_text(book):

    with open(book) as b:
        book_text = b.read()

    return book_text

def main ():
    book_text = get_book_text(book)
    count = word_count(book_text)
    char_count =char_counter(book_text)
    char_sort = char_count_sort(char_count)
    char_list = print_char_count(char_sort)

    original_format = f"""
    ============ BOOKBOT ============
    Analyzing book found at {book}...
    ----------- Word Count ----------
    Found {count} total words
    --------- Character Count -------
{char_list}

    ============= END ===============

    """
    print(original_format)


def print_char_count(char_count_sort):
    char_list = ""
    for char in char_count_sort:
        for key , value in char.items():
            if key.isalpha():
                char_list += f"{key}:{value}\n"



    return char_list

main()
