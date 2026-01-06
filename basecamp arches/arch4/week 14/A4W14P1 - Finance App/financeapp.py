import os
import sys
import json
import sqlite3

from datetime import datetime
from transaction import Transaction


class FinanceApp:
    def __init__(self, db_name='finance.db'):
        self.connection = sqlite3.connect(os.path.join(sys.path[0], db_name))
        self.cursor = self.connection.cursor()

    def build_database(self):
        self.cursor.execute("DROP TABLE IF EXISTS transactions")
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY,
                            date TEXT,
                            description TEXT,
                            category TEXT,
                            amount REAL)''')
        self.connection.commit()

    def load_transactions_from_json(self, json_file):
        with open(os.path.join(sys.path[0], json_file), 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            for i in range(len(json_data)):
                date = datetime.strptime(json_data[i]['date'], "%d-%m-%Y").strftime("%Y-%m-%d")
                description = json_data[i]['description']
                category = json_data[i]['category']
                amount = json_data[i]['amount']
                self.cursor.execute("""
                                    INSERT INTO transactions (
                                        date,
                                        description,
                                        category,
                                        amount) VALUES(?, ?, ?, ?)""", (date, description, category, amount))
                self.connection.commit()

    def add_transaction(self, date, description, category, amount) -> Transaction:
        self.cursor.execute("""
                            INSERT INTO transactions (
                                date,
                                description,
                                category,
                                amount) VALUES(?, ?, ?, ?)""", (date, description, category, amount))
        self.connection.commit()
        id_ = self.cursor.lastrowid
        transaction = Transaction(id_, date, description, category, amount)
        return transaction.__repr__()

    def update_transaction(self, transaction_id, date, description, category, amount) -> bool:
        if date == "":
            date = None
        elif description == "":
            description = None
        elif category == "":
            category = None
        self.cursor.execute("""
                            UPDATE transactions
                            SET
                                date = COALESCE(?, date),
                                description = COALESCE(?, description),
                                category = COALESCE(?, category),
                                amount = COALESCE(?, amount)
                            WHERE id = ?
                            """, (date, description, category, amount, transaction_id))
        self.connection.commit()
        return True

    def delete_transaction(self, transaction_id) -> bool:
        self.cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
        self.connection.commit()
        return True

    def search_transactions(self, term: str) -> list[Transaction]:
        Listt = []
        self.cursor.execute("""
                            SELECT * FROM transactions WHERE category = ? OR description = ?
                            """, (term, term))
        List = self.cursor.fetchall()
        for i, item in enumerate(List):
            id_, date, description, category, amount = item
            Listt.append(Transaction(id_, date, description, category, amount))
        return Listt

    def get_transactions(self, year: int | None = None) -> list[Transaction]:
        Listt = []
        if year == "":
            # fetch all
            self.cursor.execute("SELECT * FROM transactions")
        else:
            self.cursor.execute("""
                SELECT *
                FROM transactions
                WHERE date BETWEEN ? AND ?
            """, (f"{year}-01-01", f"{year}-12-31"))
        List = self.cursor.fetchall()
        for i, item in enumerate(List):
            id_, date, description, category, amount = item
            Listt.append(Transaction(id_, date, description, category, amount))
        return Listt

    def get_expenses(self, year: int | None = None) -> list[tuple[str, float]]:
        if year is not None:
            self.cursor.execute("""SELECT category, SUM(amount)
                                FROM transactions WHERE amount < 0 AND LOWER(category) != ? AND LOWER(category) != ? AND date BETWEEN ? AND ?
                                GROUP BY category
                                ORDER BY SUM(amount) DESC
                                """, ("work", "savings", f"{year}-01-01", f"{year}-12-31"))
        else:
            self.cursor.execute("""SELECT category, SUM(amount)
                                FROM transactions WHERE amount < 0 AND LOWER(category) != ? AND LOWER(category) != ?
                                GROUP BY category
                                ORDER BY SUM(amount) DESC
                                """, ("work", "savings",))
        return self.cursor.fetchall()
        

    def get_savings(self) -> list[tuple[str, float]]:
        self.cursor.execute("""
                            SELECT
                                CAST(strftime('%Y', date) AS INTEGER) AS year,
                                SUM(amount)
                            FROM transactions
                            WHERE category = ?
                            GROUP BY year
                            ORDER BY year ASC
                            """, ("Savings",))
        return self.cursor.fetchall()

    def count_transactions(self, year: int | None = None) -> int:
        return len(self.get_transactions(year))

    def get_report(self, year: int | None = None) -> dict[str, float]:
        report = {}
        tot = []
        if year != "":            
            expenses = self.get_expenses(year)
            savings = self.get_savings()
            transactions = self.count_transactions(year)
            for i in range(len(savings)):
                if savings[i][0] == int(year):
                    tot.append(float(savings[i][1]) * -1)
            tot_save = tot[0]
            tot_expens = sum(amount for _, amount in expenses)
            self.cursor.execute("SELECT amount FROM transactions WHERE category = ? AND date BETWEEN ? AND ?", ("Work", f"{year}-01-01", f"{year}-12-31"))
            Income = self.cursor.fetchall()
            income = sum(row[0] for row in Income)
            Total = income + tot_save + tot_expens
            report["Transactions"] = transactions
            report["Income"] = round(income, 2)
            report["Expenses"] = round(tot_expens, 2)
            report["Savings"] = round(tot_save, 2)
            report["Total"] = round(Total, 2)
            return report
        else:
            return None