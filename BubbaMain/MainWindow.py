import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import QTimer
from moods import mood_dict
from UtilityLogic import get_all_stats
from moods import get_system_mood
from PySide6.QtQ

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        title = "Bubba Bacán"
        wi, hi = 500, 400
        stats = get_all_stats()
        

        self.resize(wi, hi)
        self.setWindowTitle(title)

        self.primary_label = QLabel("Finding mood...")
        self.message_label = QLabel("getting stats...")
        self.modifiers_label = QLabel("")
        layout = QVBoxLayout()

        layout.addWidget(self.primary_label)
        layout.addWidget(self.message_label)
        layout.addWidget(self.modifiers_label)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect((self.update_bubba))
        self.timer.start(500)
        

    def update_bubba(self):
        stats = get_all_stats()
        mood = get_system_mood(stats)
        #print(stats)
        print(mood)
        self.primary_label.setText(mood["primary"])
        self.message_label.setText(mood["message"])
        self.modifiers_label.setText("\n".join(mood["modifiers"]))
        #self.setStyleSheet()




if __name__ == "__main__":
    print(get_all_stats())
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())