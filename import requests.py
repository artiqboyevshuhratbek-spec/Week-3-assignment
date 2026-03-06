import requests

def analyze_subject(subject):
    print("Fetching top 10 results...")
    url = "https://openlibrary.org/search.json"
    params = {
        "q": subject,
        "limit": 10,
        "fields": "title,author_name,first_publish_year,number_of_pages_median"
    }

    response = requests.get(url, params=params)
    data = response.json()
    books = data.get("docs", [])

    thickest_book = None
    oldest_book = None

    for book in books:
        # Safely check for page count
        if "number_of_pages_median" in book and isinstance(book["number_of_pages_median"], int):
            if (thickest_book is None or
                book["number_of_pages_median"] > thickest_book["number_of_pages_median"]):
                thickest_book = book

        # Safely check for publish year
        if "first_publish_year" in book and isinstance(book["first_publish_year"], int):
            if (oldest_book is None or
                book["first_publish_year"] < oldest_book["first_publish_year"]):
                oldest_book = book

    print("\n--- Analysis Results ---")
    if thickest_book:
        print("Thickest Book:")
        print(f"Title: {thickest_book.get('title', 'Unknown')}")
        print(f"Pages: {thickest_book['number_of_pages_median']}")
    else:
        print("No book with page count found.")

    if oldest_book:
        print("\nOldest Book:")
        print(f"Title: {oldest_book.get('title', 'Unknown')}")
        print(f"Year: {oldest_book['first_publish_year']}")
    else:
        print("No book with publication year found.")

# Main program
subject = input("Enter a subject: ")
analyze_subject(subject)