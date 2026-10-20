"""User interface"""
import core.handler as handler
from PyQt6.QtWidgets import QMainWindow, QPushButton
from PyQt6.QtCore import QSize

# Customizable window class
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TodoBoy")
        self.setFixedSize(QSize(600,800))

        add_btn = QPushButton("Add Task", self)
        add_btn.clicked.connect(handler.handle_add_task)
        del_btn = QPushButton("Delete Task", self)
        del_btn.clicked.connect(handler.handle_delete_task)
        edit_btn = QPushButton("Edit Task", self)
        edit_btn.clicked.connect(handler.handle_edit_task)

