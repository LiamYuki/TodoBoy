"""Custom dialog for adding a new todo item"""
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox
from core.todo import Todo

class AddDialog(QDialog):
    """Dialog for adding a new todo item"""
    def __init__(self):
        """Initialize the dialog"""
        super().__init__()
        self.setWindowTitle("Add Task")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        self.label = QLabel("Enter your task:")
        layout.addWidget(self.label)

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.create_task)
        self.buttonBox.rejected.connect(self.reject)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

    def create_task(self):
        """Handle the ceation of a new task"""
        if self.input_field.text():
            print(Todo(self.input_field.text()).content())
            self.accept()