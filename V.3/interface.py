import pygame
from pygame.locals import *

class Interface:

    def __init__(self, screen):
        
        pygame.init()

        self.screen = screen

        self.screen_center = (self.screen.get_width() / 2, self.screen.get_height() / 2)

        self.Menu()

        print(self.screen)
    
    def Menu(self):

        """
        big button : 1
        small button : 4
        """

        # Load Font
        
        big_button_font = pygame.font.Font("Project_Elastique/V.3/font/Arcade.ttf", 35)
        small_button_font = pygame.font.Font("Project_Elastique/V.3/font/Arcade.ttf", 25)

        # Load image or color
        background = pygame.image.load("Project_Elastique/V.3/texture/background.png").convert_alpha()
        big_button = pygame.image.load("Project_Elastique/V.3/texture/button.png").convert_alpha()
        small_button = pygame.image.load("Project_Elastique/V.3/texture/button.png").convert_alpha()

        # Coef resize for image
        coef = (self.screen.get_width()+self.screen.get_height())/(big_button.get_width()+big_button.get_height())
        big_button_coef = 1/3
        small_button_coef = 1/4

        # Resize img
        background =  pygame.transform.scale(background, (self.screen.get_width(),self.screen.get_height()))
        big_button = pygame.transform.scale(big_button, (int(big_button.get_width()*coef*big_button_coef), int(big_button.get_height()*coef*big_button_coef)))
        small_button = pygame.transform.scale(small_button, (int(small_button.get_width()*coef*small_button_coef), int(small_button.get_height()*coef*small_button_coef)))

        # Text render
        big_button_txt_1 = big_button_font.render('Play', True, (255,255,255))
        small_button_txt_1 = small_button_font.render('Setting', True, (255,255,255))
        small_button_txt_2 = small_button_font.render('Quit', True, (255,255,255))

        # Get Center info
        background_center = (background.get_width() / 2, background.get_height() / 2)

        big_button_center = (big_button.get_width() / 2, big_button.get_height() / 2)
        small_button_center = (small_button.get_width() / 2, small_button.get_height() / 2)

        big_button_txt_1_center = (big_button_txt_1.get_width() / 2, big_button_txt_1.get_height() / 2)
        small_button_txt_1_center = (small_button_txt_1.get_width() / 2, small_button_txt_1.get_height() / 2)
        small_button_txt_2_center = (small_button_txt_2.get_width() / 2, small_button_txt_2.get_height() / 2)

        # Set pos Button
        big_button_pos = (1/2, 1/4)
        small_button_pos = ((1/2, 2/4), (1/2, 3/4))

        # Affichage
        self.screen.blit(background,(0,0)) 

        big_button_rect_1 = self.screen.blit(big_button, (int(self.screen.get_width()*big_button_pos[0]-big_button_center[0]), int(self.screen.get_height()*big_button_pos[1]-big_button_center[1])))
        small_button_rect_1 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[0][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[0][1]-small_button_center[1])))
        small_button_rect_2 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[1][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[1][1]-small_button_center[1])))

        self.screen.blit(big_button_txt_1, (int(self.screen.get_width()*big_button_pos[0]-big_button_txt_1_center[0]), int(self.screen.get_height()*big_button_pos[1]-big_button_txt_1_center[1])))
        self.screen.blit(small_button_txt_1, (int(self.screen.get_width()*small_button_pos[0][0]-small_button_txt_1_center[0]), int(self.screen.get_height()*small_button_pos[0][1]-small_button_txt_1_center[1])))
        self.screen.blit(small_button_txt_2, (int(self.screen.get_width()*small_button_pos[1][0]-small_button_txt_2_center[0]), int(self.screen.get_height()*small_button_pos[1][1]-small_button_txt_2_center[1])))

        pygame.display.flip()

        # Detect Click
        pygame.event.clear()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if big_button_rect_1.collidepoint(mouse_x,mouse_y):
                    print("Play")
                    break
                elif small_button_rect_1.collidepoint(mouse_x,mouse_y):
                    print("Setting")
                    self.Setting()
                    break
                elif small_button_rect_2.collidepoint(mouse_x,mouse_y):
                    print("Quit")
                    pygame.quit()
                    quit()
                else: 
                    print("Nothings")
            elif event.type == QUIT:
                pygame.quit()
                quit()

    def Setting(self):

        """
        big button : 1
        small button : 10
        """

        # Load Font
        big_button_font = pygame.font.Font("Project_Elastique/V.3/font/Arcade.ttf", 35)
        small_button_font = pygame.font.Font("font/Arcade.ttf", 25)

        # Load image or color
        background = pygame.image.load("texture/background.png").convert_alpha()
        big_button = pygame.image.load("texture/button.png").convert_alpha()
        small_button = pygame.image.load("texture/button.png").convert_alpha()

        # Coef resize for image
        coef = (self.screen.get_width()+self.screen.get_height())/(big_button.get_width()+big_button.get_height())
        big_button_coef = 1/4
        small_button_coef = 1/6

        # Resize img
        background =  pygame.transform.scale(background, (self.screen.get_width(),self.screen.get_height()))
        big_button = pygame.transform.scale(big_button, (int(big_button.get_width()*coef*big_button_coef), int(big_button.get_height()*coef*big_button_coef)))
        small_button = pygame.transform.scale(small_button, (int(small_button.get_width()*coef*small_button_coef), int(small_button.get_height()*coef*small_button_coef)))

        # Text render
        big_button_txt_1 = big_button_font.render('Back', True, (255,255,255))
        small_button_txt_1 = small_button_font.render('Set 1', True, (255,255,255))
        small_button_txt_2 = small_button_font.render('Set 2', True, (255,255,255))
        small_button_txt_3 = small_button_font.render('Set 3', True, (255,255,255))
        small_button_txt_4 = small_button_font.render('Set 4', True, (255,255,255))
        small_button_txt_5 = small_button_font.render('Set 5', True, (255,255,255))
        small_button_txt_6 = small_button_font.render('Set 6', True, (255,255,255))
        small_button_txt_7 = small_button_font.render('Set 7', True, (255,255,255))
        small_button_txt_8 = small_button_font.render('Set 8', True, (255,255,255))
        small_button_txt_9 = small_button_font.render('Set 9', True, (255,255,255))
        small_button_txt_10 = small_button_font.render('Set 10', True, (255,255,255))
        small_button_txt_11 = small_button_font.render('Set 11', True, (255,255,255))
        small_button_txt_12 = small_button_font.render('Set 12', True, (255,255,255))
        small_button_txt_13 = small_button_font.render('Set 13', True, (255,255,255))
        small_button_txt_14 = small_button_font.render('Set 14', True, (255,255,255))
        small_button_txt_15= small_button_font.render('Set 15', True, (255,255,255))

        # Get Center info
        background_center = (background.get_width() / 2, background.get_height() / 2)

        big_button_center = (big_button.get_width() / 2, big_button.get_height() / 2)
        small_button_center = (small_button.get_width() / 2, small_button.get_height() / 2)

        big_button_txt_1_center = (big_button_txt_1.get_width() / 2, big_button_txt_1.get_height() / 2)
        small_button_txt_1_center = (small_button_txt_1.get_width() / 2, small_button_txt_1.get_height() / 2)
        small_button_txt_2_center = (small_button_txt_2.get_width() / 2, small_button_txt_2.get_height() / 2)
        small_button_txt_3_center = (small_button_txt_3.get_width() / 2, small_button_txt_3.get_height() / 2)
        small_button_txt_4_center = (small_button_txt_4.get_width() / 2, small_button_txt_4.get_height() / 2)
        small_button_txt_5_center = (small_button_txt_1.get_width() / 2, small_button_txt_1.get_height() / 2)
        small_button_txt_6_center = (small_button_txt_2.get_width() / 2, small_button_txt_2.get_height() / 2)
        small_button_txt_7_center = (small_button_txt_3.get_width() / 2, small_button_txt_3.get_height() / 2)
        small_button_txt_8_center = (small_button_txt_4.get_width() / 2, small_button_txt_4.get_height() / 2)
        small_button_txt_9_center = (small_button_txt_1.get_width() / 2, small_button_txt_1.get_height() / 2)
        small_button_txt_10_center = (small_button_txt_2.get_width() / 2, small_button_txt_2.get_height() / 2)
        small_button_txt_11_center = (small_button_txt_2.get_width() / 2, small_button_txt_2.get_height() / 2)
        small_button_txt_12_center = (small_button_txt_3.get_width() / 2, small_button_txt_3.get_height() / 2)
        small_button_txt_13_center = (small_button_txt_4.get_width() / 2, small_button_txt_4.get_height() / 2)
        small_button_txt_14_center = (small_button_txt_1.get_width() / 2, small_button_txt_1.get_height() / 2)
        small_button_txt_15_center = (small_button_txt_2.get_width() / 2, small_button_txt_2.get_height() / 2)

        # Set pos Button
        big_button_pos = (1/2, 6/7)
        small_button_pos = ((1/4, 1/7), (1/4, 2/7), (1/4, 3/7), (1/4, 4/7), (1/4, 5/7), 
                            (2/4, 1/7), (2/4, 2/7), (2/4, 3/7), (2/4, 4/7), (2/4, 5/7),
                            (3/4, 1/7), (3/4, 2/7), (3/4, 3/7), (3/4, 4/7), (3/4, 5/7))

        # Affichage
        self.screen.blit(background,(0,0)) 

        big_button_rect_1 = self.screen.blit(big_button, (int(self.screen.get_width()*big_button_pos[0]-big_button_center[0]), int(self.screen.get_height()*big_button_pos[1]-big_button_center[1])))
        small_button_rect_1 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[0][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[0][1]-small_button_center[1])))
        small_button_rect_2 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[1][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[1][1]-small_button_center[1])))
        small_button_rect_3 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[2][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[2][1]-small_button_center[1])))
        small_button_rect_4 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[3][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[3][1]-small_button_center[1])))
        small_button_rect_5 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[4][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[4][1]-small_button_center[1])))
        small_button_rect_6 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[5][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[5][1]-small_button_center[1])))
        small_button_rect_7 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[6][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[6][1]-small_button_center[1])))
        small_button_rect_8 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[7][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[7][1]-small_button_center[1])))
        small_button_rect_9 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[8][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[8][1]-small_button_center[1])))
        small_button_rect_10 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[9][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[9][1]-small_button_center[1])))
        small_button_rect_11 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[10][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[10][1]-small_button_center[1])))
        small_button_rect_12 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[11][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[11][1]-small_button_center[1])))
        small_button_rect_13 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[12][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[12][1]-small_button_center[1])))
        small_button_rect_14 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[13][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[13][1]-small_button_center[1])))
        small_button_rect_15 = self.screen.blit(small_button, (int(self.screen.get_width()*small_button_pos[14][0]-small_button_center[0]), int(self.screen.get_height()*small_button_pos[14][1]-small_button_center[1])))

        self.screen.blit(big_button_txt_1, (int(self.screen.get_width()*big_button_pos[0]-big_button_txt_1_center[0]), int(self.screen.get_height()*big_button_pos[1]-big_button_txt_1_center[1])))
        self.screen.blit(small_button_txt_1, (int(self.screen.get_width()*small_button_pos[0][0]-small_button_txt_1_center[0]), int(self.screen.get_height()*small_button_pos[0][1]-small_button_txt_1_center[1])))
        self.screen.blit(small_button_txt_2, (int(self.screen.get_width()*small_button_pos[1][0]-small_button_txt_2_center[0]), int(self.screen.get_height()*small_button_pos[1][1]-small_button_txt_2_center[1])))
        self.screen.blit(small_button_txt_3, (int(self.screen.get_width()*small_button_pos[2][0]-small_button_txt_3_center[0]), int(self.screen.get_height()*small_button_pos[2][1]-small_button_txt_3_center[1])))
        self.screen.blit(small_button_txt_4, (int(self.screen.get_width()*small_button_pos[3][0]-small_button_txt_4_center[0]), int(self.screen.get_height()*small_button_pos[3][1]-small_button_txt_4_center[1])))
        self.screen.blit(small_button_txt_5, (int(self.screen.get_width()*small_button_pos[4][0]-small_button_txt_5_center[0]), int(self.screen.get_height()*small_button_pos[4][1]-small_button_txt_5_center[1])))
        self.screen.blit(small_button_txt_6, (int(self.screen.get_width()*small_button_pos[5][0]-small_button_txt_6_center[0]), int(self.screen.get_height()*small_button_pos[5][1]-small_button_txt_6_center[1])))
        self.screen.blit(small_button_txt_7, (int(self.screen.get_width()*small_button_pos[6][0]-small_button_txt_7_center[0]), int(self.screen.get_height()*small_button_pos[6][1]-small_button_txt_7_center[1])))
        self.screen.blit(small_button_txt_8, (int(self.screen.get_width()*small_button_pos[7][0]-small_button_txt_8_center[0]), int(self.screen.get_height()*small_button_pos[7][1]-small_button_txt_8_center[1])))
        self.screen.blit(small_button_txt_9, (int(self.screen.get_width()*small_button_pos[8][0]-small_button_txt_9_center[0]), int(self.screen.get_height()*small_button_pos[8][1]-small_button_txt_9_center[1])))
        self.screen.blit(small_button_txt_10, (int(self.screen.get_width()*small_button_pos[9][0]-small_button_txt_10_center[0]), int(self.screen.get_height()*small_button_pos[9][1]-small_button_txt_10_center[1])))
        self.screen.blit(small_button_txt_11, (int(self.screen.get_width()*small_button_pos[10][0]-small_button_txt_11_center[0]), int(self.screen.get_height()*small_button_pos[10][1]-small_button_txt_6_center[1])))
        self.screen.blit(small_button_txt_12, (int(self.screen.get_width()*small_button_pos[11][0]-small_button_txt_12_center[0]), int(self.screen.get_height()*small_button_pos[11][1]-small_button_txt_7_center[1])))
        self.screen.blit(small_button_txt_13, (int(self.screen.get_width()*small_button_pos[12][0]-small_button_txt_13_center[0]), int(self.screen.get_height()*small_button_pos[12][1]-small_button_txt_8_center[1])))
        self.screen.blit(small_button_txt_14, (int(self.screen.get_width()*small_button_pos[13][0]-small_button_txt_14_center[0]), int(self.screen.get_height()*small_button_pos[13][1]-small_button_txt_9_center[1])))
        self.screen.blit(small_button_txt_15, (int(self.screen.get_width()*small_button_pos[14][0]-small_button_txt_15_center[0]), int(self.screen.get_height()*small_button_pos[14][1]-small_button_txt_10_center[1])))

        pygame.display.flip()

        # Detect Click
        pygame.event.clear()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if big_button_rect_1.collidepoint(mouse_x,mouse_y):
                    print("Back")
                    self.Menu()
                    break
                elif small_button_rect_1.collidepoint(mouse_x,mouse_y):
                    print("Set 1")
                elif small_button_rect_2.collidepoint(mouse_x,mouse_y):
                    print("Set 2")
                elif small_button_rect_3.collidepoint(mouse_x,mouse_y):
                    print("Set 3")
                elif small_button_rect_4.collidepoint(mouse_x,mouse_y):
                    print("Set 4")
                elif small_button_rect_5.collidepoint(mouse_x,mouse_y):
                    print("Set 5")
                elif small_button_rect_6.collidepoint(mouse_x,mouse_y):
                    print("Set 6")
                elif small_button_rect_7.collidepoint(mouse_x,mouse_y):
                    print("Set 7")
                elif small_button_rect_8.collidepoint(mouse_x,mouse_y):
                    print("Set 8")
                elif small_button_rect_9.collidepoint(mouse_x,mouse_y):
                    print("Set 9")
                elif small_button_rect_10.collidepoint(mouse_x,mouse_y):
                    print("Set 10")
                elif small_button_rect_11.collidepoint(mouse_x,mouse_y):
                    print("Set 11")
                elif small_button_rect_12.collidepoint(mouse_x,mouse_y):
                    print("Set 12")
                elif small_button_rect_13.collidepoint(mouse_x,mouse_y):
                    print("Set 13")
                elif small_button_rect_14.collidepoint(mouse_x,mouse_y):
                    print("Set 14")
                elif small_button_rect_15.collidepoint(mouse_x,mouse_y):
                    print("Set 15")
                else: 
                    print("Nothings")
            elif event.type == QUIT:
                break