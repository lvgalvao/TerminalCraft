from models.db import get_db

class Book:
    def __init__(self):
        self.db = get_db()

    def create(self, title, author):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        self.db.commit()

    def read(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM books")
        return cursor.fetchall()

    def update(self, id, title, author):
        cursor = self.db.cursor()
        cursor.execute("UPDATE books SET title = ?, author = ? WHERE id = ?", (title, author, id))
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (id,))
        self.db.commit()

    def read_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM books WHERE id=?", (id,))
        return cursor.fetchone()