"""User interface"""
from core.AddDialog import AddDialog
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout
from PyQt6.QtCore import QSize

class Window(QMainWindow):
    """Customizable window class"""
    def __init__(self):
        """Creates the application window"""
        super().__init__()
        self.setWindowTitle("TodoBoy")
        self.setFixedSize(QSize(600,800))

        layout = QGridLayout()
        layout.addLayout(self._setup_button_layout(), 3, 2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _setup_button_layout(self):
        """Style buttons for the window"""
        add_btn = QPushButton("Add", self)
        add_btn.clicked.connect(self.add_task)

        button_layout = QHBoxLayout()
        button_layout.addWidget(add_btn)

        return button_layout

    def add_task(self):
        dialog = AddDialog()
        dialog.exec()