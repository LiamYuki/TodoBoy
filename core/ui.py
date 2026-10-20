from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize

# Customizable window class
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TodoBoy")
        self.setFixedSize(QSize(600,800))

        add_btn = QPushButton("Add Task", self)
        del_btn = QPushButton("Delete Task", self)
        edit_btn = QPushButton("Edit Task", self)

# Grab context, only one instance required
CONTEXT = QApplication([])

# Create window and show it
WINDOW = Window()
WINDOW.show()

# Start the event loop
CONTEXT.exec()