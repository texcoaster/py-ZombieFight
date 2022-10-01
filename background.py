import pygame
from gameobject import *
from game_config import *

class BackGround(GameObject):
  def __init__(self):
    super().__init__(0, 0)
    self.index = 0
    self.level = 0

    self.backgound_image = []
    for i in range(GameConfig.MAXLEVEL):
      self.backgound_image.append(pygame.image.load("_images/background/bg_img_"+str(i+1)+".png"))

    self.level_name = [
      "OrdinaryPlace"
    ]
  
  def draw(self, screen):
    screen.blit(self.backgound_image[self.level-1], [0, 0])

    self.drawText(screen, 150, 25, "Score:", (255, 255, 255), 65)
    self.drawText(screen, 700, 25, "HighScore:", (255, 255, 255), 65)

    if self.index == 0:
      self.drawText(screen, 480, 360, "Level "+str(self.level), (0, 0, 0), 100, True)
      self.drawText(screen, 480, 450, self.level_name[self.level-1], (0, 0, 0), 80, True)
    if self.index == 1:
      ...

  def drawText(self, screen, x, y, text, color, size, pretty=False):
    if pretty == False:
      fnt = pygame.font.Font(None, size)
      sur = fnt.render(text, True, color)
      screen.blit(sur, [x-sur.get_width()/2, y-sur.get_height()/2])

    if pretty == True:
      fnt = pygame.font.Font(None, size)
      cr = int(color[0] / 2)
      cg = int(color[1] / 2)
      cb = int(color[2] / 2)

      sur = fnt.render(text, True, (cr, cg, cb))
      x = x - sur.get_width() / 2
      y = y - sur.get_height() / 2
      screen.blit(sur, [x + 1, y + 1])

      cr = color[0] + 128
      if cr > 255: cr = 255
      cg = color[1] + 128
      if cg > 255: cg = 255
      cb = color[2] + 128
      if cb > 255: cb = 255

      sur = fnt.render(text, True, (cr, cg, cb))
      screen.blit(sur, [x - 1, y - 1])
      sur = fnt.render(text, True, color)
      screen.blit(sur, [x, y])

  def setIndex(self, index):
    self.index = index
  def setLevel(self, level):
    self.level = level
