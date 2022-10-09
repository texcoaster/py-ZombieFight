import pygame
import math
from gameobject import *
from game_config import *
from level import *
from score import *
from text_utils import *

class BackGround(GameObject):
  def __init__(self):
    super().__init__(0, 0)
    self.children.append(Level())
    self.children.append(Score())

    self.backgound_image = []
    for i in range(GameConfig.MAXLEVEL):
      self.backgound_image.append(pygame.image.load("_images/background/bg_img_"+str(i+1)+".png"))
  
  def keyInput(self, key):
    self.children[0].keyInput(key)

  def draw(self, screen):
    if GameConfig.index == 0:
      screen.blit(self.backgound_image[GameConfig.level-1], [0, 0])
      TextUtils.drawText(screen, 480, 650, "press space to start", (0, 0, 0), 35)
    if GameConfig.index == 1:
      for i in range(-960, 1920, 960):
        for j in range(-720, 1440, 720):
          screen.blit(self.backgound_image[GameConfig.level-1], [self.x+i, self.y+j])

    for child in self.children:
      child.draw(screen)
  
  def goUp(self):
    self.y += int(GameConfig.player_speed * math.sin(math.radians(90)))
    if self.y >= 720:
      self.y = 0
  def goDown(self):
    self.y += int(GameConfig.player_speed * math.sin(math.radians(270)))
    if self.y <= -720:
      self.y = 0
  def goLeft(self):
    self.x += int(GameConfig.player_speed * math.cos(math.radians(0)))
    if self.x >= 960:
      self.x = 0
  def goRight(self):
    self.x += int(GameConfig.player_speed * math.cos(math.radians(180)))
    if self.x <= -960:
      self.x = 0
