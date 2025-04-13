
def word_count (book_text):
    words = book_text.split()
    return len(words)

def char_counter (book_text):
    char_count = {}
    for char in book_text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def char_count_sort(char_count):
    char_count_list = []
    for count in char_count:
        char_count_list.append({count:char_count[count]}) 
    char_count_list.sort(reverse=True, key=lambda  item_dict: list(item_dict.values())[0])
    return char_count_list

def test():
    book = "./books/frankenstein.txt"
    book = get_book_text(book)
    char_count = char_counter(book)
   # print (char_count)
    print (char_count_sort(char_count))

def get_book_text(book):

    with open(book) as b:
        book_text = b.read()

    return book_text

#test()