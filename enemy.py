import pygame
import math
from gameobject import *
from game_config import *

class Enemy(GameObject):
  def __init__(self, x, y, imgFile, speed, attack, shield):
    super().__init__(x, y)
    self.img = pygame.image.load(imgFile)
    self.speed = speed
    self.attack = attack
    self.shield = shield

  def draw(self, screen):
    screen.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])
    if self.x < 480:
      self.x += self.speed * math.cos(math.radians(0))
    elif self.x > 480:
      self.x += self.speed * math.cos(math.radians(180))
    if self.y < 360:
      self.y += self.speed * math.sin(math.radians(90))
    elif self.y > 360:
      self.y += self.speed * math.sin(math.radians(270))
  
  def goUp(self):
    self.y += GameConfig.player_speed
  def goDown(self):
    self.y -= GameConfig.player_speed
  def goLeft(self):
    self.x += GameConfig.player_speed
  def goRight(self):
    self.x -= GameConfig.player_speed
