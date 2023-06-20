from textual import events
from textual.app import App
from textual.widgets import Button, ScrollView, TextField


class BookDetailView(App):
    def __init__(self, controller, book_id):
        self.controller = controller
        self.book_id = book_id
        super().__init__()

    async def on_mount(self, event: events.Mount) -> None:
        self.title_field = TextField(read_only=True)
        self.author_field = TextField(read_only=True)
        await self.view.dock(Button('Back', name='back'), edge='top')
        await self.view.dock(
            ScrollView(self.title_field, name='title'), edge='left', size=30
        )
        await self.view.dock(
            ScrollView(self.author_field, name='author'), edge='left', size=30
        )

    async def action_back(self):
        self.controller.switch_to_list_view()

    async def action_read(self):
        book = self.controller.read_book(self.book_id)
        self.title_field.text = book['title']
        self.author_field.text = book['author']

    async def on_idle(self, event: events.Idle) -> None:
        self.action_read()
