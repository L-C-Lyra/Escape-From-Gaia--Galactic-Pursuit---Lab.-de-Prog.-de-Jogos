from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.keyboard import *
from PPlay.mouse import *
import main_menu

def main():
    game_window = Window(1024, 1024)

    game_background = GameImage("./src/assets/game_background.png")

    game_keyboard = game_window.get_keyboard()
    game_mouse = game_window.get_mouse()

    game_window.set_title("Escape From Gaia - Galactic Pursuit")

    game_title = Sprite("./src/assets/game_title.png")
    game_title.set_position((game_window.width - game_title.width) / 2, (game_window.height - game_title.height) / 6)

    press_space = Animation("./src/assets/press_space_sequence.png", 6, loop=True)
    press_space.set_position((game_window.width - press_space.width) / 2, (game_window.height - press_space.height) / 2)

    press_space.set_total_duration(200)
    press_space.set_sequence(0, 6, loop=True)

    press_space_background = GameImage("./src/assets/press_space_background.png")

    while True:
        if(game_keyboard.key_pressed("SPACE")):
            main_menu.main(game_window, game_background, game_keyboard, game_mouse)
        if(game_keyboard.key_pressed("ESC")):
            game_window.close()
        
        game_background.draw()
        
        game_title.draw()
        press_space_background.draw()
        press_space.play()
        press_space.draw()
        
        game_window.update()
        press_space.update()


if __name__ == "__main__":
    main()