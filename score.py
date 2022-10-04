from gameobject import *
from text_utils import *

class Score(GameObject):
  score = 0

  def __init__(self):
    super().__init__(0, 0)
    self.highscore = 0
    self.is_new_record = False
  
  def draw(self, screen):
    if self.highscore < Score.score:
      self.highscore = Score.score
      self.is_new_record = True

    TextUtils.drawText(screen, 150, 35, "Score:"+str(Score.score), (255, 255, 255), 65)
    TextUtils.drawText(screen, 700, 35, "HighScore:"+str(self.highscore), (255, 255, 255), 65, self.is_new_record)
