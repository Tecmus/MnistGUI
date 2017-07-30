#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen,QPolygonF,QBrush


class DrawPad(QWidget):
    
    def __init__(self, parent=None):
        super(DrawPad,self).__init__(parent)

        self.initUI()
        
        self.points=[]
        self.is_paint=True

    def initUI(self):      
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()
        
    def mousePressEvent(self, event):
        self.is_paint=True
        
        
    def mouseReleaseEvent(self, event):
        self.is_paint = False       

    def mouseMoveEvent(self, e):
        if self.is_paint==True:
            self.points.append(e.pos())
            self.update()
            
    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()


    def drawPoints(self, qp):
        pen=QPen()
        pen.setWidth(10)
        qp.setPen(pen)
        qp.setBrush(QBrush())
        qp.drawPolyline(QPolygonF(self.points))

    def clearPad(self):
        self.points.clear()
        self.update()
        pass



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = DrawPad()
    sys.exit(app.exec_())