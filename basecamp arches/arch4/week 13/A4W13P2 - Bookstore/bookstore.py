import os
import sys
import json
import math
import sqlite3
from datetime import datetime, timedelta
menu = """
[B] Borrow book
[R] Return book
[S] Search book
[Q] Quit program
"""
books = []
book = {}


def load_json():
    path = os.path.dirname(__file__)
    file = os.path.join(path, "books.json")
    try:
        with open(file, "r") as fr:
            json_data = json.load(fr)
            return json_data
    except FileNotFoundError:
        print("file was not found")


def main():
    con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
    con.execute(
        '''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL,
            year TEXT NOT NULL,
            status TEXT DEFAULT "AVAILABLE",
            return_date DATE DEFAULT NULL
        );'''
    )
    cur = con.cursor()
    files = load_json()
    for file in files:
        isbn = file["isbn"]
        title = file["title"]
        author = file["author"]
        pages = file["pages"]
        year = file["year"]
        cur.execute("SELECT * FROM books WHERE isbn = ?", (isbn,))
        data = cur.fetchone()
        if data is None:
            cur.execute("""
                        INSERT INTO books (
                            isbn,
                            title,
                            author,
                            pages,
                            year) VALUES(?, ?, ?, ?, ?)
                        """, (isbn, title, author, pages, year))
            con.commit()
    cur.execute("SELECT * FROM books")
    items = cur.fetchall()
    for item in items:
        book_id, isbn, title, author, pages, year, status, return_date = item
        book = {
            "id": book_id,
            "isbn": isbn,
            "title": title,
            "author": author,
            "pages": pages,
            "year": year,
            "status": status,
            "return_date": return_date
            }
        books.append(book)
    print(menu)
    menu_choice = input("type the corresponding letter on your keyboard\n>").upper()
    if menu_choice == "Q":
        quit()
    elif menu_choice == "B":
        id_book = input("enter the book (id/isbn)\n>")
        days_borrow = int(input("how many days are you borrowing it?\n>"))
        cur.execute("SELECT status FROM books WHERE id = ? OR isbn = ?", (id_book, id_book))
        book_status = cur.fetchone()[0]
        if book_status == "BORROWED":
            print("book is borrowed at this time")
        elif book_status == "AVAILABLE":
            date_now = datetime.now().date()
            return_date = date_now + timedelta(days=days_borrow)
            return_date = return_date.strftime("%d-%m-%Y")
            cur.execute("UPDATE books SET status = ?, return_date = ? WHERE id = ? OR isbn = ?", ('BORROWED', return_date, id_book, id_book))
            con.commit()
            print(return_date)
    elif menu_choice == "R":
        id_book = input("enter the book (id/isbn)\n>")
        cur.execute("SELECT status, return_date FROM books WHERE id = ? OR isbn = ?", (id_book, id_book))
        status, return_date = cur.fetchone()
        if status == "AVAILABLE":
            print("this books has not been borrowed")
        elif status == "BORROWED":
            date_now = datetime.now().date()
            end_date = datetime.strptime(return_date, "%d-%m-%Y").date()
            difference = (date_now - end_date).days
            if difference < 0:
                print("returned")
            else:
                fine = difference * 0.50
                print(fine)
            cur.execute("UPDATE books SET status = ?, return_date = ? WHERE id = ? OR isbn = ?", ("AVAILABLE", None, id_book, id_book))
            con.commit()
    elif menu_choice == "S":
        search_input = input("search for (title/isbn/author)\n>")
        for book in books:
            if search_input in book.values():
                print(book)


if __name__ == "__main__":
    main()