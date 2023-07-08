import pygame
from settings import *

class UI:
    def __init__(self, surface) -> None:
        
        #setup
        self.display_surface = surface
        
        #health
        self.health_bar = pygame.image.load(".//JUEGO 2//graphics//ui//health_bar.png").convert_alpha()
        self.health_bar_topleft = (54,39)
        self.bar_max_width = 152
        self.bar_heigth = 4
        
        #coins
        self.coin = pygame.image.load(".//JUEGO 2//graphics//ui//coin.png").convert_alpha()
        self.coin_rect = self.coin.get_rect(topleft = (50,61))
        
        self.font = pygame.font.Font(".//JUEGO 2//graphics//ui//ARCADEPI.TTF", 30)
        
        
        
    def show_health(self, current_health, max_health):
        self.display_surface.blit(self.health_bar, (20,10))
        current_health_ratio = current_health / max_health
        
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect((self.health_bar_topleft), (current_bar_width,self.bar_heigth))
        pygame.draw.rect(self.display_surface, C_DEEP_RED, health_bar_rect)
        
    def show_coins(self, amount):
        self.display_surface.blit(self.coin, self.coin_rect)
        coin_amount_surface = self.font.render(str(amount), False, C_PURPLE)
        coin_amount_rect = coin_amount_surface.get_rect(midleft = (self.coin_rect.right + 4,self.coin_rect.centery))
        self.display_surface.blit(coin_amount_surface, coin_amount_rect)