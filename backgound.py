import pygame
from gameobject import *

class BackGround(GameObject):
  def __init__(self):
    super().__init__(0, 0)
    self.index = 0
  
  def draw(self, screen):
    screen.fill((0, 0, 30))
    pygame.draw.rect(screen, (0, 60, 0), [0, 500, 960, 220])

  def setIndex(self, index):
    self.index = index
