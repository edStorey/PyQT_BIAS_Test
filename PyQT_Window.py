#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    """
    ##############################################################
    set which monito this window sticks to 
    set to full screen
    """
    display_monitor = 1
    monitor = QDesktopWidget().screenGeometry(display_monitor)
    w.move(monitor.left(), monitor.top())
    #w.showFullScreen()
    """##########################################################"""


        #w.resize(250, 150)
    #w.move(300, 300)
    w.setGeometry(300, 300, 300, 220)
    w.setWindowTitle('Icon')
    #w.setWindowTitle('Simple')
    w.setWindowIcon(QIcon('ash_zoom_2.PNG'))
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()