import pygame
from window import Window
from cards import Snake
from enemy import Enemy
from food import Food
from reset import Restart



class Game():
    def __init__(self):
        pygame.init()

        self.window = Window()
        self.food = Food(self.window.window)
        self.enemy = Enemy(self.window.window)
        self.player = Snake(self.window.window, self.enemy.enemy_list)
        self.no_enemies = 0
        self.paused = False
        self.game_on()

    def game_on(self):
        playing=True
        while playing:
            
            run = True
            while run:
                self.window.refresh()
                pygame.time.Clock().tick(60)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        playing = False
                        return False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            run = False
                            playing = False
                            return False
                                               
                if self.player.collisionEnemy(self.enemy.enemy_list) == 1:
                    self.window.gameOver(self.player.score)
                    self.no_enemies = 0
                    self.playing=False
                    if self.window.wait_for_key(any,self.player.score) == False:  
                        playing = False
                        run = False
                    else:
                        #self.window.scoreboard(self.window.save_score(self.player.score, 'user'),any)
                        run = False
                        playing=True
                        Restart(self.player,self.food,self.enemy)
                if self.player.enemyShot(self.enemy.enemy_list):
                    self.enemy.gotShot(self.player.enemyShot(self.enemy.enemy_list),self.window.window)
                    self.player.score +=1
                approval = False
                if self.player.collisionFood(self.food.food):
                    self.food.obtain(self.window.window)
                    self.no_enemies += 1
                    approval = True
                self.player.move(self.window.window)
                self.enemy.enemyMovement()
                self.enemy.enemy_spawn(self.window.window,self.no_enemies, approval)
                self.food.generate(self.window.window)
                
                self.window.score(self.player.score)
                
                
                pygame.display.update()