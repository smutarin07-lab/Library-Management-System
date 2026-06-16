


library = []

def add_book(title, author, year):
    library.append({"title": title, "author": author, "year": year, "available": True})

add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
add_book("To Kill a Mockingbird", "Harper Lee", 1960)
add_book("1984", "George Orwell", 1949)
add_book("Pride and Prejudice", "Jane Austen", 1813)
add_book("The Catcher in the Rye", "J.D. Salinger", 1951)
add_book("The Lord of the Rings", "J.R.R. Tolkien", 1954)
add_book("The Hobbit", "J.R.R. Tolkien", 1937)
add_book("The Adventures of Huckleberry Finn", "Mark Twain", 1884)
add_book("The River and the Source", "Margaret Ogola", 1990)
add_book("The Alchemist", "Paulo Coelho", 1988)

print("Books in the library:")
for book in library:
    print(f"{book['title']} by {book['author']} ({book['year']})")

def view_books():
    for book in library:
        status = "Available" if book["available"] else "Borrowed"

        print(
            f"{book['title']} by {book['author']} "
            f"({book['year']}) - {status}"
        )



def borrow_book(title):
    for book in library:
        if book['title'].lower() == title.lower():
            if book["available"]:
                book["available"] = False
                return f"You have borrowed '{book['title']}' by {book['author']} ({book['year']})."
            else:
                return f"'{book['title']}' is already borrowed."
    return "Book not found in the library."
        

def return_book(title, author, year):
    for book in library:
        if book['title'].lower() == title.lower() and book['author'].lower() == author.lower() and book['year'] == year:
            if not book["available"]:
                book["available"] = True
                return f"You have returned '{book['title']}' by {book['author']} ({book['year']})."
            else:
                return "This book was not borrowed."
    return "Book not found in the library."


def remove_book(title):
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            return f"'{book['title']}' has been removed from the library."
    return "Book not found in the library."

def search_book(title):
    for book in library:
        if book['title'].lower() == title.lower():
            return f"Found '{book['title']}' by {book['author']} ({book['year']})."
    return "Book not found in the library."

while True:
    print("1. View Books")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Remove Book")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")
    print(f"Choice: {choice}")

    if choice == "1":
        view_books()
    elif choice == "2":
        title = input("Enter the title of the book you want to search: ")
        print(search_book(title))
    elif choice == "3":
        title = input("Enter the title of the book you want to borrow: ")
        print(borrow_book(title))
    elif choice == "4":
        title = input("Enter the title of the book you want to return: ")
        author = input("Enter the author of the book: ")
        year = int(input("Enter the publication year of the book: "))
        print(return_book(title, author, year))
    elif choice == "5":
        title = input("Enter the title of the book you want to remove: ")
        print(remove_book(title))
    elif choice == "6":
        print("Exiting the library management system.")
        break
    else:
        print("Invalid choice.")
  

