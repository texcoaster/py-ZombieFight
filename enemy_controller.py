import random
from enemy import *

class EnemyController(GameObject):
  def __init__(self):
    super().__init__(0, 0)
    self.enemyFiles = [
      ["_images/enemy/enemy1_boss.png", "_images/enemy/enemy1_1.png", "_images/enemy/enemy1_2.png"]
    ]
    self.tmr = 0
  
  def draw(self, screen):
    for child in self.children:
      child.draw(screen)
    self.generate()
  
  def generate(self):
    if GameConfig.index == 1:
      self.tmr += 1

      if self.tmr < 900:
        if self.tmr % 20 == 0:
          self.children.append(Enemy(random.randint(-100, 1060), random.choice([-100, 820]), self.enemyFiles[0][1], 2, 5, 20))
        if self.tmr % 50 == 0:
          self.children.append(Enemy(random.randint(-100, 1060), random.choice([-100, 820]), self.enemyFiles[0][2], 6, 5, 5))
      if self.tmr == 900:
        self.children.append(Enemy(random.randint(-100, 1060), random.choice([-100, 820]), self.enemyFiles[0][0], 4, 15, 200))
  
  def goUp(self):
    for child in self.children:
      child.goUp()
  def goDown(self):
    for child in self.children:
      child.goDown()
  def goLeft(self):
    for child in self.children:
      child.goLeft()
  def goRight(self):
    for child in self.children:
      child.goRight()
