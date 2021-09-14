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
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication, QMainWindow, QDesktopWidget, QLabel, QStackedLayout)
from PyQt5.QtGui import QPixmap, QMovie

from PyQt5.QtCore import QRect, QTimer

from Microphone_Record import Microphone_Record

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        self.main_widget  = 0
        self.recording_screen = 0
        self.screen_saver_on = 0

        milli = 1000
        self.screen_wait_time = 5 * milli
        self.timer_wait_time = 20 * milli
    
        self.choose_window(0)

        #### HAVE TO SET CENTRAL WIDGET FOR MAIN WINDOW
        self.layout_for_wids = QStackedLayout()
        self.central_wid = QWidget()

        self.wid, self.wid2, self.wid3 = QWidget(self), QWidget(self), QWidget(self)
        grid1, grid2, grid3 = QGridLayout(), QGridLayout(), QGridLayout()  
        label, label2 = QLabel(self), QLabel(self)
        self.timer, self.screen_timer = QTimer(), QTimer()
        self.original, self.gif_screen = QMovie('timer.gif'), QMovie('download-percentage.gif')
        Rect = QRect(0,0,int(self.width()),int(self.height()))

        for layout in [[self.wid, grid1], [self.wid2, grid2], [self.wid3, grid3]] :
            self.create_layouts(layout[0], layout[1], Rect)


        self.add_movie(label, grid2, self.original)
        self.add_movie(label2, grid3, self.gif_screen)

        self.set_button_layout(grid1)

        
        self.screen_timer.timeout.connect(self.screen_saver_timeout)
        self.timer.timeout.connect(self.widget_hide)
        

        self.set_central_widget([self.wid3, self.wid, self.wid2], self.central_wid)

        self.wid.hide()
        self.wid2.hide()
        self.wid3.show()
        self.gif_screen.start()
        

        self.show()




    """"FUNCTIONAL FUNCTIONS"""

    def widget_hide(self) :
        if self.main_widget == 0 :

            self.screen_timer.stop()
            self.start_timer(self.timer, self.timer_wait_time)
            self.original.start()
            self.widget_swap(self.wid2, self.wid)
            self.recording_screen = 1
            self.main_widget = 1         
            
        else :

            self.original.stop()
            self.start_timer(self.screen_timer, self.screen_wait_time)
            self.widget_swap(self.wid, self.wid2)
            self.recording_screen = 0
            self.main_widget = 0 


    ####  OVERWRITING REAL FUNCTION
    def mousePressEvent(self, QmouseEvent) :
        
        if self.recording_screen == 0 :
            
            self.screen_timer.stop()
            self.screen_saver_on = 0
            self.start_timer(self.screen_timer, self.screen_wait_time)
            self.screen_saver_timeout()
            self.wid3.hide()
    
    def screen_saver_timeout(self) :
        x = 0
        if self.screen_saver_on == 1 :
            self.screen_saver_on = 0
            self.widget_swap(self.wid3, self.wid)
            self.gif_screen.start()
        else :
            self.screen_saver_on = 1
            self.gif_screen.stop()
            self.widget_swap(self.wid, self.wid3)


    def start_timer(self, timer, time) :
        timer.setSingleShot(True)
        timer.start(time)

    def widget_swap(self, show, hide) :
        show.show()
        hide.hide()



    """"  INIT FUNCTIONS   """

    def choose_window(self,  window) :
        monitor = QDesktopWidget().screenGeometry(window)
        self.move(monitor.left(), monitor.top())

        self.showFullScreen()


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



    def set_central_widget(self, Widgets, central_widget) :
        for widget in Widgets :
            self.layout_for_wids.addWidget(widget)      
        
        central_widget.setLayout(self.layout_for_wids)
        self.setCentralWidget(central_widget)



class Example2(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 300, 200)
        self.choose_window(1)
        self.show()


    def choose_window(self,  window) :
        monitor = QDesktopWidget().screenGeometry(window)
        self.move(monitor.left(), monitor.top())
        self.showFullScreen()


    def image_display(self, image) :

        label = QLabel(self)
        orignal = QPixmap(image)
        Rect = QRect(0,0,int(orignal.width()/2),orignal.height())
        cropped = QPixmap(orignal.copy(Rect))
        label.setPixmap(cropped.scaledToWidth(self.width()))
        label.setScaledContents(True)
        
        label.move(0, 0)
        label.show()
        label.resize(self.width() ,self.height())



class Example3(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 200)
        
        self.choose_window(2)
        
        self.show()

    def image_display(self, image) :

        label = QLabel(self)
        orignal = QPixmap(image)
        Rect = QRect(int(orignal.width()/2)+1,0,int(orignal.width()/2),orignal.height())
        cropped = QPixmap(orignal.copy(Rect))
        label.setPixmap(cropped.scaledToWidth(self.width()))
        label.setScaledContents(True)

        label.move(0, 0)
        label.show()
        label.resize(self.width(),self.height())

    def choose_window(self,  window) :
        monitor = QDesktopWidget().screenGeometry(window)
        self.move(monitor.left(), monitor.top())
        self.showFullScreen()




def main():
    spectrogram = 'Mel_no_border.jpeg'

    app = QApplication(sys.argv)
    ex = Example()
    ex2 = Example2()
    ex3 = Example3()
    Mic = Microphone_Record()

    

    ex2.image_display(spectrogram)
    ex3.image_display(spectrogram)
    Mic.record()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()