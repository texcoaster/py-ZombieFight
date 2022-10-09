import pygame
from gameobject import *
from game_config import *

class Player(GameObject):
  def __init__(self):
    super().__init__(480, 360)
    self.img = pygame.image.load("_images/player.png")
  
  def draw(self, screen):
    if GameConfig.index == 1:
      screen.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])
