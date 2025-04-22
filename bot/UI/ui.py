from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First Qt App")
        self.setGeometry(100, 100, 300, 150)

        self.layout = QVBoxLayout()

        self.label = QLabel("Hello from Qt!")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.on_button_click)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def on_button_click(self):
        self.label.setText("Button clicked!")