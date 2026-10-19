from datetime import date

class Todo:
    def __init__(self, message):
        self.message = message
        self.date = date.today()
        self.finished = False

    def content(self):
        return f'{self.date}: {self.message}'

    def edit(self, message):
        self.message = message
        self.date = date.today()

    def complete(self):
        self.finished = True