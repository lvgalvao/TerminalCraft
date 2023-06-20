# controllers/library_controller.py

from textual.app import App

from models import BookModel
from views import LibraryView


class LibraryController(App):
    def __init__(self):
        self.model = BookModel()
        self.view = LibraryView()

    def run(self):
        books = self.model.get_books()
        self.view.display_books(books)
