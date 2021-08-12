#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

This example shows a tooltip on
a window and a button.

Author: Jan Bodnar
Website: zetcode.com
"""


"""
THUS FILE MAKES A WINDOW FULLSCREEN ON YOUR FIRST MONITOR AND THEN CREATES A BUTTON THAT OPENS IN ANOTHER WINDOW

"""

import sys, string
from PyQt5.QtWidgets import (QWidget, QToolTip, QGridLayout,
    QPushButton, QApplication, QMainWindow, QDesktopWidget, QLabel, QStackedLayout)
from PyQt5.QtGui import QFont, QPixmap, QMovie

from PyQt5.QtCore import QRect, QSize, QTimer

import time

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()




    def initUI(self):


        self.display_monitor = 0

        self.recording_screen = 0
    
        monitor = QDesktopWidget().screenGeometry(self.display_monitor)
        self.move(monitor.left(), monitor.top())

        self.showFullScreen()
        self.main_widget = 0


        #### HAVE TO SET CENTRAL WIDGET FOR MAIN WINDOW
        self.layout_for_wids = QStackedLayout()
        self.central_wid = QWidget()

        self.wid, self.wid2, self.wid3 = QWidget(self), QWidget(self), QWidget(self)
        grid1, grid2, grid3 = QGridLayout(), QGridLayout(), QGridLayout()  
        Rect = QRect(0,0,int(self.width()),int(self.height()))




        self.create_layouts(self.wid, grid1, Rect)
        self.create_layouts(self.wid2, grid2, Rect)
        self.create_layouts(self.wid3, grid3, Rect)



        label, label2 = QLabel(self), QLabel(self)
        self.original, self.gif_screen = QMovie('timer.gif'), QMovie('download-percentage.gif')
 
        self.add_movie(label, grid2, self.original)
        self.add_movie(label2, grid3, self.gif_screen)

        self.set_button_layout(grid1)

        





        self.screen_saver_on = 0
        self.screen_timer = QTimer()
        self.screen_timer.timeout.connect(self.screen_saver_timeout)
       

        
        
        self.layout_for_wids.addWidget(self.wid3)
        self.layout_for_wids.addWidget(self.wid)
        self.layout_for_wids.addWidget(self.wid2)
        
        
        
        self.central_wid.setLayout(self.layout_for_wids)
        self.setCentralWidget(self.central_wid)

        self.wid.hide()
        self.wid2.hide()
        self.wid3.show()
        self.gif_screen.start()
        

        self.show()


    def create_layouts(self, widget, grid, rect) :
        widget.setLayout(grid)
        widget.setGeometry(rect)


    def add_movie(self, label, grid, movie) :
        label.setMovie(movie)
        label.setScaledContents(True)
        grid.addWidget(label)


    def set_button_layout(self, grid) :

        grid.setVerticalSpacing(30)
        grid.setHorizontalSpacing(70)
        grid.setRowStretch(0,1)
        grid.setRowStretch(7,1)
        grid.setColumnStretch(0,1)
        grid.setColumnStretch(7,1)

        ## CREATE UPPERCASE LIST OF LETTERS
        alphabet_string = string.ascii_uppercase
        names = list(alphabet_string)

        ### CREATE WIDGET LAYOUT
        positions = [(i, j) for i in range(1,7) for j in range(1,6)]

        for position, name in zip(positions, names):
         button = QPushButton(name)
         button.setMinimumSize(int(self.wid.width()/7),int(self.wid.height()/8))
         button.setStyleSheet("QPushButton { color: red ;"
                              "border-style: outset;"
                              "border-radius: 40px;"
                              "background-color: yellow;"
                              "selection-color: red ;"
                              "selection-background-color: blue;"
                              "border-width: 2px;"
                              "border-color: green;"
                              "font: bold 14px;"
                              "padding: 6px; }"
                              "QPushButton::hover { background-color: green }"
                              "QPushButton::pressed { background-color: blue }"
                              )

         button.clicked.connect(self.widget_hide)

         if name == 'Z' :
            grid.addWidget(button, 6, 3)
         else :
            grid.addWidget(button, *position)



    def widget_hide(self) :
        if self.main_widget == 0 :
            
            self.wid.hide()
            self.wid2.show()
            self.main_widget = 1
            self.timer = QTimer()
            self.timer.timeout.connect(self.widget_hide)
            self.timer.setSingleShot(True)
            self.timer.start(20000)
            self.screen_timer.stop()
            self.recording_screen = 1
            self.original.start()
            
            
            
        else :
            
            self.wid2.hide()
            self.wid.show()
            self.original.stop()
            self.screen_timer.setSingleShot(True)
            self.screen_timer.start(5000)
            self.recording_screen = 0
            
            self.main_widget = 0 

    ####  OVERWRITING REAL FUNCTION
    def mousePressEvent(self, QmouseEvent) :
        
        if self.recording_screen == 0 :
            self.wid3.hide()
            #
            #self.wid.show()
            self.screen_timer.stop()
            
            self.screen_saver_on = 0
            self.screen_timer.setSingleShot(True)
            self.screen_timer.start(5000)
        
            self.screen_saver_timeout()
        
    def screen_saver_timeout(self) :
        x = 0
        if self.screen_saver_on == 1 :
            self.screen_saver_on = 0
            self.wid.hide()
            self.wid3.show()
            self.gif_screen.start()
        else :
            #self.screen_timer.stop()
            self.screen_saver_on = 1
            self.gif_screen.stop()
            self.wid3.hide()
            self.wid.show()

            
            



        
            


    def window2(self):                                             # <===
        self.w = Example2()
        
        monitor = QDesktopWidget().screenGeometry(self.display_monitor)
        self.w.move(monitor.left(), monitor.top())
        self.w.showFullScreen()
        self.w.show()

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>SCREEN 1</b> widget')

        btn = QPushButton('SCREEN 1', self)
        #new_window = Example2()
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.setToolTip('This is a <b>SCREEN 1</b> widget')
        self.hide()


class Example2(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window22222")
        self.setGeometry(300, 300, 300, 200)
        monitor = QDesktopWidget().screenGeometry(1)
        self.move(monitor.left(), monitor.top())
        QToolTip.setFont(QFont('SansSerif', 10))
        self.showFullScreen()

        self.setToolTip('This is a <b>SCREEN 2</b> widget')

        btn = QPushButton('SCREEN 2', self)
        #new_window = Example2()
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.setToolTip('This is a <b>SCREEN 2</b> widget')
        

        """self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QLabel(self.centralwidget)

        self.photo.setGeometry(QRect(0, 0, 841, 511))
        self.photo.resize(self.photo.sizeHint())
        self.photo.setText("")

        self.photo.setPixmap(QPixmap("ash_zoom_2.PNG"))

        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.photo.move(100, 100)

        self.photo.show()"""

    def image_display(self, image) :

        #Rect = QRect(10,)
        #Rect.setRect(10,10,100,100)
        label = QLabel(self)
        #.setRect(10,10, 100, 100)
        #label.setRect(10,10, 100, 100)
        orignal = QPixmap(image)
        Rect = QRect(0,0,int(orignal.width()/2),orignal.height())
        cropped = QPixmap(orignal.copy(Rect))
        label.setPixmap(cropped.scaledToWidth(self.width()))
        label.setScaledContents(True)
        #label.setPixmap(cropped.scaledToHeight(self.height()))
        
        
        
        label.move(0, 0)
        label.show()
        label.resize(self.width() ,self.height())
        #label.resize(pixmap.width(),pixmap.height())


        #self.setCentralWidget(self.centralWidget)
        
        #self.show()


class Example3(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window22222")
        self.setGeometry(300, 300, 300, 200)
        monitor = QDesktopWidget().screenGeometry(2)
        self.move(monitor.left(), monitor.top())


        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>SCREEN 3</b> widget')

        btn = QPushButton('SCREEN 3', self)
        #new_window = Example2()
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.setToolTip('This is a <b>SCREEN 3</b> widget')
        
        self.showFullScreen()
        self.show()

    def image_display(self, image) :

        #Rect = QRect(10,)
        #Rect.setRect(10,10,100,100)
        label = QLabel(self)
        #.setRect(10,10, 100, 100)
        #label.setRect(10,10, 100, 100)
        orignal = QPixmap(image)
        Rect = QRect(int(orignal.width()/2)+1,0,int(orignal.width()/2),orignal.height())
        cropped = QPixmap(orignal.copy(Rect))
        label.setPixmap(cropped.scaledToWidth(self.width()))
        label.setScaledContents(True)
        #label.setPixmap(cropped.scaledToHeight(self.height()))
        
        
        
        label.move(0, 0)
        label.show()
        label.resize(self.width(),self.height())


def main():

    app = QApplication(sys.argv)
    ex = Example()
    #ex.mousePressEvent = ex.screen_saver_timer()
    ex2 = Example2()
    ex2.image_display('Mel_no_border.jpeg')
    ex3 = Example3()
    ex3.image_display('Mel_no_border.jpeg')
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()