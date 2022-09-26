import pygame
from gameobject import *

class Shop(GameObject):
  def __init__(self):
    super().__init__(0, 0)
    # self.width = 200
    # self.height = 65

    # self.press = False

  def draw(self, screen):
    pass
  #   pygame.draw.rect(screen, (0, 150, 0), [self.x, self.y, self.x+self.width, self.y+self.height])

  #   mouse = pygame.mouse.get_pos()
  #   click = pygame.mouse.get_pressed(5)
  #   if self.x <= mouse[0] <= self.x+self.width and self.y <= mouse[1] <= self.y+self.height:
  #     pygame.draw.rect(screen, (0, 200, 0), [self.x, self.y, self.x+self.width, self.y+self.height])
  #     if click[0] == 1 and self.press == False:
  #       self.press = True
  #       self.show()
  #     if click[0] == 0:
  #       self.press = False

  #   fnt = pygame.font.Font(None, 100)
  #   sur = fnt.render("SHOP", True, (0, 0, 0))
  #   screen.blit(sur, [self.x, self.y])
  
  # def show(self):
  #   print("SHOP")
