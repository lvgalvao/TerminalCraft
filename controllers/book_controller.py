from models import Book
from views import BookListView
from views import BookDetailView

class BookController:
    def __init__(self):
        self.model = Book()
        self.current_view = BookListView(controller=self)

    def start(self):
        self.current_view.run()

    def create_book(self, title, author):
        self.model.create(title, author)

    def read_books(self):
        return self.model.read()

    def read_book(self, id):
        return self.model.read(id)

    def update_book(self, id, title, author):
        self.model.update(id, title, author)

    def delete_book(self, id):
        self.model.delete(id)

    def switch_to_detail_view(self, id):
        self.current_view = BookDetailView(controller=self, book_id=id)
        self.current_view.run()

    def switch_to_list_view(self):
        self.current_view = BookListView(controller=self)
        self.current_view.run()
