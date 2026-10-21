#Create your own shooter

from pygame import *
from random import randint 

"Required classes"


score = 0
lost = 0


#parent class for sprites
class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,):
        super().__init__()
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #every sprite must have the rect property - the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#heir class for the player sprite (controlled by arrows)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed


#heir class for the enemy sprite (moves by itself)
class Enemy1(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(1, 650)
            self.rect.y = 0
            lost = lost + 1
            

#Game scene
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter game")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))


monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy1('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)


#Game player
player = Player('rocket.png', 5, win_height - 80, 80, 100, 10)


game = True 
clock = time.Clock()
FPS = 200
finish = False


font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))


#music
# mixer.init()
# mixer.music.load()
# mixer.music.play()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    
    if finish != True:  
        window.blit(background,(0, 0))
        

        #write text on the screen
        text = font.render("score: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))


        text_lose = font.render("score: " + str(lost), 1, (255, 255, 255))
        window.blit(text, (10, 50))


        #launch sprite movement
        player.update()   
        player.reset()        
        monsters.update()
        monsters.draw(window)

        display.update()
    clock.tick(FPS)
    time.delay(20)
