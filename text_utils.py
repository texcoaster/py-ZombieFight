import pygame

class TextUtils:
  def drawText(screen, x, y, text, color, size, pretty=False):
    if pretty == False:
      fnt = pygame.font.Font(None, size)
      sur = fnt.render(text, True, color)
      screen.blit(sur, [x-sur.get_width()/2, y-sur.get_height()/2])

    if pretty == True:
      fnt = pygame.font.Font(None, size)
      cr = int(color[0] / 2)
      cg = int(color[1] / 2)
      cb = int(color[2] / 2)

      sur = fnt.render(text, True, (cr, cg, cb))
      x = x - sur.get_width() / 2
      y = y - sur.get_height() / 2
      screen.blit(sur, [x + 1, y + 1])

      cr = color[0] + 128
      if cr > 255: cr = 255
      cg = color[1] + 128
      if cg > 255: cg = 255
      cb = color[2] + 128
      if cb > 255: cb = 255

      sur = fnt.render(text, True, (cr, cg, cb))
      screen.blit(sur, [x - 1, y - 1])
      sur = fnt.render(text, True, color)
      screen.blit(sur, [x, y])