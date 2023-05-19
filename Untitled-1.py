from pygame import * 
from random import randint
from time import time as timer

font.init()

life = 3
win_width1 = 700
window = display.set_mode((700,500))
win_heidht1 = 500

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image =  transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        
        self.rect.x = player_x
        self.rect.y = player_y

    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):   
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_heidht1 - 25 :
            self.rect.y += self.speed
    

    


ball = Player('baall.png',500,400,200,20,10)




background = transform.scale(image.load('image.png.jpg'), (win_width1, win_heidht1))


game = True
rel_time = False

finish = False
while game:
    

    for e in event.get():
        if e.type == QUIT:
            
            game = False
        
        
    display.update() 
    if not finish: 

        window.blit(background,(0,0))
        ball.reset()
        ball.update()
        
    
     
    time.delay(30)

