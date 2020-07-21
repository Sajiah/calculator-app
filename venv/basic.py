import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
                             QHBoxLayout, QVBoxLayout,
                             QPushButton, QLabel)


# main window class and set initialization function to run our code
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # create a button pass text in button called ok

        label = QLabel("Hi there, I'm a label.  Woot.")
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        # Horizontal layout. If you change H to V, it will be a vertical layout
        horizontal = QHBoxLayout()
        horizontal.addStretch(1)

        # Allows you to add widget (label, pushbutton, notebook etc)
        horizontal.addWidget(okButton)
        horizontal.addWidget(cancelButton)


        vertical = QVBoxLayout()
        vertical.addStretch(1)
        # Add the horizontal layout to the vertical layout
        vertical.addWidget(label)
        vertical.addLayout(horizontal)


        self.setLayout(vertical)

        self.setWindowTitle("Horizontal Layout")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # Until it exits, it will run the code
    sys.exit(app.exec_())


