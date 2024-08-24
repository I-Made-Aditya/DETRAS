import QtQuick 2.15
import QtQuick.Controls 2.15
import QtMultimedia 5.15

ApplicationWindow {
    id: root

    width: 800
    height: 600

    VideoOutput {
        id: videoOutput

        source: MediaPlayer {
            id: mediaPlayer

            source: "small.mp4"
            autoPlay: true
        }

        anchors.fill: parent
    }
}