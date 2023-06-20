from textual.app import App
from textual.widgets import Placeholder, ScrollView, Button
from textual import events

class BookView(App):
    def __init__(self, controller):
        self.controller = controller
        super().__init__()

    async def on_mount(self, event: events.Mount) -> None:
        await self.view.dock(Button("Create", name="create"), edge="top")
        await self.view.dock(Button("Read", name="read"), edge="top")
        await self.view.dock(Button("Update", name="update"), edge="top")
        await self.view.dock(Button("Delete", name="delete"), edge="top")
        await self.view.dock(ScrollView(Placeholder(), name="booklist"), edge="left", size=30)

    async def action_create(self):
        title = await self.ask("Enter title:")
        author = await self.ask("Enter author:")
        self.controller.create_book(title, author)

    async def action_read(self):
        books = self.controller.read_books()
        # Add your logic to display books here

    async def action_update(self):
        id = await self.ask("Enter id of book to update:")
        title = await self.ask("Enter new title:")
        author = await self.ask("Enter new author:")
        self.controller.update_book(id, title, author)

    async def action_delete(self):
        id = await self.ask("Enter id of book to delete:")
        self.controller.delete_book(id)

    async def on_idle(self, event: events.Idle) -> None:
        self.action_read()

    async def on_click(self, event: events.Click) -> None:
        # Handle click event on the book list and CRUD buttons
        pass
