import pygame
import button
from pygame import mixer
import game
from window import Window
import buttoninherit
import os

class Menu:
    def __init__(self):
        pygame.mixer.init()
        self.screen = Window()
        self.run = True
        self.start_game = False
        self.menu_state = 'main'
        self.sound_volume = 0.5
        self.music_volume = 0.5

        self.difficulty_level = 1
        self.config_load()
        self.assets_load()        
        
        mixer.music.play(-1)
        mixer.music.set_volume(self.music_volume)

        

        self.menu()
    def menu(self):

        
        
        while self.run == True:
            self.screen.window.blit(self.main_menu_background,(0,0))
            pygame.time.Clock().tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    return False

            if self.menu_state == 'main':
                if self.start_button():
                    pass
                if self.options_button():
                    pass
                self.help_button()
                self.exit_button()
            elif self.menu_state == 'options':
                self.options_menu()
            elif self.menu_state == 'help':
                self.help_screen()
            self.sound_effect.set_volume(self.sound_volume)

            
            
            pygame.display.update()

    def options_menu(self):
        s = pygame.Surface((1920,1080))  # the size of your rect
        s.set_alpha(200)                # alpha level
        s.fill((0,0,0))           # this fills the entire surface
        self.screen.window.blit(s, (0,0))    # (0,0) are the top-left coordinates
        options_menu_image = pygame.transform.scale(self.options_menu_image, self.scale(self.options_menu_image))

        
        self.option_menu_width = options_menu_image.get_width()
        self.option_menu_height = options_menu_image.get_height()


        self.screen.window.blit(options_menu_image, ((self.screen.width/2)-(self.option_menu_width/2), (self.screen.height/2)-(self.option_menu_height/2)))

        self.sound_button(self.option_menu_width, self.option_menu_height)
        self.music_button(self.option_menu_width, self.option_menu_height)
        self.difficulty_button(self.option_menu_width, self.option_menu_height)
        self.back_button(self.option_menu_width, self.option_menu_height)

    def help_screen(self):

        s = pygame.Surface((1920,1080))  
        s.set_alpha(200)                
        s.fill((0,0,0))           
        self.screen.window.blit(s, (0,0))
           
        help_screen_image = pygame.transform.scale(self.help_screen_image, self.scale(self.help_screen_image))

        
        help_screen_width = help_screen_image.get_width()
        help_screen_height = help_screen_image.get_height()


        self.screen.window.blit(help_screen_image, ((self.screen.width/2)-(help_screen_width/2), (self.screen.height/2)-(help_screen_height/2)))

        self.back_button(help_screen_width, help_screen_height)


    def start_button(self):
        self.start_pressed_image = pygame.image.load('assets/menu/start_pressed.png')
        self.start_image = pygame.image.load('assets/menu/start_button.png')
        self.start_image = pygame.transform.scale(self.start_image,self.scale(self.start_image))
        self.start_pressed_image = pygame.transform.scale(self.start_pressed_image,self.scale(self.start_pressed_image))
        self.start_btn = buttoninherit.ButtonInherit((self.screen.width/2)-(self.start_image.get_width()/2),(self.screen.height*(2/20)),self.start_image,1)

        if not self.start_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.start_btn = buttoninherit.ButtonInherit((self.screen.width/2)-(self.start_image.get_width()/2),(self.screen.height*(2/20)),self.start_image,1)
        else:
            self.start_btn = buttoninherit.ButtonInherit((self.screen.width/2)-(self.start_pressed_image.get_width()/2),(self.screen.height*(2/20)),self.start_pressed_image,1)

        if self.start_btn.draw(self.screen.window):
            self.start_game = True
            self.run = False
            self.sound_effect.play()
        
    def options_button(self):
        self.options_pressed_image = pygame.image.load('assets/menu/options_pressed.png')
        self.options_image = pygame.image.load('assets/menu/options_button.png')
        self.options_image = pygame.transform.scale(self.options_image,self.scale(self.options_image))
        self.options_pressed_image = pygame.transform.scale(self.options_pressed_image,self.scale(self.options_pressed_image))

        self.options_btn = button.Button((self.screen.width/2)-(self.options_image.get_width()/2),(self.screen.height*(6/20)), self.options_image, 1)

        if not self.options_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.options_btn = button.Button((self.screen.width/2)-(self.options_image.get_width()/2),(self.screen.height*(6/20)),self.options_image,1)
        else:
            self.options_btn = button.Button((self.screen.width/2)-(self.options_pressed_image.get_width()/2),(self.screen.height*(6/20)),self.options_pressed_image,1)

        if self.options_btn.draw(self.screen.window):
            self.menu_state = 'options'
            self.sound_effect.play()

    def help_button(self):
        
        self.help_pressed_image = pygame.image.load('assets/menu/help_pressed.png')
        self.help_image = pygame.image.load('assets/menu/help_button.png')
        self.help_pressed_image = pygame.transform.scale(self.help_pressed_image,self.scale(self.help_pressed_image))
        self.help_image = pygame.transform.scale(self.help_image,self.scale(self.help_image))
        self.help_btn = button.Button((self.screen.width/2)-(self.help_image.get_width()/2),(self.screen.height*(10/20)), self.help_image, 1)

        if not self.help_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.help_btn = button.Button((self.screen.width/2)-(self.help_image.get_width()/2),(self.screen.height*(10/20)),self.help_image,1)
        else:
            self.help_btn = button.Button((self.screen.width/2)-(self.help_pressed_image.get_width()/2),(self.screen.height*(10/20)),self.help_pressed_image,1)

        if self.help_btn.draw(self.screen.window):
            self.sound_effect.play()
            self.menu_state = 'help'
            
    
    def exit_button(self):
        self.exit_pressed_image = pygame.image.load('assets/menu/exit_pressed.png')
        self.exit_image = pygame.image.load('assets/menu/exit_button.png')
        self.exit_image = pygame.transform.scale(self.exit_image,self.scale(self.exit_image))
        self.exit_pressed_image = pygame.transform.scale(self.exit_pressed_image,self.scale(self.exit_pressed_image))

        self.exit_btn = button.Button((self.screen.width/2)-(self.exit_image.get_width()/2),(self.screen.height*(14/20)), self.exit_image, 1)

        if not self.exit_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.exit_btn = button.Button((self.screen.width/2)-(self.exit_image.get_width()/2),(self.screen.height*(14/20)),self.exit_image,1)
        else:
            self.exit_btn = button.Button((self.screen.width/2)-(self.exit_pressed_image.get_width()/2),(self.screen.height*(14/20)),self.exit_pressed_image,1)

        if self.exit_btn.draw(self.screen.window):
                
                self.sound_effect.play()
                self.run = False
                return 'pressed'
                

    def sound_button(self,width,height):
        self.sound_btn = button.Button((self.screen.width/2)-(width*0.4),height*(1/5), self.sound_image, 1)

        if not self.sound_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.sound_btn = button.Button((self.screen.width/2)-(width*0.4),height*(1/5),self.sound_image,1)
        else:
            self.sound_btn = button.Button((self.screen.width/2)-(width*0.4),height*(1/5),self.sound_pressed_image,1)

        if self.sound_btn.draw(self.screen.window):
                self.sound_effect.play()

        self.numberFont = pygame.font.Font('assets/fonts/Minecraft.ttf', 120)
        self.volume_info = self.numberFont.render(str(round(self.sound_volume*100)), True, (0,0,0))
        self.screen.window.blit(self.volume_info, ((self.screen.width/2)+(width*0.25),height*(1/5)))

        self.volume_up(self.option_menu_width,height*(1/5),'sound')
        self.volume_down(self.option_menu_width,height*(1/5),'sound')
    
    def music_button(self,width,height):
        self.music_btn = button.Button((self.screen.width/2)-(width*0.4),height*(2/5), self.music_image, 1)

        if not self.music_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.music_btn = button.Button((self.screen.width/2)-(width*0.4),height*(2/5),self.music_image,1)
        else:
            self.music_btn = button.Button((self.screen.width/2)-(width*0.4),height*(2/5),self.music_pressed_image,1)

        if self.music_btn.draw(self.screen.window):
                self.sound_effect.play()

        self.numberFont = pygame.font.Font('assets/fonts/Minecraft.ttf', 120)
        self.volume_info = self.numberFont.render(str(round(self.music_volume*100)), True, (0,0,0))
        self.screen.window.blit(self.volume_info, ((self.screen.width/2)+(width*0.25),height*(2/5)))

        
        mixer.music.set_volume(self.music_volume)

        self.volume_up(self.option_menu_width,height*(2/5),'music')
        self.volume_down(self.option_menu_width,height*(2/5),'music')


    def difficulty_button(self,width,height):
        
        self.difficulty_btn = button.Button((self.screen.width/2)-(width*0.4),height*(3/5), self.difficulty_image, 1)

        if not self.difficulty_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.difficulty_btn = button.Button((self.screen.width/2)-(width*0.4),height*(3/5),self.difficulty_image,1)
        else:
            self.difficulty_btn = button.Button((self.screen.width/2)-(width*0.4),height*(3/5),self.difficulty_pressed_image,1)

        if self.difficulty_btn.draw(self.screen.window):
                self.sound_effect.play()
        
        self.difficulty_mode(self.option_menu_width,height*(3/5))

    def back_button(self,width,height):
        self.back_btn = button.Button((self.screen.width/2)-(width*0.4),height*(4/5), self.back_image, 1)

        if not self.back_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.back_btn = button.Button((self.screen.width/2)-(width*0.4),height*(4/5),self.back_image,1)
        else:
            self.back_btn = button.Button((self.screen.width/2)-(width*0.4),height*(4/5),self.back_pressed_image,1)

        if self.back_btn.draw(self.screen.window):
                self.menu_state = 'main'
                self.config_save()
                self.sound_effect.play()

    def volume_up(self,width,height,type):
        self.volume_up_btn = button.Button((self.screen.width/2)+(width*0.4),height, self.volume_up_image, 1)

        if not self.volume_up_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.volume_up_btn = button.Button((self.screen.width/2)+(width*0.4),height,self.volume_up_image,1)
        else:
            self.volume_up_btn = button.Button((self.screen.width/2)+(width*0.4),height,self.volume_up_pressed_image,1)

        if self.volume_up_btn.draw(self.screen.window):
            if type == 'sound':
                self.sound_volume += 0.01
                if self.sound_volume >= 1:
                    self.sound_volume = 1       
            if type == 'music':
                self.music_volume += 0.01
                if self.music_volume >= 1:
                    self.music_volume = 1                    

            self.sound_effect.play()
                    

    def volume_down(self,width,height,type):
        self.volume_down_btn = button.Button((self.screen.width/2)+(width*0.1),height, self.volume_down_image, 1)

        if not self.volume_down_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.volume_down_btn = button.Button((self.screen.width/2)+(width*0.1),height,self.volume_down_image,1)
        else:
            self.volume_down_btn = button.Button((self.screen.width/2)+(width*0.1),height,self.volume_down_pressed_image,1)

        if self.volume_down_btn.draw(self.screen.window):
                if type == 'sound':
                    self.sound_volume -= 0.01
                    if self.sound_volume <=0:
                        self.sound_volume = 0
                        
                elif type == 'music':
                    self.music_volume -= 0.01
                    if self.music_volume <=0:
                        self.music_volume = 0

                self.sound_effect.play()
                    
                    
    
    def arrow_left(self,width,height):
        self.arrow_left_btn = button.Button((self.screen.width/2)+(width*0.1),height, self.arrow_left_image, 1)

        if not self.arrow_left_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.arrow_left_btn = button.Button((self.screen.width/2)+(width*0.1),height,self.arrow_left_image,1)
        else:
            self.arrow_left_btn = button.Button((self.screen.width/2)+(width*0.1),height,self.arrow_left_pressed_image,1)

        if self.arrow_left_btn.draw(self.screen.window):
            self.sound_effect.play()
            return 1

    def arrow_right(self,width,height):
        
        self.arrow_right_btn = button.Button((self.screen.width/2)+(width*0.4),height, self.arrow_right_image, 1)

        if not self.arrow_right_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.arrow_right_btn = button.Button((self.screen.width/2)+(width*0.4),height,self.arrow_right_image,1)
        else:
            self.arrow_right_btn = button.Button((self.screen.width/2)+(width*0.4),height,self.arrow_right_pressed_image,1)

        if self.arrow_right_btn.draw(self.screen.window):
            self.sound_effect.play()
            return 1

    def resume_button(self):
        
        resume_image = pygame.transform.scale(self.resume_image,self.scale(self.resume_image))
        resume_pressed_image = pygame.transform.scale(self.resume_pressed_image,self.scale(self.resume_pressed_image))
        self.resume_btn = button.Button((self.screen.width/2)-(resume_image.get_width()/2),(self.screen.height*(2/20)),resume_image,1)

        if not self.resume_btn.rect.collidepoint(pygame.mouse.get_pos()):
            self.resume_btn = button.Button((self.screen.width/2)-(resume_image.get_width()/2),(self.screen.height*(2/20)),resume_image,1)
        else:
            self.resume_btn = button.Button((self.screen.width/2)-(resume_pressed_image.get_width()/2),(self.screen.height*(2/20)),resume_pressed_image,1)

        if self.resume_btn.draw(self.screen.window):
            self.sound_effect.play()
            return 'pressed'

    def difficulty_mode(self,width,height):

        

        self.diff_mode = self.mode_list[self.difficulty_level]

        if self.arrow_left(self.option_menu_width,height):
            self.difficulty_level-=1
            if self.difficulty_level<0:
                self.difficulty_level=2
        elif self.arrow_right(self.option_menu_width,height):
            self.difficulty_level += 1
            if self.difficulty_level>2:
                self.difficulty_level=0
        self.screen.window.blit(self.diff_mode, ((self.screen.width/2)+(width*0.17),height))

    def config_save(self):
        list_of_settings = [str(self.sound_volume),';', str(self.music_volume),';', str(self.difficulty_level)]

        config = open("data/config.txt", "w")
        config.writelines(list_of_settings)
        config.close()

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
            

    def scale(self,element):

        k_x = self.screen.width/1920
        k_y = self.screen.height/1080

        width = element.get_width()*k_x
        height = element.get_height()*k_y

        return (width,height)



    def assets_load(self):
    
        #difficulty
        self.mode_list = []
        self.mode_list.append(pygame.image.load('assets/menu/easy.png'))
        self.mode_list.append(pygame.image.load('assets/menu/normal.png'))
        self.mode_list.append(pygame.image.load('assets/menu/hard.png'))

        #menu
        self.options_menu_image = pygame.image.load('assets/menu/options_menu.png')
        self.pause_menu_image = pygame.image.load('assets/menu/pause_menu.png')
        
        self.resume_pressed_image = pygame.image.load('assets/menu/resume_pressed.png')
        self.resume_image = pygame.image.load('assets/menu/resume_button.png')

        self.sound_image = pygame.image.load('assets/menu/sound_button.png')
        self.sound_pressed_image = pygame.image.load('assets/menu/sound_pressed.png')
        self.music_pressed_image = pygame.image.load('assets/menu/music_pressed.png')
        self.music_image = pygame.image.load('assets/menu/music_button.png')
        self.arrow_right_pressed_image = pygame.image.load('assets/menu/arrow_right_pressed.png')
        self.arrow_right_image = pygame.image.load('assets/menu/arrow_right.png')
        self.arrow_left_pressed_image = pygame.image.load('assets/menu/arrow_left_pressed.png')
        self.arrow_left_image = pygame.image.load('assets/menu/arrow_left.png')
        self.volume_down_pressed_image = pygame.image.load('assets/menu/volume_down_pressed.png')
        self.volume_down_image = pygame.image.load('assets/menu/volume_down.png')
        self.volume_up_pressed_image = pygame.image.load('assets/menu/volume_up_pressed.png')
        self.volume_up_image = pygame.image.load('assets/menu/volume_up.png')
        self.back_pressed_image = pygame.image.load('assets/menu/back_pressed.png')
        self.back_image = pygame.image.load('assets/menu/back_button.png')
        self.difficulty_pressed_image = pygame.image.load('assets/menu/difficulty_pressed.png')
        self.difficulty_image = pygame.image.load('assets/menu/difficulty_button.png')
        self.help_screen_image = pygame.image.load('assets/menu/help_screen.png')
        self.main_menu_background = pygame.image.load('assets/menu/menu_background.png').convert()

        #sound
        self.sound_effect = mixer.Sound('assets/sound/laser.wav')
        mixer.music.load('assets/sound/Chiptronical.ogg')