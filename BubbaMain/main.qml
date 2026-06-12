import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {
    id: root
    visible: true
    width: 400
    height: 400
    title: "Bubba Bacan"
    flags: Qt.Window | Qt.FramelessWindowHint
    color: "#87CEFA"


    
    Rectangle {
        width: 20
        height: 20
        color: "red"
        x: 0
        y:0
        z: 10
        MouseArea {
            anchors.fill: parent
            acceptedButtons: Qt.LeftButton
            onPressed: root.startSystemMove()
        }
    }
}
