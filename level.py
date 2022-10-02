from gameobject import *
from drawtext import *
from game_config import *

class Level(GameObject):
  def __init__(self):
    super().__init__(0, 0)
    self.press_spacekey = False
    self.level_name = [
      "OrdinaryPlace", "Desert"
    ]
  
  def keyInput(self, key):
    if GameConfig.index == 0:
      if key[pygame.K_LEFT] == True and GameConfig.level > 1:
        GameConfig.level -= 1
      if key[pygame.K_RIGHT] == True and GameConfig.level < GameConfig.MAXLEVEL:
        GameConfig.level += 1

      if key[pygame.K_SPACE] == True:
        self.press_spacekey = True
      if key[pygame.K_SPACE] == False and self.press_spacekey:
        self.press_spacekey = False
        GameConfig.index = 1
  
  def draw(self, screen):
    if GameConfig.index == 0:
      DrawText.drawText(screen, 480, 360, "Level "+str(GameConfig.level), (0, 0, 0), 100, True)
      DrawText.drawText(screen, 480, 450, self.level_name[GameConfig.level-1], (0, 0, 0), 80, True)
