import os
import sys
import sqlite3

from result import Result
from student import Student
from course import Course


class ResultsManager:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(
            sys.path[0], 'studentresults.db'))
        self.dbc = self.conn.cursor()

    def create_tables(self):
        self.dbc.execute('''CREATE TABLE IF NOT EXISTS courses
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          points INTEGER NOT NULL);''')

        self.dbc.execute('''CREATE TABLE IF NOT EXISTS students
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          first_name TEXT NOT NULL,
                          last_name TEXT NOT NULL,
                          date_of_birth DATE NOT NULL,
                          class_code TEXT NULL);''')

        self.dbc.execute('''CREATE TABLE IF NOT EXISTS results
                         (student_id INTEGER NOT NULL,
                          course_id INTEGER NOT NULL,
                          mark INTEGER NOT NULL,
                          achieved DATE NOT NULL,
                          PRIMARY KEY(student_id, course_id, mark));''')

        self.conn.commit()

    def get_course(self, course_id) -> Course:
        self.dbc.execute(
            "SELECT id, name, points FROM courses WHERE id = ?",
            (course_id,)
        )
        table_row = self.dbc.fetchone()
        if not table_row:
            return None
        return Course(table_row[1], table_row[2], id=table_row[0])

    def add_course(self, course: Course) -> Course:
        self.dbc.execute(
            "INSERT INTO courses (name, points) VALUES (?, ?)",
            (course.name, course.points)
        )
        self.conn.commit()
        course.id = self.dbc.lastrowid
        return course

    def get_student(self, student_id) -> Student:
        self.dbc.execute(
            "SELECT id, first_name, last_name, date_of_birth, class_code FROM students WHERE id = ?",
            (student_id,)
        )
        table_row = self.dbc.fetchone()
        if not table_row:
            return None
        return Student(table_row[1], table_row[2], table_row[3], table_row[4], id=table_row[0])

    def add_student(self, student: Student) -> Student:
        self.dbc.execute(
            "INSERT INTO students (first_name, last_name, date_of_birth, class_code) VALUES (?, ?, ?, ?)",
            (student.first_name, student.last_name, student.date_of_birth, student.class_code)
        )
        self.conn.commit()
        student.id = self.dbc.lastrowid
        return student

    def add_result(self, result: Result) -> bool:
        self.dbc.execute(
            "SELECT MAX(mark) FROM results WHERE student_id = ? and course_id = ?",
            (result.student_id, result.course_id)
        )
        table_row = self.dbc.fetchone()
        highest = table_row[0]
        if highest is None or result.mark > highest:
            self.dbc.execute(
                "INSERT INTO results (student_id, course_id, mark, achieved) VALUES (?, ?, ?, ?)",
                (result.student_id, result.course_id, result.mark, result.achieved)
            )
            self.conn.commit()
            return True
        return False

    def get_results_by_student(self, student_id, only_last=True):
        if only_last:
            requested = """
                SELECT student_id, course_id, MAX(mark), achieved
                FROM results
                WHERE student_id = ?
            """
        else:
            requested = """
                SELECT student_id, course_id, mark, achieved
                FROM results
                WHERE student_id = ?
            """
        self.dbc.execute(requested, (student_id,))
        table_rows = self.dbc.fetchall()
        return table_rows

    def get_results_by_course(self, course_id, only_last=True):
        if only_last:
            requested = """
                SELECT student_id, course_id, MAX(mark), achieved
                FROM results
                WHERE course_id = ?
            """
        else:
            requested = """
                SELECT student_id, course_id, mark, achieved
                FROM results
                WHERE course_id = ?
            """
        self.dbc.execute(requested, (course_id,))
        table_rows = self.dbc.fetchall()
        return table_rows

    def close(self):
        self.conn.close()
