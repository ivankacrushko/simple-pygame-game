import random

class Restart:
    def __init__(self,player,food,enemy):
        player.x = 640
        player.y = 360
        food.x = random.randint(25,1230)
        food.y = random.randint(25,690)
        player.score = 0
        player.speed = 3
        enemy.enemy_list.clear()
        
