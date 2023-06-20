from textual.widgets import Label, Header, Footer, Input, Button

class MyAppWidgets:
    def __init__(self):
        self.header = Header(show_clock=True)
        self.label = Label('Olá Mundo!')
        self.input_field = Input("Digite seu nome: ")
        self.footer = Footer()

        self.buttons = [
            Button("Verde", variant="success"),
            Button("Vermelho", variant="error"),
            Button("Amarelo", variant="warning")
        ]