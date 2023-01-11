import pygame
from pygame import mixer
import os

class Snake:
    def __init__(self, screen, enemy_list):
        pygame.mixer.init()
        self.config_load()
        self.difficulty()
        self.width = 32
        self.height = 32
        self.x = 640
        self.y = 360
        self.color = 0,200,0
        self.head = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.snake = pygame.draw.rect(screen, (self.color), self.head)
        self.screen = screen
        self.speed_x=0
        self.speed_y=0
        self.score = 0
        self.enemy_spawn = False
        self.direction = 0
        self.bullet_state = 'ready'
        self.bullet_speed = 15

        self.sound_effect_death = mixer.Sound('assets/sound/death.wav')
        self.sound_effect_food = mixer.Sound('assets/sound/food.wav')
        self.sound_effect_enemy = mixer.Sound('assets/sound/enemy.wav')
        self.sound_effect_death.set_volume(self.sound_volume)
        self.sound_effect_food.set_volume(self.sound_volume)
        self.sound_effect_enemy.set_volume(self.sound_volume)

        self.snake_image = pygame.image.load('assets/graphic/space.png')
        self.snake_image_move = pygame.image.load('assets/graphic/space_move.png')
        self.base_bullet_image = pygame.image.load('assets/graphic/bullet.png')


    def move(self, screen):
        keys = pygame.key.get_pressed()      
        self.snake_img = pygame.transform.rotate(self.snake_image, self.direction)

        if keys[pygame.K_RIGHT]:
            self.speed_x += self.core_speed/10
            if self.speed_x >= self.core_speed:
                self.speed_x = self.core_speed
            self.x += self.speed_x

            self.snake_img = pygame.transform.rotate(self.snake_image_move, -90)
            self.direction = -90

        if keys[pygame.K_LEFT]:
            self.speed_x += self.core_speed/10
            if self.speed_x >= self.core_speed:
                self.speed_x = self.core_speed
            self.x -= self.speed_x

            self.snake_img = pygame.transform.rotate(self.snake_image_move, 90)
            self.direction = 90
            
        if keys[pygame.K_UP]:

            self.speed_y +=self.core_speed/10
            if self.speed_y >= self.core_speed:
                self.speed_y = self.core_speed
            self.y -= self.speed_y

            self.snake_img = pygame.transform.rotate(self.snake_image_move, self.direction)
            self.direction = 0

        if keys[pygame.K_DOWN]:
            self.speed_y +=self.core_speed/10
            if self.speed_y >= self.core_speed:
                self.speed_y = self.core_speed
            self.y += self.speed_y

            self.snake_img = pygame.transform.rotate(self.snake_image_move, 180)
            self.direction = 180

        if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            
            self.snake_img = pygame.transform.rotate(self.snake_image_move, -45)
            self.direction = -45

        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            
            self.snake_img = pygame.transform.rotate(self.snake_image_move, 45)
            self.direction = 45

        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            
            self.snake_img = pygame.transform.rotate(self.snake_image_move, 135)
            self.direction = 135

        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:

            self.snake_img = pygame.transform.rotate(self.snake_image_move, 225)
            self.direction = 225

        if self.direction == 0:
            self.y -= self.speed_y
        elif self.direction == 90:
            self.x -= self.speed_x
        elif self.direction == -90:
            self.x += self.speed_x
        elif self.direction == 180:
            self.y += self.speed_y

        if not any(keys):
                if self.speed_x or self.speed_y <=0:
                    self.speed_x = 0
                    self.speed_y = 0
                else:
                    self.speed_x -=0.2
                    self.speed_y -=0.2        


        if keys[pygame.K_SPACE]:
            if self.bullet_state == 'ready':
                self.fire_bullet()

        if self.bullet_state == 'fire' and self.shooting_approval == True:
            self.bullet_movement(screen)




        self.border()
        self.snake = self.snake_img.get_rect(x=self.x, y=self.y)
        screen.blit(self.snake_img, self.snake)        
        
    def border(self):

        if self.x > self.screen.get_width()+25:
            self.x = -25
        if self.x < -25:
            self.x = self.screen.get_width() + 25
        if self.y > self.screen.get_height() + 25:
            self.y = -25
        if self.y < -25:
            self.y = self.screen.get_height() + 25
        

    def collisionFood(self,food):

        self.collideFood = pygame.Rect.colliderect(self.snake, food)
        if self.collideFood:
            self.sound_effect_food.play()
            self.score +=1
            self.core_speed += self.speed_increase
            self.enemy_spawn = True
            return self.score

    def collisionEnemy(self,enemy_list):

        for enemy in enemy_list:
            self.collideEnemy = pygame.Rect.colliderect(self.snake, enemy)
            if self.collideEnemy:
                self.sound_effect_death.play()
                self.x = 640
                self.y = 360
                self.core_speed = 3
                return 1

    def fire_bullet(self):
        
        self.bullet_x = self.x
        self.bullet_y = self.y
        self.bullet_direction = self.direction
        self.bullet_state = 'fire'

    def bullet_movement(self ,screen):
        if self.bullet_direction == 90:
            self.bullet_image = pygame.transform.rotate(self.base_bullet_image, 90)
            self.bullet_x -= self.bullet_speed
    
        if self.bullet_direction == -90:
            self.bullet_image = pygame.transform.rotate(self.base_bullet_image, -90)
            self.bullet_x += self.bullet_speed

        if self.bullet_direction == 0:
            self.bullet_image = pygame.transform.rotate(self.base_bullet_image, 0)
            self.bullet_y -= self.bullet_speed

        if self.bullet_direction == 180:
            self.bullet_image = pygame.transform.rotate(self.base_bullet_image, 180)
            self.bullet_y += self.bullet_speed

        if self.bullet_direction == 45:
            self.bullet_image = pygame.transform.rotate(self.base_bullet_image, 45)
            self.bullet_y -= self.bullet_speed
            self.bullet_x -= self.bullet_speed

        if self.bullet_direction == 135:
            self.bullet_image = pygame.transform.rotate(self.base_bullet_image, 135)
            self.bullet_x -= self.bullet_speed
            self.bullet_y += self.bullet_speed

        if self.bullet_direction == -45:
            self.bullet_image = pygame.transform.rotate(self.base_bullet_image, -45)
            self.bullet_x += self.bullet_speed
            self.bullet_y -= self.bullet_speed
        if self.bullet_direction == 225:
            self.bullet_image = pygame.transform.rotate(self.base_bullet_image, 225)
            self.bullet_x += self.bullet_speed
            self.bullet_y += self.bullet_speed

        self.bullet_fire = self.bullet_image.get_rect(x=self.bullet_x, y=self.bullet_y)
        screen.blit(self.bullet_image, self.bullet_fire)
        
        if self.bullet_x > 1945:
            self.bullet_x = self.x
            self.bullet_state = 'ready'
        if self.bullet_x < -25:
            self.bullet_x = self.x
            self.bullet_state = 'ready'
        if self.bullet_y >1105:
            self.bullet_y = self.y
            self.bullet_state = 'ready'
        if self.bullet_y < -25:
            self.bullet_y = self.y
            self.bullet_state = 'ready'
        
    def enemyShot(self,enemy_list):

        for enemy in enemy_list:
            try:
                self.collideEnemy = pygame.Rect.colliderect(self.bullet_fire, enemy)
            except:
                pass
            if self.collideEnemy:
                
                self.sound_effect_enemy.play()
                return enemy
                
    def config_load(self):
        if not os.path.exists('data/config.txt'):
            pass
        else:
            config = open('data/config.txt', 'r')
            config = config.readline()
            config = config.split(';')

            self.sound_volume = float(config[0])
            self.music_volume = float(config[1])
            self.difficulty_level = int(config[2])

    def difficulty(self):
        if self.difficulty_level == 0:
            self.core_speed = 2
            self.speed_increase = 0.3
            self.shooting_approval = True

        elif self.difficulty_level == 1:
            self.core_speed = 3
            self.speed_increase = 0.3
            self.shooting_approval = True

        elif self.difficulty_level == 2:
            self.core_speed = 3
            self.speed_increase = 0.5
            self.shooting_approval = False
        
            
                    



