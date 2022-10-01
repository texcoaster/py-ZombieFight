import pygame
from gameobject import *

class Enemy(GameObject):
  def __init__(self):
    super().__init__(0, 0)

  def draw(self, screen):
    ...
