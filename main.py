import pygame as pg
pg.init()

width, height = 500, 500

screen = pg.display.set_mode((width, height))
pg.display.set_caption("Test")

objects = pg.sprite.Group()

class Object(pg.sprite.Sprite):
  def __init__(self, size, color, pos):
    super().__init__()
    objects.add(self)

    self.image = pg.Surface(size)
    self.image.fill(color)

    self.rect = self.image.get_rect()
    self.rect.center = pos


red_box = Object((50, 50), "red", (width/2, height/2))

#Vars
clock = pg.time.Clock()
running = True

while running:
  #Limits fps to 30
  clock.tick(30)

  #Exits on game quit (close tab)
  for event in pg.event.get():
    if event.type == pg.QUIT: 
      running = False

  keys = pg.key.get_pressed()
  up = keys[pg.K_w] or keys[pg.K_UP]
  left = keys[pg.K_a] or keys[pg.K_LEFT]
  down = keys[pg.K_s] or keys[pg.K_DOWN]
  right = keys[pg.K_d] or keys[pg.K_RIGHT]

  red_box.rect.x += (right - left) * 5
  red_box.rect.y += (down - up) * 5

  #BG
  screen.fill((255, 255, 255))
  #Objects
  objects.draw(screen)
  #Load
  pg.display.update()