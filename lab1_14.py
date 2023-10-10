def insert_book(books_list):
    n = int(input("How many Books would you like to add ?"))
    for i in range(n):
        isbn = input("Enter the ISBN of the book : ")
        title = input("Enter the title of the book : ")
        author = input("Enter the author of the book : ")
        book = (isbn, title, author)
        books_list.append(book)
        print(f"Book {i + 1} inserted successfully.")


def delete_book(books_list):
    isbn = input("Enter the ISBN of the book to delete: ")
    for book in books_list:
        if book[0] == isbn:
            books_list.remove(book)
            print("Book deleted successfully.")
            return
    print("Book with the given ISBN not found.")


def search_book(books_list):  # Searching books using sequential search
    isbn = input("Enter the ISBN of the book to search for: ")
    for book in books_list:
        if book[0] == isbn:
            print("Book found:")
            print("ISBN:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            return
    print("Book with the given ISBN not found.")


def display_books(books_list):
    print("Current book inventory :\n")
    if not books_list:
        print("No books in inventory.")
    else:
        i = 0
        for book in books_list:
            i += 1
            print(f"Book {i} : ")
            print("ISBN:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("")




books = [
    ('9780061120084', 'To Kill a Mockingbird', 'Harper Lee'),
    ('9780142424179', '1984', 'George Orwell'),
    ('9780743273565', 'The Great Gatsby', 'F. Scott Fitzgerald'),
    ('9780060256654', 'Where the Wild Things Are', 'Maurice Sendak'),
    ('9780590353427', 'Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling')
]

while True:
    print("********************** Book Inventory Management **********************")
    print("1. Insert Book")
    print("2. Delete Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. List Operations")
    print("6. Tuple Operations")
    print("7. Type Conversion")
    print("8. Exit")
    print("***********************************************************************")

    ch = input("Enter your choice : ")

    if ch == '1':
        insert_book(books)
    elif ch == '2':
        delete_book(books)
    elif ch == '3':
        search_book(books)
    elif ch == '4':
        display_books(books)
    elif ch == '5':
        while True:
            print("---------- Type Conversion ----------")
            print(
                "1. Tuple to List\n2. List to Tuple\n3. string to list\n4. string to tuple\n5. GO back\n-------------------------------------")
            t = input("Enter ISBN to change the Type : ")

            book_found = None
            for i, book in enumerate(books):
                if book[0] == t:
                    ch1 = input("Enter your choice : ")
                    if ch1 == '1':
                        books[i] = (tuple(book[0]), tuple(book[1]), tuple(book[2]))
                        book_found = books[i]
                    elif ch == '2':
                        books[i] = (list(book[0]), list(book[1]), list(book[2]))
                        book_found = books[i]
                    elif ch == '3':
                        books[i] = list(book[1])
                        book_found = books[i]
                    elif ch == '4':
                        books[i] = tuple(book[1])
                        book_found = books[i]
                    elif ch == '5':
                        break
                    break

            if book_found is not None:
                print("ISBN:", book_found[0], "Type:", type(book_found[0]))
                print("Title:", book_found[1], "Type:", type(book_found[1]))
                print("Author:", book_found[2], "Type:", type(book_found[2]))
            else:
                print("Book not found.")

    elif ch == '9':
        print("************************ Thank you ************************")
        break
    else:
        print("Invalid choice. Please try again.")
    print()
