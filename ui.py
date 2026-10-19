from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow

# Grab context, only one instance required
CONTEXT = QApplication([])

# Create window and show it
WINDOW = QMainWindow() 
WINDOW.show()

# Start the event loop
CONTEXT.exec()