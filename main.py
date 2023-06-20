from textual import on
from textual.app import App
from textual.widgets import Label, Header, Footer, Input, Button
from textual.containers import Container
from textual.events import Key
from textual.binding import Binding

class MyApp(App):

    TITLE = "Meu App Topzera"
    CSS_PATH = "static/style.css"

    BINDINGS = [
        # Shortcut, Action, Footer message
       Binding('t', 'change_theme()','Changing theme', show=True),
       Binding('s', 'sair()','Exiting the application', show=True),
    ]

    def action_sair(self):
        self.exit()

    def action_change_theme(self):
        self.dark = not self.dark

    def compose(self):
        with Container(classes='label'):
            yield Label('Hello World!', id='label-principal')

        yield Input("Enter your name: ")

        with Container(classes='buttons'):
            yield Button("Green", variant="success")
            yield Button("Red", variant="error")
            yield Button("Yellow", variant="warning")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed):
        self.query_one('#label-principal').update(f'Clicked on button {event.button.label}')

    def on_input_changed(self, event: Input.Changed):
        self.query_one('#label-principal').update(f'Hello {event.input.value}')

    def on_input_submitted(self, event: Input.Submitted):
        self.query_one('#label-principal').update(f'Hello [red]{event.input.value}[/]')

if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
