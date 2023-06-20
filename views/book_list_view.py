from textual.app import App
from textual.widgets import Button, TableView
from textual import events

class BookListView(App):
    def __init__(self, controller):
        self.controller = controller
        super().__init__()

    async def on_mount(self, event: events.Mount) -> None:
        self.table = TableView(headers=["ID", "Title", "Author"])
        await self.view.dock(Button("Create", name="create"), edge="top")
        await self.view.dock(Button("Update", name="update"), edge="top")
        await self.view.dock(Button("Delete", name="delete"), edge="top")
        await self.view.dock(self.table, edge="left", size=30)

    async def action_create(self):
        title = await self.ask("Enter title:")
        author = await self.ask("Enter author:")
        self.controller.create_book(title, author)
        self.action_read()  # Refresh list

    async def action_update(self):
        id = await self.ask("Enter id of book to update:")
        self.controller.switch_to_detail_view(id)

    async def action_delete(self):
        id = await self.ask("Enter id of book to delete:")
        self.controller.delete_book(id)
        self.action_read()  # Refresh list

    async def action_read(self):
        books = self.controller.read_books()
        self.table.data = books
