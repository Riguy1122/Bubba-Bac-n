import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from moods import mood_list

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        title = "Bubba Bacán"
        wi, hi = 500, 400
        self.current_mood = 0
        
        self.resize(wi, hi)
        self.setWindowTitle(title)

        self.button = QPushButton("Next mood")
        self.label = QLabel(mood_list[self.current_mood]["message"])
        layout = QVBoxLayout()

        self.button.clicked.connect(self.cycle_mood)

        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def cycle_mood(self):
        self.current_mood = (self.current_mood + 1) % len(mood_list)
        self.label.setText(mood_list[self.current_mood]["message"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())