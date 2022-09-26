import pygame
from gameobject import *

class Inventory(GameObject):
  def __init__(self):
    super().__init__(0, 0)

  def draw(self, screen):
    for i in range(0, 490, 70):
      pygame.draw.rect(screen, (0, 0, 0), [i, 650, i+70, 720])
