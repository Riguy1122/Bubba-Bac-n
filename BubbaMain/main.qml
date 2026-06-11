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
    
    DragHandler {
        target: null

        onActiveChanged: {
            if (active) {
                root.startSystemMove()
            }
        }
    }
    Rectangle {
        anchors.fill: parent
        width: 10
        height: 10
        color: "#1395B5"
    }
    
}
