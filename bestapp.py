import pygame
import sys
import random
from PIL import Image

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.ani = False
        self.sprites = []
        self.sprites.append(pygame.image.load('ani/bang-0.png'))
        self.sprites.append(pygame.image.load('ani/bang-1.png'))
        self.sprites.append(pygame.image.load('ani/bang-2.png'))
        self.sprites.append(pygame.image.load('ani/bang-3.png'))
        self.sprites.append(pygame.image.load('ani/bang-4.png'))
        self.sprites.append(pygame.image.load('ani/bang-5.png'))
        self.sprites.append(pygame.image.load('ani/bang-6.png'))
        self.sprites.append(pygame.image.load('ani/bang-7.png'))
        self.sprites.append(pygame.image.load('ani/bang-8.png'))
        self.sprites.append(pygame.image.load('ani/bang-9.png'))
        self.sprites.append(pygame.image.load('ani/bang-10.png'))
        self.sprites.append(pygame.image.load('ani/bang-11.png'))
        self.sprites.append(pygame.image.load('ani/bang-12.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def bangani(self):
        self.ani = True

    def update(self,speed):
        if self.ani == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.ani = False

        self.image = self.sprites[int(self.current_sprite)]

class Player2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.ani2 = False
        self.sprites = []
        self.sprites.append(pygame.image.load('ani2/1-0.png'))
        self.sprites.append(pygame.image.load('ani2/1-1.png'))
        self.sprites.append(pygame.image.load('ani2/1-2.png'))
        self.sprites.append(pygame.image.load('ani2/1-3.png'))
        self.sprites.append(pygame.image.load('ani2/1-4.png'))
        self.sprites.append(pygame.image.load('ani2/1-5.png'))
        self.sprites.append(pygame.image.load('ani2/1-6.png'))
        self.sprites.append(pygame.image.load('ani2/1-7.png'))
        self.sprites.append(pygame.image.load('ani2/1-8.png'))
        self.sprites.append(pygame.image.load('ani2/1-9.png'))
        self.sprites.append(pygame.image.load('ani2/1-10.png'))
        self.sprites.append(pygame.image.load('ani2/1-11.png'))
        self.sprites.append(pygame.image.load('ani2/1-12.png'))
        self.sprites.append(pygame.image.load('ani2/1-13.png'))
        self.sprites.append(pygame.image.load('ani2/1-14.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def anoneani(self):
        self.ani2 = True

    def update(self,speed):
        if self.ani2 == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.ani2 = False

        self.image = self.sprites[int(self.current_sprite)]

class Button:
    def __init__ ( self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('MTO Grunge Sans.ttf', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

class Button2():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

def show_score(x, y):
    
    score = font.render("Counting : " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

def loop():
    if choose == 0:
        player.bangani()
        bang.play()	
    if choose == 1:
        player2.anoneani()
        anone.play()

moving_sprites = pygame.sprite.Group()
player = Player(110, 80 )
moving_sprites.add(player)

moving_sprites2 = pygame.sprite.Group()
player2 = Player2(110, 80 )
moving_sprites2.add(player2)

logo = pygame.image.load('logo bang.jpg')
pygame.display.set_icon(logo)

clock = pygame.time.Clock()
pygame.display.set_caption("Bangg")
size = screen_width, screen_height = 705, 500
color = 151, 190, 182
screen=pygame.display.set_mode((screen_width, screen_height))

anone = pygame.mixer.Sound('anone anoneee.mp3')
bang = pygame.mixer.Sound('bang.mp3')
score_value = 0
font = pygame.font.Font('MTO Grunge Sans.ttf', 50)
textX = 265
testY = 5

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (151, 190, 182)
WHITE = (255, 255, 255)
mBLUE = (68, 89, 142)

chooselist = [0]
choose = chooselist[0]
auto = False

leftb = pygame.image.load('left.jpg').convert_alpha()
rightb = pygame.image.load('right.jpg').convert_alpha()

left_button = Button2(25, 220, leftb, 0.8)
right_button = Button2(630, 220, rightb, 0.8)

while 1:
    play_button = Button(285, 430, 150, 50, WHITE, mBLUE, 'BANGG!', 40)
    replay_button = Button(120, 430, 100, 50, WHITE, mBLUE, 'AUTO', 40)	
    breplay_button = Button(120, 430, 100, 50, BLACK, mBLUE, 'AUTO', 40)	    
    quit_button = Button(490, 430, 100, 50, WHITE, mBLUE, 'QUIT', 40)	

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if left_button.draw(screen):
            if choose == chooselist[0] :
                choose = 1
            elif choose == chooselist[1] :
                choose = 0
        elif right_button.draw(screen):
            if choose == chooselist[0] :
                choose = 1
            elif choose == chooselist[1] :
                choose = 0

        if choose == chooselist[0] :
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                auto = False
                player.bangani()
                bang.play()
                score_value += 1
            
        elif choose == chooselist[1] :
             if play_button.is_pressed(mouse_pos, mouse_pressed):
                auto = False
                player2.anoneani()
                anone.play()
                score_value += 1
        
        if replay_button.is_pressed(mouse_pos, mouse_pressed):
            if auto == False :	
                auto = True 
            elif auto == True :
                auto = False
        
        if quit_button.is_pressed(mouse_pos, mouse_pressed):
            sys.exit()

    if auto :
        loop()			

    if score_value >= 10:
        chooselist=[0, 1]

    screen.fill(color)
    if choose == 0 :
        moving_sprites.draw(screen)
        moving_sprites.update(0.25)
    elif choose == 1 :
        moving_sprites2.draw(screen)
        moving_sprites2.update(0.25)
    # screen.blit(test, testrect)

    screen.blit(leftb, (25, 220))
    screen.blit(rightb, (630, 220))

    screen.blit(play_button.image, play_button.rect)
    screen.blit(quit_button.image, quit_button.rect)
    if auto:
        screen.blit(breplay_button.image, breplay_button.rect)
    elif auto == False :
        screen.blit(replay_button.image, replay_button.rect)	
    show_score(textX, testY)
    clock.tick(60)
    pygame.display.flip()
