from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.mouse import *
import start_menu
import main_menu
import play_menu

def main(game_window, game_keyboard, game_mouse, difficulty_value, game_mode_value):
    game_background = GameImage("./src/assets/game_menu/game_background.png")

    nova_ryder = Sprite("./src/assets/game_menu/nova_ryder.png")
    nova_ryder.set_position((game_window.width / 2) - (nova_ryder.width / 2), ((game_window.height / 2) - (nova_ryder.height / 2)) * 1.90)

    vel_x = 250.0
    vel_y = 250.0

    while True:
        if(game_keyboard.key_pressed("ESC")):
            game_window.close()
        
        game_background.draw()

        nova_ryder.draw()

        if(nova_ryder.x > 0):
            if(game_keyboard.key_pressed("LEFT") or game_keyboard.key_pressed("A")):
                nova_ryder.x -= vel_x * game_window.delta_time()
        if(nova_ryder.x < (game_window.width - nova_ryder.width)):
            if(game_keyboard.key_pressed("RIGHT") or game_keyboard.key_pressed("D")):
                nova_ryder.x += vel_x * game_window.delta_time()
        if(nova_ryder.y >= 0 and nova_ryder.y >= (game_window.height / 2)):
            if(game_keyboard.key_pressed("UP") or game_keyboard.key_pressed("W")):
                nova_ryder.y -= vel_y * game_window.delta_time()
        if(nova_ryder.y <= (game_window.height - nova_ryder.height)):
            if(game_keyboard.key_pressed("DOWN") or game_keyboard.key_pressed("S")):
                nova_ryder.y += vel_y * game_window.delta_time()
        
        
        game_window.update()


if __name__ == "__main__":
    main()