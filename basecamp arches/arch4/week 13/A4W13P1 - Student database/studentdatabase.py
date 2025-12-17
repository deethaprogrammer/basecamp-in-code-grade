import os
import sys
import sqlite3

menu = """
[A] Add new student
[C] Assign student to class
[D] List all students
[L] List all students in class
[S] Search student
[Q] Quit program
"""


def main():
    con = sqlite3.connect(os.path.join(sys.path[0], 'studentdatabase.db'))
    con.execute(
        '''CREATE TABLE IF NOT EXISTS students (
            studentnumber INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            class TEXT DEFAULT NULL
        );'''
    )
    cur = con.cursor()
    print(menu)
    menu_choice = input("press the corresponding key.\n>").upper()
    if menu_choice == "Q":
        quit()
    elif menu_choice == "A":
        first_name = input("what is your first name?\n>")
        last_name = input("what is your last name?\n>")
        city = input("in what city do you live?\n>")
        date_of_birth = input("when where you born?\n>")
        class_room = input("what is your class?\n>")
        cur.execute("""
                    INSERT INTO students (
                        first_name,
                        last_name,
                        city,
                        date_of_birth,
                        class) VALUES(?, ?, ?, ?, ?)""", (first_name, last_name, city, date_of_birth, class_room))
        con.commit()

        student_ID = cur.lastrowid

        print(student_ID)
    elif menu_choice == "C":
        student_id = input("what is the id of the student?\n>")
        class_room = input("what class?\n>")
        cur.execute("SELECT * FROM students WHERE studentnumber = ?",
                    (student_id,))
        student_ID = cur.fetchone()
        if student_ID is None:
            print(f"Could not find student with number: {student_id}")
        else:
            cur.execute("UPDATE students SET class = ? WHERE studentnumber = ?",
                        (class_room, student_id))
            con.commit()
    elif menu_choice == "D":
        cur.execute("SELECT * FROM students ORDER BY class DESC")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    elif menu_choice == "L":
        class_room = input("what class?\n>")
        cur.execute("SELECT * FROM students WHERE class = ? ORDER BY studentnumber ASC",
                    (class_room,))
        students = cur.fetchall()
        for student in students:
            print(student)
    elif menu_choice == "S":
        variable = input("what is the students first name, last name or city?\n>")
        cur.execute("SELECT * FROM students WHERE first_name = ? OR last_name = ? OR city = ?",
                    (variable, variable, variable))
        item = cur.fetchone()
        print(item)


if __name__ == "__main__":
    main()