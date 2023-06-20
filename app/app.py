from textual.app import App
from widgets import MyAppWidgets
from events import MyAppEvents
from textual.containers import Horizontal
from textual.widgets import Button, Input



class MyApp(App):
    TITLE = "Meu App Topzera"

    def __init__(self):
        super().__init__()

        self.widgets = MyAppWidgets()
        self.events = MyAppEvents(self, self.widgets)

        # Bind events to handlers
        self.bind(Button.Pressed, self.events.on_button_pressed)
        self.bind(Input.Changed, self.events.on_input_changed)
        self.bind(Input.Submitted, self.events.on_input_submitted)

    def compose(self):
        yield self.widgets.header
        yield self.widgets.label
        yield self.widgets.input_field

        with Horizontal():
            for button in self.widgets.buttons:
                yield button

        yield self.widgets.footer