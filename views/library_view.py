# views/library_view.py
from textual.widgets import Label


class LibraryView:
    def display_books(self, books):
        print('Library Books:')
        for book in books:
            yield print(
                Label(f"Title: {book['title']}\nAuthor: {book['author']}\n")
            )
