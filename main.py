import sys
from PyQt5.QtWidgets import QWidget, QApplication,QMainWindow
from PyQt5.QtGui import QScreen,QPixmap,QImage
from PyQt5 import Qt
from PyQt5.QtCore import QSize
import numpy as np
from MainUI import  Ui_MainWindow
from keras.models import load_model
from keras.models import Sequential

class MainUIObj(QMainWindow):
    def __init__(self):
        super(MainUIObj,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = load_model("./models/cnn")
    def predictNum(self):
        screen=QApplication.primaryScreen()
        # SmoothTransformation
        img=screen.grabWindow(self.ui.widget.winId()).toImage().scaled(QSize(28,28),  transformMode = 1)
        num_pixel=[]
        for y in range(img.height()):
            for x in range(img.width()):
                curr_pixel=img.pixelColor(x,y).red()
                if curr_pixel!=240:
                    num_pixel.append(1)
                else:
                    num_pixel.append(0)
        num_pixel=np.array(num_pixel)
        num_pixel=num_pixel.reshape(1,28,28,1)
        index_num=np.argmax(self.model.predict(num_pixel)[0])
        self.ui.plainTextEdit.setPlainText(str(index_num))



        pass
    def clearPad(self):
        self.ui.widget.clearPad()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw=MainUIObj()
    mw.show()
    sys.exit(app.exec_())


