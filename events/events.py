from textual.widgets import Button, Input

class MyAppEvents:
    def __init__(self, app, widgets):
        self.app = app
        self.widgets = widgets

    def on_button_pressed(self, event: Button.Pressed):
        self.widgets.label.update(f'Cliquei no botão {event.button.label}')

    def on_input_changed(self, event: Input.Changed):
        self.widgets.label.update(f'Olá {event.input.value}')

    def on_input_submitted(self, event: Input.Submitted):
        self.widgets.label.update(f'Olá [red]{event.input.value}[/]')