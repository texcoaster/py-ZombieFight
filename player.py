import pygame
from gameobject import *

class Player(GameObject):
  def __init__(self):
    self.x = 480
    self.y = 360
  
  def keyInput(self, key):
    ...
  
  def draw(self, screen):
    ...
