import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import QTimer
from moods import mood_dict
from UtilityLogic import get_all_stats

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        title = "Bubba Bacán"
        wi, hi = 500, 400
        self.current_mood = 0
        
        self.resize(wi, hi)
        self.setWindowTitle(title)

        self.button = QPushButton("Next mood")
        self.label = QLabel(mood_dict[self.current_mood]["message"])
        self.label2 = QLabel("getting stats...")
        layout = QVBoxLayout()

        self.button.clicked.connect(self.cycle_mood)

        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.label2)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect((self.update_stats))
        self.timer.start(500)



    def update_stats(self):
        self.stats_data = get_all_stats()
        self.cpu = self.stats_data["cpu"]["percent"]
        self.ram = self.stats_data["memory"]["used"]
        self.battery = self.stats_data["battery"]["percent"]
        self.text = f"CPU: {self.cpu}%\nRAM: {self.ram}\nBattery: {self.battery}%"
        self.label2.setText(self.text)

    def cycle_mood(self):
        self.current_mood = (self.current_mood + 1) % len(mood_dict)
        self.label.setText(mood_dict[self.current_mood]["message"])


if __name__ == "__main__":
    print(get_all_stats())
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())