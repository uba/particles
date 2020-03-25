# -*- coding: utf-8 -*-
__author__ = 'Douglas Uba'

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor
from random import random

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dead = False
    
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
        
    def isDead(self):
        return self.dead
        
    def update(self):
        pass
        
    def render(self, painter):
        pass
     
class Particle(Entity):
    def __init__(self, x, y, size, speed, color):
        super(Particle, self).__init__(x, y)
        self.size = size
        self.speedX = -speed + (random() * speed * 2)
        self.speedY = -speed + (random() * speed * 2)
        self.isFading = False
        self.color = color
        
    def update(self):
        # Update position
        self.x += self.speedX
        self.y -= self.speedY
        
        # Update speed
        self.speedX *= 0.98
        self.speedY *= 0.98
        
        # Update color and lifetime
        if self.isFading: 
            self.color.setAlpha(self.color.alpha() * 0.92)
        elif random() > 0.97:
            self.isFading = True
            
        if self.color.alpha() < 10:
            self.dead = True
        
    def render(self, painter):
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.color)
        center = QPoint(self.x, self.y)
        painter.drawEllipse(center, self.size, self.size)
