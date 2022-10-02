from gameobject import *
from drawtext import *

class Level(GameObject):
  def __init__(self):
    super().__init__(0, 0)
    self.level = 0
    self.level_name = [
      "OrdinaryPlace"
    ]
  
  def draw(self, screen):
    DrawText.drawText(screen, 480, 360, "Level "+str(self.level), (0, 0, 0), 100, True)
    DrawText.drawText(screen, 480, 450, self.level_name[self.level-1], (0, 0, 0), 80, True)

  def setLevel(self, level):
    self.level = level
