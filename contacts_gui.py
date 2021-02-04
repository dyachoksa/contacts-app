# Import system packages
import sys

# Import widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# Cate an instance of application
app = QApplication(sys.argv)

# Setup simple GUI
window = QWidget()
window.setWindowTitle("Contacts App")
window.setGeometry(100, 100, 280, 80)

helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)

# Show main window
window.show()

# Run application's event loop
exit_code = app.exec_()

sys.exit(exit_code)
