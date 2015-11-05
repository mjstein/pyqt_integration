from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtCore import pyqtProperty, QObject, QUrl
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine, QQmlApplicationEngine
import sys

class Person(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialise the value of the properties.
        self._name = 'YUM'
        self._shoeSize = 0

    # Define the getter of the 'name' property.  The C++ type of the
    # property is QString which Python will convert to and from a string.
    @pyqtProperty('QString')
    def name(self):
        return self._name

    # Define the setter of the 'name' property.
    @name.setter
    def name(self, name):
        self._name = name

    # Define the getter of the 'shoeSize' property.  The C++ type and
    # Python type of the property is int.
    @pyqtProperty(int)
    def shoeSize(self):
        return self._shoeSize

    # Define the setter of the 'shoeSize' property.
    @shoeSize.setter
    def shoeSize(self, shoeSize):
        self._shoeSize = shoeSize

app = QApplication(sys.argv)
qmlRegisterType(Person, "People", 1, 0, "Person")
view = QQuickView()
view.setSource(QUrl("example.qml"))
view.show()

app.exec()
