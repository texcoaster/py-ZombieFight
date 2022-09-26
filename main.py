import pygame
import sys

from gameobject import *
from backgound import *
from cannon import *
from enemy import *
from shop import *
from menu import *
from inventory import *


tmr = 0
index = 0

def main():
  global tmr, index

  pygame.init()
  pygame.display.set_caption("ZOMBIEFIGHT")
  screen = pygame.display.set_mode((960, 720))
  clock = pygame.time.Clock()

  root = GameObject(0, 0)
  GameObject.root = root

  background = BackGround()
  cannon = Cannon()
  enemy = Enemy()
  shop = Shop()
  inventory = Inventory()
  menu = Menu()

  root.children.append(background)
  root.children.append(cannon)
  root.children.append(enemy)
  root.children.append(shop)
  root.children.append(menu)
  root.children.append(inventory)


  while True:
    tmr = tmr + 1
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
          screen = pygame.display.set_mode((670, 925), pygame.FULLSCREEN)
        if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
          screen = pygame.display.set_mode((670, 925))

    background.setIndex(index)
    
    root.draw(screen)


    pygame.display.update()
    clock.tick(30)


if __name__ == '__main__':
  main()
