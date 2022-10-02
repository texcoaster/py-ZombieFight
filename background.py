import pygame
from gameobject import *
from game_config import *
from level import *
from score import *
from drawtext import *

class BackGround(GameObject):
  def __init__(self):
    super().__init__(0, 0)
    self.index = 0
    self.level = 0

    self.press_spacekey = False

    self.children.append(Level())
    self.children.append(Score())

    self.backgound_image = []
    for i in range(GameConfig.MAXLEVEL):
      self.backgound_image.append(pygame.image.load("_images/background/bg_img_"+str(i+1)+".png"))
  
  def draw(self, screen):
    self.children[0].setLevel(self.level)

    if self.index == 0:
      screen.blit(self.backgound_image[self.level-1], [0, 0])
      self.children[0].draw(screen)
      DrawText.drawText(screen, 480, 650, "press space to start", (0, 0, 0), 35)

    if self.index == 1:
      screen.blit(self.backgound_image[self.level-1], [0, 0])

    self.children[1].draw(screen)

  def setIndex(self, index):
    self.index = index
  def setLevel(self, level):
    self.level = level
