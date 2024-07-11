from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.mouse import *
import start_menu
import play_menu

def main(game_window, game_background, game_keyboard, game_mouse):
    game_title = Sprite("./src/assets/game_title.png")
    game_title.set_position((game_window.width - game_title.width) / 2, (game_window.height - game_title.height) / 6)

    new_game = Sprite("./src/assets/buttons/new_game.png")
    new_game.set_position((game_window.width - new_game.width) / 2, (game_window.height - new_game.height) / 2)
    new_game_selected = Sprite("./src/assets/buttons/new_game_selected.png")
    new_game_selected.set_position((game_window.width - new_game_selected.width) / 2, (game_window.height - new_game_selected.height) / 2)

    settings = Sprite("./src/assets/buttons/settings.png")
    settings.set_position((game_window.width - settings.width) / 2, (game_window.height - settings.height) / 1.5)
    settings_selected = Sprite("./src/assets/buttons/settings_selected.png")
    settings_selected.set_position((game_window.width - settings_selected.width) / 2, (game_window.height - settings_selected.height) / 1.5)

    exit = Sprite("./src/assets/buttons/exit.png")
    exit.set_position((game_window.width - exit.width) / 2, (game_window.height - exit.height) / 1.2)
    exit_selected = Sprite("./src/assets/buttons/exit_selected.png")
    exit_selected.set_position((game_window.width - exit_selected.width) / 2, (game_window.height - exit_selected.height) / 1.2)

    while True:
        game_background.draw()
        
        game_title.draw()
        new_game_selected.draw()
        new_game.draw()
        settings_selected.draw()
        settings.draw()
        exit_selected.draw()
        exit.draw()

        if(not game_mouse.is_over_object(new_game)):
            new_game.unhide()
            new_game_selected.hide()
        else:
            new_game.hide()
            new_game_selected.unhide()
            if(game_mouse.is_button_pressed(1)):
                play_menu.main(game_window, game_background, game_keyboard, game_mouse)
        if(not game_mouse.is_over_object(settings)):
            settings.unhide()
            settings_selected.hide()
        else:
            settings.hide()
            settings_selected.unhide()
            if(game_mouse.is_button_pressed(1)):
                pass
        if(not game_mouse.is_over_object(exit)):
            exit.unhide()
            exit_selected.hide()
        else:
            exit.hide()
            exit_selected.unhide()
            if(game_mouse.is_button_pressed(1)):
                game_window.close()
        
        game_window.update()


if __name__ == "__main__":
    main()