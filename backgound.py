import pygame
from gameobject import *

class BackGround(GameObject):
  def __init__(self):
    super().__init__(0, 0)
    self.index = 0
  
  def draw(self, screen):
    screen.fill((0, 0, 30))
    pygame.draw.rect(screen, (0, 60, 0), [0, 500, 960, 220])

    self.drawText(screen, 50, 0, "Score:", (255, 255, 255), 65)
    self.drawText(screen, 550, 0, "HighScore:", (255, 255, 255), 65)

  def drawText(self, screen, x, y, text, color, size):
    fnt = pygame.font.Font(None, size)
    sur = fnt.render(text, True, color)
    screen.blit(sur, [x, y])

  def setIndex(self, index):
    self.index = index
