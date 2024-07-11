from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.mouse import *
import main_menu

def main(game_window, game_background, game_keyboard, game_mouse):
    play_title = Sprite("./src/assets/play_title.png")
    play_title.set_position((game_window.width - play_title.width) / 2, (game_window.height - play_title.height) / 8)

    difficulty_title = Sprite("./src/assets/difficulty_title.png")
    difficulty_title.set_position((game_window.width - difficulty_title.width) / 2, (game_window.height - difficulty_title.height) / 2.5)

    easy = Sprite("./src/assets/buttons/easy.png")
    easy.set_position((game_window.width - easy.width) / 9, (game_window.height - easy.height) / 2)
    easy_selected = Sprite("./src/assets/buttons/easy_selected.png")
    easy_selected.set_position((game_window.width - easy_selected.width) / 9, (game_window.height - easy_selected.height) / 2)
    selected_easy = False

    medium = Sprite("./src/assets/buttons/medium.png")
    medium.set_position((game_window.width - medium.width) / 2, (game_window.height - medium.height) / 2)
    medium_selected = Sprite("./src/assets/buttons/medium_selected.png")
    medium_selected.set_position((game_window.width - medium_selected.width) / 2, (game_window.height - medium_selected.height) / 2)
    selected_medium = False

    hard = Sprite("./src/assets/buttons/hard.png")
    hard.set_position(((game_window.width - hard.width) / 9) * 8, (game_window.height - hard.height) / 2)
    hard_selected = Sprite("./src/assets/buttons/hard_selected.png")
    hard_selected.set_position(((game_window.width - hard_selected.width) / 9) * 8, (game_window.height - hard_selected.height) / 2)
    selected_hard = False

    game_mode_title = Sprite("./src/assets/game_mode_title.png")
    game_mode_title.set_position((game_window.width - game_mode_title.width) / 2, (game_window.height - game_mode_title.height) / 1.65)

    arcade = Sprite("./src/assets/buttons/arcade.png")
    arcade.set_position((game_window.width - arcade.width) / 6, (game_window.height - arcade.height) / 1.4)
    arcade_selected = Sprite("./src/assets/buttons/arcade_selected.png")
    arcade_selected.set_position((game_window.width - arcade_selected.width) / 6, (game_window.height - arcade_selected.height) / 1.4)
    selected_arcade = False

    endless = Sprite("./src/assets/buttons/endless.png")
    endless.set_position(((game_window.width - endless.width) / 6) * 5, (game_window.height - endless.height) / 1.4)
    endless_selected = Sprite("./src/assets/buttons/endless_selected.png")
    endless_selected.set_position(((game_window.width - endless_selected.width) / 6) * 5, (game_window.height - endless_selected.height) / 1.4)
    selected_endless = False

    back = Sprite("./src/assets/buttons/back.png")
    back.set_position((game_window.width - back.width) / 10, (game_window.height - back.height) / 1.1)
    back_selected = Sprite("./src/assets/buttons/back_selected.png")
    back_selected.set_position((game_window.width - back_selected.width) / 10, (game_window.height - back_selected.height) / 1.1)

    run = Sprite("./src/assets/buttons/run.png")
    run.set_position(((game_window.width - run.width) / 10) * 9, (game_window.height - run.height) / 1.1)
    run_selected = Sprite("./src/assets/buttons/run_selected.png")
    run_selected.set_position(((game_window.width - run_selected.width) / 10) * 9, (game_window.height - run_selected.height) / 1.1)

    difficulty_value = 0
    game_mode_value = 0

    while True:
        if(game_keyboard.key_pressed("ESC")):
            main_menu.main(game_window, game_background, game_keyboard, game_mouse)
        
        game_background.draw()

        play_title.draw()
        difficulty_title.draw()
        easy_selected.draw()
        easy.draw()
        medium_selected.draw()
        medium.draw()
        hard_selected.draw()
        hard.draw()
        game_mode_title.draw()
        arcade_selected.draw()
        arcade.draw()
        endless_selected.draw()
        endless.draw()
        back_selected.draw()
        back.draw()
        run_selected.draw()
        run.draw()

        if(not game_mouse.is_over_object(easy) and (not selected_easy)):
            easy.unhide()
            easy_selected.hide()
        else:
            easy.hide()
            easy_selected.unhide()
            if(game_mouse.is_button_pressed(1)):
                easy.hide()
                easy_selected.unhide()
                selected_easy = True
                selected_medium = False
                selected_hard = False
                difficulty_value = 1
        if(not game_mouse.is_over_object(medium) and (not selected_medium)):
            medium.unhide()
            medium_selected.hide()
        else:
            medium.hide()
            medium_selected.unhide()
            if(game_mouse.is_button_pressed(1)):
                medium.hide()
                medium_selected.unhide()
                selected_easy = False
                selected_medium = True
                selected_hard = False
                difficulty_value = 2
        if(not game_mouse.is_over_object(hard) and (not selected_hard)):
            hard.unhide()
            hard_selected.hide()
        else:
            hard.hide()
            hard_selected.unhide()
            if(game_mouse.is_button_pressed(1)):
                hard.hide()
                hard_selected.unhide()
                selected_easy = False
                selected_medium = False
                selected_hard = True
                difficulty_value = 3
        if(not game_mouse.is_over_object(arcade) and (not selected_arcade)):
            arcade.unhide()
            arcade_selected.hide()
        else:
            arcade.hide()
            arcade_selected.unhide()
            if(game_mouse.is_button_pressed(1)):
                arcade.hide()
                arcade_selected.unhide()
                selected_arcade = True
                selected_endless = False
                game_mode_value = 0
        if(not game_mouse.is_over_object(endless) and (not selected_endless)):
            endless.unhide()
            endless_selected.hide()
        else:
            endless.hide()
            endless_selected.unhide()
            if(game_mouse.is_button_pressed(1)):
                endless.hide()
                endless_selected.unhide()
                selected_arcade = False
                selected_endless = True
                game_mode_value = 1
        if(not game_mouse.is_over_object(back)):
            back.unhide()
            back_selected.hide()
        else:
            back.hide()
            back_selected.unhide()
            if(game_mouse.is_button_pressed(1)):
                main_menu.main(game_window, game_background, game_keyboard, game_mouse)
        if(not game_mouse.is_over_object(run)):
            run.unhide()
            run_selected.hide()
        else:
            run.hide()
            run_selected.unhide()
            if(game_mouse.is_button_pressed(1)):
                pass

        game_window.update()


if __name__ == "__main__":
    main()