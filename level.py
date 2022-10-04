from gameobject import *
from text_utils import *
from game_config import *

class Level(GameObject):
  def __init__(self):
    super().__init__(0, 0)
    self.press_spacekey = False
    self.press_leftkey = False
    self.press_rightkey = False
    self.level_name = [
      "OrdinaryPlace", "Desert"
    ]

    self.arrow_image = pygame.image.load("_images/background/arrow.png")
    self.left_arrow_image = pygame.transform.rotozoom(self.arrow_image, 90, 0.35)
    self.right_arrow_image = pygame.transform.rotozoom(self.arrow_image, -90, 0.35)

    self.tmr1 = 0
    self.tmr2 = 0
    self.isBig1 = False
    self.isBig2 = False
  
  def keyInput(self, key):
    if GameConfig.index == 0:
      if key[pygame.K_LEFT] == True and GameConfig.level > 1:
        self.press_leftkey = True
      if key[pygame.K_LEFT] == False and self.press_leftkey:
        self.press_leftkey = False
        self.bigAndSmall(1)
        GameConfig.level -= 1

      if key[pygame.K_RIGHT] == True and GameConfig.level < GameConfig.MAXLEVEL:
        GameConfig.level += 1
        self.right_arrow_image = pygame.transform.rotozoom(self.arrow_image, -90, 0.45)
        self.changed2 = False
      if key[pygame.K_RIGHT] == False and self.changed2 == False:
        self.right_arrow_image = pygame.transform.rotozoom(self.arrow_image, -90, 0.35)
        self.changed2 = True

      if key[pygame.K_SPACE] == True:
        self.press_spacekey = True
      if key[pygame.K_SPACE] == False and self.press_spacekey:
        self.press_spacekey = False
        GameConfig.index = 1
  
  def draw(self, screen):
    if GameConfig.index == 0:
      TextUtils.drawText(screen, 480, 360, "Level "+str(GameConfig.level), (0, 0, 0), 100, True)
      TextUtils.drawText(screen, 480, 450, self.level_name[GameConfig.level-1], (0, 0, 0), 80, True)

      screen.blit(self.left_arrow_image, [300-self.left_arrow_image.get_width()/2, 360-self.left_arrow_image.get_height()/2])
      screen.blit(self.right_arrow_image, [660-self.right_arrow_image.get_width()/2, 360-self.right_arrow_image.get_height()/2])
      self.tmr1 += 1
      self.tmr2 += 1
  
  def bigAndSmall(self, num):
    if num == 1:
      self.tmr1 = 0
      self.left_arrow_image = pygame.transform.rotozoom(self.arrow_image, 90, 0.45)
