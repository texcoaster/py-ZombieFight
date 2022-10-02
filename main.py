import pygame
import sys

from gameobject import *
from background import *
from enemy import *
from player import *
from game_config import *


tmr = 0

def main():
  global tmr

  pygame.init()
  pygame.display.set_caption("ZOMBIEFIGHT")
  screen = pygame.display.set_mode((960, 720))
  clock = pygame.time.Clock()

  GameConfig.index = 0
  GameConfig.level = 1
  GameConfig.MAXLEVEL = 2

  root = GameObject(0, 0)
  GameObject.root = root

  background = BackGround()
  enemy = Enemy()
  player = Player()

  root.children.append(background)
  root.children.append(enemy)
  root.children.append(player)


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
    
    key = pygame.key.get_pressed()
    root.keyInput(key)
    root.draw(screen)


    pygame.display.update()
    clock.tick(30)


if __name__ == '__main__':
  main()
