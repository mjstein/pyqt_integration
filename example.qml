import People 1.0
import QtQuick 2.0
Rectangle {
Person {
id: person
name: 'Hello'
}
 Text {
         text: qsTr(person.name)
                 anchors.centerIn: parent
                     }
      id: canvas
      width: 250
      height: 200
      color: "red"
}


