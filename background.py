import pygame
from gameobject import *
from game_config import *
from level import *
from score import *
from drawtext import *

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
      DrawText.drawText(screen, 480, 650, "press space to start", (0, 0, 0), 35)
    if GameConfig.index == 1:
      screen.blit(self.backgound_image[GameConfig.level-1], [0, 0])

    for child in self.children:
      child.draw(screen)
