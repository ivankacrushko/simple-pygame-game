import pygame

class Window:
    def __init__(self):
        pygame.font.init()
        self.height = 768
        self.width = 1366
        self.color = 200,200,200

        self.font = pygame.font.Font('assets/fonts/Minecraft.ttf', 120)
        pygame.display.set_caption('Kapi the Game no. 1')
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill((self.color))
        
        self.background = pygame.image.load('assets/graphic/background.png').convert()
        self.gameover = pygame.image.load('assets/menu/gameover.png').convert()
        
        

    def refresh(self):
        self.window.fill(self.color)
        self.window.blit(self.background,(0,0))

    def score(self,score):
        font = pygame.font.Font('assets/fonts/Minecraft.ttf', 40)
        text = f"SCORE: {score}"
        text_surface = font.render(text, False, (255,255,255))
        self.window.blit(text_surface, (0,0))
        
    def gameOver(self,score):
        self.window.fill(self.color)
        self.gameover_image = pygame.transform.scale(self.gameover, self.window_scale(self.gameover))
        self.window.blit(self.gameover_image,(0,0))

        img2 = self.font.render(f'Your score: {score}', True, (200,0,0))
        img2 = pygame.transform.scale(img2, self.window_scale(img2))
        img3 = self.font.render('Press SPACE to continue', True, (200,200,200))
        img3 = pygame.transform.scale(img3, self.window_scale(img3))
        
        self.window.blit(img2, ((self.width/2)-(img2.get_width()/2), self.height*(7/10)))
        self.window.blit(img3, ((self.width/2)-(img3.get_width()/2), self.height*(9/10)))

        pygame.display.update()

    def scoreboard(self,scoreboard,key):
        
        texts = []
        color = (255,255,255)
        waiting = True

        texts.append(self.font.render(f'User Name ...................... Score', True, color))
        texts[0] = pygame.transform.scale(texts[0], self.window_scale(texts[0]))
        for i in range(len(scoreboard)):
            texts.append(self.font.render(f'{scoreboard[i][0]} ................................ {scoreboard[i][1]}', True, color))
            texts[i+1] = pygame.transform.scale(texts[i+1], self.window_scale(texts[i+1]))
            print(f'user{i}')

        texts.append(self.font.render('Press SPACE to continue', True, color))
        texts[-1] = pygame.transform.scale(texts[-1], self.window_scale(texts[-1]))

        while waiting:
            self.window.fill((0,0,0))

            for i in range(len(texts)):
                self.window.blit(texts[i], ((self.width/10), i*self.height/7))

        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    if event.key == pygame.K_SPACE:
                        return True
                    
            pygame.display.update()
    
    def pause(self):
        waiting = True
        while waiting:
            self.window.fill((0,0,0))
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True
                    
            pygame.display.update()

    def save_score(self,score,user):
        def takeSecond(elem):
            return elem[1]

        cv = [user,score]
        scoreboard_file = open("data/scoreboard.txt", "r")
        scoreboard = scoreboard_file.readlines()
        
        for i in range(len(scoreboard)):
            scoreboard[i] = scoreboard[i].replace('\n','')
            scoreboard[i] = scoreboard[i].split(':')
            scoreboard[i][1] = int(scoreboard[i][1])
        scoreboard.sort(key=takeSecond)
        
        scoreboard.sort()
        for i in range(len(scoreboard)):
            if scoreboard[i][1] < cv[1]:
                scoreboard[i] = cv
                break
        scoreboard.sort(reverse=True, key=takeSecond)
        scoreboard_file.close()
        
        
        scoreobard_file = open("scoreboard.txt", "w")
        for i in range(len(scoreboard)):
            line = scoreboard[i][0],':',str(scoreboard[i][1]),'\n'
            scoreobard_file.writelines(line)

        return scoreboard

    def wait_for_key(self,key,score):
        waiting = True
        while waiting:
            events = pygame.event.get()
            keys = pygame.key.get_pressed()
            for event in events:
                if event.type == pygame.QUIT:
                    waiting = False
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    if event.key == pygame.K_SPACE:
                        return True
                    if event.key == pygame.K_RETURN:
                        return(self.scoreboard(self.save_score(score,'user'),key))

    def window_scale(self,element):

        k_x = self.width/1920
        k_y = self.height/1080

        width = element.get_width()*k_x
        height = element.get_height()*k_y

        return (width,height)
