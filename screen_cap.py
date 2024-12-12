from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys 
import keyboard
  
"""
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 

        # Hide the Top Bar
        self.setWindowFlag(Qt.FramelessWindowHint) 
        # Set Window Title
        self.setWindowTitle("Python") 
        # Set Window poacity
        self.setWindowOpacity(0.5) 
  
  
        # setting  the geometry of window 
        self.setGeometry(60, 60, 600, 400) 
  
        # creating a label widget 
        # self.label_1 = QLabel("transparent ", self) 
        # self.label_1.move(100, 100) 
        # self.label_1.adjustSize() 
  
        # show all the widgets 
        self.show() 
"""

class FramelessWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.label = QLabel("Hello world", self)
        self.offset = None
        self.setWindowOpacity(0.03) 


        # https://stackoverflow.com/questions/62807295/how-to-resize-a-window-from-the-edges-after-adding-the-property-qtcore-qt-framel
        self.gripSize = 16
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self)
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)

    def resizeEvent(self, event):
        QWidget.resizeEvent(self, event)
        rect = self.rect()
        # top left grip doesn't need to be moved...
        # top right
        self.grips[1].move(rect.right() - self.gripSize, 0)
        # bottom right
        self.grips[2].move(
            rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        # bottom left
        self.grips[3].move(0, rect.bottom() - self.gripSize)

    """
    https://stackoverflow.com/questions/58901806/how-to-make-my-title-less-window-drag-able-in-pyqt5
    """
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = FramelessWidget()
    win.setGeometry(300, 300, 300, 300)
    win.show()
    sys.exit(app.exec_())
