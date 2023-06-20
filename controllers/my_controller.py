# controllers/my_controller.py

from models import MyModel
from views import MyView


class MyController:
    def __init__(self):
        self.model = MyModel()
        self.view = MyView()

    def run(self):
        data = self.model.get_data()
        self.view.display_data(data)
