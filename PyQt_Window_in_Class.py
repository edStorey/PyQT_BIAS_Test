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
#from threading import Thread
from PyQt5.QtWidgets import ( QWidget, QGridLayout,
    QPushButton, QApplication, QMainWindow, QDesktopWidget, QLabel, QStackedLayout)
from PyQt5.QtGui import QMovie

import fans

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

from PyQt5.QtCore import QRect, QTimer, QUrl, Qt

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # string value
        title = "Main_Window"
  
        # set the title
        self.setWindowTitle(title)

        self.initUI()

    def initUI(self):

        


        self.main_widget  = 0
        #self.recording_screen = 0
        self.screen_saver_on = 0

        self.milli = 1000
        self.screen_wait_time = 20 * self.milli
        self.timer_wait_time = 45 * self.milli

        self.H_idle_animation, self.M_idle_animation = "Idle-Loop-LR-5s.gif", "reversed-Idle-Loop-LR-5s.gif"
    
        self.choose_window(0)

        self.setAttribute(Qt.WA_AcceptTouchEvents, True)
        self.installEventFilter(self)
        
        

        

        #### HAVE TO SET CENTRAL WIDGET FOR MAIN WINDOW
        self.layout_for_wids = QStackedLayout()
        self.central_wid = QWidget()
        self.ex2, self.ex4 = Example2(), Example2()

        self.ex2.setWindowTitle("Human_Voice")
        self.ex4.setWindowTitle("Synthetic_Voice")



        self.wid, self.wid2= QWidget(self), QWidget(self)
        self.wid3 = QVideoWidget()
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        grid1, grid2, grid3 = QGridLayout(), QGridLayout(), QGridLayout() 
        self.label, label2 = QLabel(self), QLabel(self)
        self.timer, self.screen_timer = QTimer(), QTimer()
        self.original, self.gif_screen = QMovie('I_cant_hear_you.gif'), QMovie('UVoB-vid-1024x600.gif')
        self.gif_screen2 = QMediaContent(QUrl.fromLocalFile('Segment-2011-05-01-HermeTest.wav'))
        Rect = QRect(0,0,int(self.width()),int(self.height()))

        
        for layout in [[self.wid, grid1], [self.wid2, grid2], [self.wid3, grid3]] :
            self.create_layouts(layout[0], layout[1], Rect)
            


        self.add_movie(self.label, grid2, self.original)
        #self.add_movie(label3, grid4, self.voice_gif)
        self.add_movie(label2, grid3, self.gif_screen)
        
        
        

        self.set_button_layout(grid1)

        
        self.screen_timer.timeout.connect(self.screen_saver_timeout)
        self.timer.timeout.connect(self.widget_hide)
        

        self.set_central_widget([self.wid3, self.wid, self.wid2], self.central_wid)
        

        self.ex2.image_display(self.H_idle_animation)
        #self.ex3.image_display('Waiting.jpg')
        self.ex4.image_display(self.M_idle_animation)
        
        self.setStyleSheet("background-color: white;")

        #self.mediaPlayer.setVideoOutput(self.wid3)
        

        



        self.wid.hide()
        self.wid2.hide()
        #self.wid4.hide()
        self.wid3.show()
        self.gif_screen.start()

        
        

        self.show()


    def image_display(self, image) :
    
        #self.label.clear()


        original = QMovie(image)
        self.label.setMovie(original)
        self.label.setScaledContents(True)
        
       
        self.label.resize(self.width() ,self.height())

        
        self.label.show()
        
        original.start()


    """"FUNCTIONAL FUNCTIONS"""

    def widget_hide(self, H_GIF = "Idle-Loop-LR-5s.gif", M_GIF = "Idle-Loop-LR-5s.gif", WAV = None, TS_GIF = 'I_cant_hear_you.gif') :
       
        if self.main_widget == 0 :
    
            self.screen_timer.stop()
            #self.voice_gif.stop()
            self.start_timer(self.timer, self.timer_wait_time)
            self.original.start()
            self.widget_swap(self.wid2, self.wid)
            self.ex1_change_image(self.ex2, H_GIF)
            #self.ex1_change_image(self.ex3, 'Mel_no_border.jpeg')
            self.ex1_change_image(self.ex4, M_GIF)
            self.image_display(TS_GIF)
            self.ex2.audio_play(WAV)
            self.main_widget = 1  

            """"CROMACS START FANS"""
            #start_1()


                  
            
        else :
            
            self.original.stop()
            self.start_timer(self.screen_timer, self.screen_wait_time)
            self.widget_swap(self.wid, self.wid2)
            self.ex1_change_image(self.ex2, self.H_idle_animation)
            #self.ex1_change_image(self.ex3, 'Waiting.jpg')
            self.ex1_change_image(self.ex4, self.M_idle_animation)
            self.ex2.audio_stop()
            self.main_widget = 0 

            """"CROMACS STOP FANS"""
            fans.stop_fans()
            

    def ex1_change_image(self, win, image) :
        win.image_display(image)


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



    """  OVERWRITING REAL FUNCTION """
    
    def mousePressEvent(self, QmouseEvent) :

        self.stopScreenTimer()


    def mouseReleaseEvent(self, QmouseEvent):

        self.startScreenTimer()



    def stopScreenTimer(self) :
        
        if self.main_widget == 0 :

            #self.start_timer(self.screen_timer, self.screen_wait_time)
            self.screen_timer.setSingleShot(False)
            self.screen_timer.stop()
            self.screen_saver_on = 0
            #self.start_timer(self.screen_timer, self.screen_wait_time)
            #self.screen_saver_timeout()
            self.widget_swap(self.wid, self.wid3)
            self.wid3.hide()


    def startScreenTimer(self) :
        
        if self.main_widget == 0 :
            
            self.screen_timer.stop()
            self.screen_saver_on = 0
            self.start_timer(self.screen_timer, self.screen_wait_time)
            self.screen_saver_timeout()
            self.wid3.hide()




    """"  INIT FUNCTIONS   """

    def choose_window(self,  window) :
        test = QDesktopWidget().screenCount()

        monitor = QDesktopWidget().screenGeometry(window)
        self.move(monitor.left(), monitor.top())
        self.resize(monitor.width(), monitor.height())

        self.showFullScreen()


    def create_layouts(self, widget, grid, rect) :
        ## set contents margin get rid of default margin on grids and sets to 0
        grid.setContentsMargins(0,0,0,0)
        widget.setLayout(grid)
        widget.setGeometry(rect)
        widget.showFullScreen()


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

        Utterances_List = [ "I can't hear you",
                            "Am I breathing?",
                            "The data is corrupted",
                            "I can detect fluctuations",
                            "What does it mean?",
                            "I sound strange",
                            "This is alien",
                            "Breathing, a tortuous task",
                            "Breathing, essential to life" ]

        ### CREATE WIDGET LAYOUT
        positions = [(i, j) for i in range(1,4) for j in range(1,4)]

        file_list = []
        
        self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9 = {
                    QPushButton(Utterances_List[0]), QPushButton(Utterances_List[1]), QPushButton(Utterances_List[2]), 
                    QPushButton(Utterances_List[3]), QPushButton(Utterances_List[4]), QPushButton(Utterances_List[5]),
                    QPushButton(Utterances_List[6]), QPushButton(Utterances_List[7]), QPushButton(Utterances_List[8])}


        #buttons = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        buttons = []

        for number in range(1, 10) :
            h_gif = "H_Utterances/HU" + str(number) + ".gif"
            m_gif = "M_Utterances/MU" + str(number) + ".gif"
            wav = "Wav_Files/WU" + str(number) + ".wav"
            i_gif = "Interface_Gifs/IU" + str(number) + ".gif"

            file_list.append([h_gif, m_gif, wav, i_gif])

        



        for position, name in zip( positions, Utterances_List):
            button = QPushButton(name)
            buttons.append(button)
            button.setMinimumSize(int(self.wid.width()/4),int(self.wid.height()/4))
            button.setStyleSheet("QPushButton { "
                                                    
                                                    "color: black ;"
                                                    #"border-color: rgb(214,163,84) ;"
                                                    "border-color: #09f8fb ;"
                                                    "border-color: black ;"
                                                    "border-style: outset;"
                                                    "border-radius: 40px;"
                                                    "background-color: green;"
                                                    #"background-color: rgb(224,204,151);" ### Beige
                                                    "background-color: rgb(255,255,255, 0);"
                                                    #"selection-color: red ;"
                                                    #"selection-background-color: teal;"
                                                    "border-width: 2px;"
                                                    #"border-color: green;"
                                                    "font: bold 33px;"
                                                    "padding: 6px; }"
                                                    "QPushButton::pressed { background-color: rgb(0,0,0, 25) }"
                                                    )
            if name == 'Z' :
                grid.addWidget(button, 6, 3)
            else :
                grid.addWidget(button, *position)


            
       # for button, number in zip(self.buttons, number_list) :
            

            
            button.pressed.connect(self.stopScreenTimer)
            button.released.connect(self.startScreenTimer)
            button.grabGesture(Qt.TapAndHoldGesture)
            #button.clicked.connect(self.ex1_change_image)

        buttons[0].clicked.connect(lambda : self.widget_hide(H_GIF = file_list[0][0], M_GIF = file_list[0][1], WAV = file_list[0][2], TS_GIF = file_list[0][3]))
        buttons[1].clicked.connect(lambda : self.widget_hide(H_GIF = file_list[1][0], M_GIF = file_list[1][1], WAV = file_list[1][2], TS_GIF = file_list[1][3]))
        buttons[2].clicked.connect(lambda : self.widget_hide(H_GIF = file_list[2][0], M_GIF = file_list[2][1], WAV = file_list[2][2], TS_GIF = file_list[2][3]))
        buttons[3].clicked.connect(lambda : self.widget_hide(H_GIF = file_list[3][0], M_GIF = file_list[3][1], WAV = file_list[3][2], TS_GIF = file_list[3][3]))
        buttons[4].clicked.connect(lambda : self.widget_hide(H_GIF = file_list[4][0], M_GIF = file_list[4][1], WAV = file_list[4][2], TS_GIF = file_list[4][3]))
        buttons[5].clicked.connect(lambda : self.widget_hide(H_GIF = file_list[5][0], M_GIF = file_list[5][1], WAV = file_list[5][2], TS_GIF = file_list[5][3]))
        buttons[6].clicked.connect(lambda : self.widget_hide(H_GIF = file_list[6][0], M_GIF = file_list[6][1], WAV = file_list[6][2], TS_GIF = file_list[6][3]))
        buttons[7].clicked.connect(lambda : self.widget_hide(H_GIF = file_list[7][0], M_GIF = file_list[7][1], WAV = file_list[7][2], TS_GIF = file_list[7][3]))
        buttons[8].clicked.connect(lambda : self.widget_hide(H_GIF = file_list[8][0], M_GIF = file_list[8][1], WAV = file_list[8][2], TS_GIF = file_list[8][3]))    


        buttons[0].clicked.connect(fans.start_1)
        buttons[1].clicked.connect(fans.start_2)
        buttons[2].clicked.connect(fans.start_3)
        buttons[3].clicked.connect(fans.start_4)
        buttons[4].clicked.connect(fans.start_5)
        buttons[5].clicked.connect(fans.start_6)
        buttons[6].clicked.connect(fans.start_7)
        buttons[7].clicked.connect(fans.start_8)
        buttons[8].clicked.connect(fans.start_9)


    def set_central_widget(self, Widgets, central_widget) :
        for widget in Widgets :
            self.layout_for_wids.addWidget(widget)      
        
        central_widget.setLayout(self.layout_for_wids)
        self.setCentralWidget(central_widget)



class Example2(QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        #self.gif_screen2 = QMediaContent(QUrl.fromLocalFile('Segment-2011-05-01-HermeTest.wav'))
        
        #self.setGeometry(300, 300, 300, 200)
        self.choose_window(1)
        self.show()


    def choose_window(self,  window) :
        monitor = QDesktopWidget().screenGeometry(window)
        self.move(monitor.left(), monitor.top())
        width = 1280*2
        Height = 800
   
        # setting  the fixed width of window
        self.setFixedWidth(width)
        self.setFixedHeight(Height)
        

        self.setWindowFlags(Qt.FramelessWindowHint)
        #self.showFullScreen()


    def image_display(self, image) :

        self.label.clear()


        original = QMovie(image)
        self.label.setMovie(original)
        self.label.setScaledContents(True)
        
       
        self.label.resize(self.width() ,self.height())

        
        self.label.show()
        
        original.start()

    def audio_play(self, audio) :
        #self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(None)))
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(audio)))
        self.mediaPlayer.play()

    def audio_stop(self) :
        self.mediaPlayer.stop()
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(None)))

        

    def display_window(self) :
        self.show()



def main():
    spectrogram = 'Mel_no_border.jpeg'

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()