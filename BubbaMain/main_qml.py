import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

qml_path = Path(__file__).parent / "main.qml"
engine.load(QUrl.fromLocalFile(str(qml_path)))

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())