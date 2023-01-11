import pygame
import random

class Food:
    def __init__(self,screen):
        self.width = 32
        self.height = 32
        self.x = random.randint(25,screen.get_width() - 50)
        self.y = random.randint(25,screen.get_height() - 50)
        self.color = 0,0,200

        self.food = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.food = pygame.draw.rect(screen, (self.color), self.food)
        
        self.food_image = pygame.image.load('assets/graphic/monster.png')



    def generate(self,screen):
        #self.food = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        #self.food = pygame.draw.rect(screen, (self.color), self.food)

        self.food = self.food_image.get_rect(x=self.x, y=self.y)
        screen.blit(self.food_image, self.food)

    def obtain(self,screen):
        self.x = random.randint(25, screen.get_width() - 50)
        self.y = random.randint(25, screen.get_height() - 50)
       # self.food = pygame.rect.Rect(self.x, self.y, self.width, self.height)
       # self.food = pygame.draw.rect(screen, (self.color), self.food)

        self.food = self.food_image.get_rect(x=self.x, y=self.y)
        screen.blit(self.food_image, self.food)


        

        return True

   
        