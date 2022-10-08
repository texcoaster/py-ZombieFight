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
      if key[pygame.K_LEFT] == True:
        self.press_leftkey = True
      if key[pygame.K_LEFT] == False and self.press_leftkey:
        self.press_leftkey = False
        self.bigAndSmall("Left")
        if GameConfig.level > 1:
          GameConfig.level -= 1

      if key[pygame.K_RIGHT] == True:
        self.press_rightkey = True
      if key[pygame.K_RIGHT] == False and self.press_rightkey:
        self.press_rightkey = False
        self.bigAndSmall("Right")
        if GameConfig.level < GameConfig.MAXLEVEL:
          GameConfig.level += 1

      if key[pygame.K_SPACE] == True:
        self.press_spacekey = True
      if key[pygame.K_SPACE] == False and self.press_spacekey:
        self.press_spacekey = False
        GameConfig.index = 1
  
  def draw(self, screen):
    if GameConfig.index == 0:
      TextUtils.drawText(screen, 480, 360, "Level "+str(GameConfig.level), (0, 0, 0), 100, True)
      TextUtils.drawText(screen, 480, 450, self.level_name[GameConfig.level-1], (0, 0, 0), 80, True)

      screen.blit(self.left_arrow_image, [300 - self.left_arrow_image.get_width() / 2, 360 - self.left_arrow_image.get_height() / 2])
      screen.blit(self.right_arrow_image, [660 - self.right_arrow_image.get_width() / 2, 360 - self.right_arrow_image.get_height() / 2])

      if self.isBig1:
        self.tmr1 += 1
      if self.isBig2:
        self.tmr2 += 1
      if self.tmr1 == 5 and self.isBig1:
        self.left_arrow_image = pygame.transform.rotozoom(self.arrow_image, 90, 0.35)
      if self.tmr2 == 5 and self.isBig2:
        self.right_arrow_image = pygame.transform.rotozoom(self.arrow_image, -90, 0.35)
  
  def bigAndSmall(self, key):
    if key == "Left":
      self.isBig1 = True
      self.tmr1 = 0
      self.left_arrow_image = pygame.transform.rotozoom(self.arrow_image, 90, 0.45)
    if key == "Right":
      self.tmr2 = 0
      self.isBig2 = True
      self.right_arrow_image = pygame.transform.rotozoom(self.arrow_image, -90, 0.45)
