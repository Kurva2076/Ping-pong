from pygame import *

back = (231, 212, 150)
win_weight = 600
win_height = 500

window = display.set_mode((win_weight, win_height))
window.fill(back)
display.set_caption('Ping-pong')

clock = time.Clock()
FPS = 60

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    #if not(finish):


    clock.tick(FPS)

    display.update()