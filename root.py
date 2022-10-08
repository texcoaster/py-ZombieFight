import pygame
from gameobject import *
from game_config import *

class Root(GameObject):
  root = None

  def __init__(self):
    super().__init__(0, 0)
    self.directions = ""
  
  def keyInput(self, key):
    self.children[0].keyInput(key)

    self.directions = []
    if GameConfig.index == 1:
      if key[pygame.K_UP] or key[pygame.K_w]:
        self.directions.append("UP")
      if key[pygame.K_DOWN] or key[pygame.K_s]:
        self.directions.append("DOWN")
      if key[pygame.K_LEFT] or key[pygame.K_a]:
        self.directions.append("LEFT")
      if key[pygame.K_RIGHT] or key[pygame.K_d]:
        self.directions.append("RIGHT")
  
  def draw(self, screen):
    self.children[0].draw(screen)

    for child in self.children[0].children:
      for i in range(len(self.directions)):
        self.callFunction(child, i)

  def callFunction(self, child, i):
    if self.directions[i] == "UP":
      child.goUp()
    if self.directions[i] == "DOWN":
      child.goDown()
    if self.directions[i] == "LEFT":
      child.goLeft()
    if self.directions[i] == "RIGHT":
      child.goRight()
