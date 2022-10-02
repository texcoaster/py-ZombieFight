import pygame
import math
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

    if GameConfig.index == 1:
      if key[pygame.K_UP] or key[pygame.K_w]:
        self.y += int(GameConfig.player_speed * math.sin(math.radians(90)))
        if self.y >= 720:
          self.y = 0

      if key[pygame.K_DOWN] or key[pygame.K_s]:
        self.y += int(GameConfig.player_speed * math.sin(math.radians(270)))
        if self.y <= -720:
          self.y = 0

      if key[pygame.K_LEFT] or key[pygame.K_a]:
        self.x += int(GameConfig.player_speed * math.cos(math.radians(180)))
        if self.x >= 960:
          self.x = 0

      if key[pygame.K_RIGHT] or key[pygame.K_d]:
        self.x += int(GameConfig.player_speed * math.cos(math.radians(0)))
        if self.x <= -960:
          self.x = 0

  def draw(self, screen):
    if GameConfig.index == 0:
      screen.blit(self.backgound_image[GameConfig.level-1], [0, 0])
      DrawText.drawText(screen, 480, 650, "press space to start", (0, 0, 0), 35)
    if GameConfig.index == 1:
      for i in range(-960, 1920, 960):
        for j in range(-720, 1440, 720):
          screen.blit(self.backgound_image[GameConfig.level-1], [self.x+i, self.y+j])

    for child in self.children:
      child.draw(screen)
