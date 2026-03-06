def clean_titles(book_list):
    cleaned_list = []
    for book in book_list:
        book = book.strip()
        if book:
            formatted_book = book.title()
            cleaned_list.append(formatted_book)
    return cleaned_list










raw_books = [
    "  great gatsby ",
    "MOBY DICK",
    "   ",
    "the catcher in the rye",
    "war and PEACE  "
]

# Run the function
print(clean_titles(raw_books))