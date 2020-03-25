# -*- coding: utf-8 -*-
__author__ = 'Douglas Uba'

from widgets import ParticlesWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QColor
import sys

app = QApplication(sys.argv)
w = ParticlesWidget(size=8, speed=4, color=QColor(220, 220, 220, 255), shadowEffect=32)
w.show()
sys.exit(app.exec_())
