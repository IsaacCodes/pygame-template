import pygame as pg
pg.init()

width, height = 500, 500

screen = pg.display.set_mode((width, height))
pg.display.set_caption("Pygame Template")

objects = pg.sprite.Group()


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

  
  #BG
  screen.fill((255, 255, 255))
  #Objects
  objects.draw(screen)
  #Load
  pg.display.update()