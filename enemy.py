import pygame
import random

class Enemy:
    def __init__(self,screen):
        self.width = 32
        self.height = 32
        self.x = random.randint(25, screen.get_width() - 25)
        self.y = random.randint(25, screen.get_height() - 25)
        self.color = 200,0,0
        self.enemy_list = []
        self.enemy_x = []
        self.enemy_y = []
        self.enemy_dir = []
        self.alphacolor = 0,0,0,255
        self.enemy_image = pygame.image.load('assets/graphic/ufo.png')
        self.enemy_speed=0
        self.enemy_direction='horizontal'
        self.increasing = True
        

    def enemy_spawn(self, screen, no_enemies, new_enemy):
        
            
            if new_enemy == True:
                self.enemy_list.append(0)
                self.enemy_x.append(random.randint(25,screen.get_width() - 25))
                self.enemy_y.append(random.randint(25,screen.get_height() - 25))
                self.enemy_dir.append(random.randint(0,1))
                
                if self.enemy_dir[-1] == 1:
                    self.enemy_dir[-1] = 'horizontal'
                else:
                    self.enemy_dir[-1] = 'vertical'
            

            for i in range(no_enemies):
                
                self.enemy_list[i] = self.enemy_image.get_rect(x=self.enemy_x[i], y=self.enemy_y[i])
                screen.blit(self.enemy_image, self.enemy_list[i])

    def enemy_info(self):
        print(self.enemy_list)

    def gotShot(self,enemy,screen):
        for i in range(len(self.enemy_list)):
            if self.enemy_list[i] == enemy:
                self.enemy_x[i] = 3000
                self.enemy_y[i] = 3000
        
    def enemyMovement(self):
        
        for i in range(len(self.enemy_list)):
            if self.enemy_dir[i] =='horizontal':
                if self.increasing == True:
                    self.enemy_x[i] += 0.5
                    self.enemy_speed +=0.5
                    if self.enemy_speed == 150:
                        self.increasing = False
                if self.increasing == False:
                    self.enemy_x[i] -= 0.5
                    self.enemy_speed -=0.5
                    if self.enemy_speed == 0:
                        self.increasing = True
            else:
                if self.increasing == True:
                    self.enemy_y[i] += 0.5
                    self.enemy_speed +=0.5
                    if self.enemy_speed == 150:
                        self.increasing = False
                if self.increasing == False:
                    self.enemy_y[i] -= 0.5
                    self.enemy_speed -=0.5
                    if self.enemy_speed == 0:
                        self.increasing = True
                
        
            

        


        
