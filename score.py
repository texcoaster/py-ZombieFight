from game_config import GameConfig
from gameobject import *
from text_utils import *
from game_config import *

class Score(GameObject):
  def __init__(self):
    super().__init__(0, 0)
    self.highscore = 0
    self.is_new_record = False
  
  def draw(self, screen):
    if self.highscore < GameConfig.score:
      self.highscore = GameConfig.score
      self.is_new_record = True

    TextUtils.drawText(screen, 150, 35, "Score:"+str(GameConfig.score), (255, 255, 255), 65)
    TextUtils.drawText(screen, 700, 35, "HighScore:"+str(self.highscore), (255, 255, 255), 65, self.is_new_record)
