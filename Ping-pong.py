from pygame import *

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed, player_weight, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_weight, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def l_control(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    
    def r_control(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (231, 212, 150)
win_weight = 600
win_height = 500

window = display.set_mode((win_weight, win_height))
window.fill(back)
display.set_caption('Ping-pong')

clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0 , 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0 , 0))

speed_x = 3
speed_y = 3

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not(finish):
        window.fill(back)

        racket1.l_control()
        racket2.r_control()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        racket1.reset()
        racket2.reset()
        ball.reset()

    clock.tick(FPS)

    display.update()
