import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite

class Button():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()        
        self.rect = pygame.Rect(0, 0, 199, 66)
        self.rect.center = self.screen_rect.center
        self.button_color = (0, 255, 0)
        self.font_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.msg_image = self.font.render("Start Game", True, self.font_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_button(self, active):
        if active == 0:
            self.screen.fill(self.button_color, self.rect)
            self.screen.blit(self.msg_image, self.msg_image_rect)
        
class HitTarget(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()        
        self.rect = pygame.Rect(0, 0, 16, 99)
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.right  
        self.dir = 1    
        self.speed = 0.1
        self.y_distance = 0
    def move(self):
        if (self.rect.bottom > self.screen_rect.bottom):
            self.dir = -1
        elif (self.rect.top < self.screen_rect.top):
            self.dir = 1
        self.y_distance += self.dir * self.speed
        self.rect.centery = int(self.y_distance)
        pygame.draw.rect(self.screen, (66, 9, 9), self.rect)
        
class Bullet(Sprite):
    def __init__(self, ship, screen):
        super().__init__()      
        self.rect = pygame.Rect(0, 0, 12, 6)
        self.rect.centery = ship.rect.centery
        self.rect.centerx = ship.rect.centerx
        self.screen = screen
        self.screen_rect = screen.get_rect()
    def update(self):
        self.rect.centerx += 1
        pygame.draw.rect(self.screen, (66, 9, 9), self.rect)    

class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("ship2.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = 0
        self.rect.centery = self.screen_rect.centery
        self.move_left = False
        self.move_right = False
        self.move_top = False
        self.move_bottom = False
    def blitme(self, active):
        if active == 1:
            if (self.move_left == True and self.rect.left > 0):
                self.rect.centerx -= 1
            elif (self.move_right == True and self.rect.right < self.screen_rect.right):
                self.rect.centerx += 1
            elif (self.move_top == True and self.rect.top > 0):
                self.rect.centery -= 1  
            elif (self.move_bottom == True and self.rect.bottom < self.screen_rect.bottom):
                self.rect.centery += 1  
        self.screen.blit(self.image, self.rect)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((666, 555))
    bgcolor = (222, 222, 255)
    screen.fill(bgcolor)
    
    ship = Ship(screen)
    hittarget = HitTarget(screen)
    bullets = Group()
    
    button = Button(screen)
    
    active = 0
    fire_cnt = 0
    
    pygame.display.set_caption("Blue Skey")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #ship.move_left = True
                    pass
                elif event.key == pygame.K_RIGHT:
                    #ship.move_right = True 
                    pass
                elif event.key == pygame.K_UP:
                    ship.move_top = True
                elif event.key == pygame.K_DOWN:
                    ship.move_bottom = True
                elif event.key == pygame.K_SPACE:
                    if active == 1:
                        bullet = Bullet(ship, screen)
                        bullets.add(bullet)
                        fire_cnt += 1
                        if (fire_cnt > 3):
                            print("Restart")
                            fire_cnt = 0
                            active = 0
                            hittarget.speed = 0.1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ship.move_left = False
                elif event.key == pygame.K_RIGHT:
                    ship.move_right = False 
                elif event.key == pygame.K_UP:
                    ship.move_top = False
                elif event.key == pygame.K_DOWN:
                    ship.move_bottom = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button.rect.collidepoint(mouse_x, mouse_y) and active == 0:
                    print("click start")
                    active = 1
                        
        screen.fill(bgcolor)            
        ship.blitme(active)
        bullets.update()
        for cur_bullet in bullets.copy():
            if (cur_bullet.rect.centerx > cur_bullet.screen_rect.right):
                bullets.remove(cur_bullet)
        if active == 1:
            hittarget.move()
        collide_bullet = pygame.sprite.spritecollideany(hittarget, bullets)
        if collide_bullet:
            print("heat!")
            fire_cnt = 0
            bullets.remove(collide_bullet)
            hittarget.speed += 0.1
        button.draw_button(active)
        pygame.display.flip()
        
run_game()
