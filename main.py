
def get_book_text(book):

    with open(book) as b:
        book_text = b.read()

    return book_text


def main ():
    book = "./books/frankenstein.txt"
    book_text = get_book_text(book)
    print(book_text)

main()