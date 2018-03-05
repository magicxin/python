import pygame
from settings import Settings
import game_function as gf
from ship import Ship
#初始化，并创建一个屏幕
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建飞船
    ship = Ship(screen)
    #设置背景颜色
    #bg_color = (230,230,230)
    #监听键盘鼠标事件
    while True:
        gf.check_events(ship)
        ship.update()
        #让最近绘制的屏幕可见
        gf.update_screen(ai_settings,screen,ship)
run_game()