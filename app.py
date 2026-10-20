"""Application Entry Point"""
from core.ui import Window
from PyQt6.QtWidgets import QApplication

# Grab context, only one instance required
context = QApplication([])

# Create window and show it
window = Window()
window.show()

# Start the event loop
context.exec()

