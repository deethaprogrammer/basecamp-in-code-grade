"""
---menu---
[A] Add book
[S] Search book
[E] Exit (and print)

---criteria---
entering a new book: The program ask to enter: book title, book author, publisher, publication date.
the input will be single lined with a comma between each part.
the book can only be added to the list once

searching a book: the user enters a term and the program needs to search that term within the titles, authors and publishers
it needs to report the existence of such a book with the requested term
seaching needs to be the function search_book(book, term) -> bool:

use a list of dictionaries for datastorage with the following attribute fields [title, author, publisher, pub_date]
"""

books = []

def search_book(books, term) -> bool:    
    for book in books:            
        if term.lower() in book.values():            
            return True
    return False


def menu(choice):
    keys = ['title', 'author', 'publisher', 'pub_date']
    
    if choice == 'A':        
        Add_Book = input("Book details: ").lower()
        value = [v.strip() for v in Add_Book.split(",")]
        
        if len(value) != len(keys):
            print("not a valid input")
            return
        book_dict = dict(zip(keys, value))
        
        if book_dict not in books:
            books.append(book_dict)
            print('Book has been added')        
        else:    
            print('Book has already been added')

    elif choice == 'S':        
        term = input("Search term: ")        
        if search_book(books, term) == True:            
            print(f'Found a book for: {term}')        
        else:
            print(f'There is no book for the term: {term}')
        
    elif choice == 'E':
        return "False"

def main():    
    while True:        
        choice = input("[A] Add book\n[S] Search book\n[E] Exit\nWhat do you choose: ").upper()
        if menu(choice) == "False":
            for book in books:
                print(book)               
            break
        
if __name__ == "__main__":
    main()