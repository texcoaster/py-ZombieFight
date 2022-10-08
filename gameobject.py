class GameObject:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.children = []

  def keyInput(self, key):
    for child in self.children:
      child.keyInput(key)

  def draw(self, screen):
    for child in self.children:
      child.draw(screen)
  
  def goUp(self):
    pass
  def goDown(self):
    pass
  def goLeft(self):
    pass
  def goRight(self):
    pass
