
# -*- coding: utf-8 -*-
__author__ = 'Douglas Uba'

from entities import Particle
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import QWidget

class ParticlesWidget(QWidget):
    def __init__(self, size=8, speed=2, color=QColor(220, 220, 220, 255), shadowEffect=32):
        super(ParticlesWidget, self).__init__()
        
        self.setWindowTitle('Particles')
        
        # Particle attributes
        self.particleSize = size
        self.particleSpeed = speed
        self.particleColor = color
        
        # The set of particles
        self.particles = []
        
        # The drawing area
        self.pixmap = QPixmap(512, 512)
        self.pixmap.fill(Qt.transparent)
        
        # Set 255 to turn off
        self.shadowEffect = shadowEffect
        self.backgroundColor = QColor(0, 0, 0, self.shadowEffect)
        
        # Animation loop
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.__updateParticles)
        self.timer.start(1000 / 60)
        
        # Setup widget
        self.resize(self.pixmap.size())
        self.setMouseTracking(True)
        self.setCursor(Qt.BlankCursor)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)
        
    def mouseMoveEvent(self, event):
        pos = event.pos()
        self.__emitParticles(pos.x(), pos.y(), self.particleSize, self.particleSpeed, QColor(self.particleColor), 1)
        
    def resizeEvent(self, event):
        self.pixmap = QPixmap(event.size())
        
    def __emitParticles(self, x, y, size, speed, color, n):
        for i in range(n):
            self.particles.append(Particle(x, y, size, speed, color))
            
    def __updateParticles(self):
        # Update each particle
        for particle in self.particles:
            particle.update()
            if particle.isDead():
                self.particles.remove(particle)
        
        # Clear
        painter = QPainter(self.pixmap)
        painter.fillRect(0, 0, self.pixmap.width(), self.pixmap.height(), self.backgroundColor)
        
        # Render particles
        for particle in self.particles:
            particle.render(painter)
        
        # Update widget content
        self.update()
        