import sys
from PyQt4 import QtCore, QtGui


class TestWindow(QtGui.QWidget):
    def __init__(self, parent = None):
        super(TestWindow, self).__init__(parent)
        self.setWindowTitle(u'cccc')

        self.pushButton = QtGui.QPushButton(u'ccccc')

        self.textEdit = QtGui.QTextEdit()

        layout = QtGui.QVBoxLayout()

        layout.addWidget(self.textEdit)
        layout.addWidget(self.pushButton)

        self.setLayout(layout)

        self.pushButton.clicked.connect(self.sayHello)

    def sayHello(self):
        self.textEdit.setText('Hello World!')


if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = TestWindow()
    mainWindow.show()
    sys.exit(app.exec_())