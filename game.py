#!/usr/bin/python

# import libraries
import game.hangman as gh


def hangman_puzzle(obj_game, play_status):
    screen_word, puzzle_hint = obj_game.get_puzzle()
    in_play = play_status
    while in_play == 1:
        # Show puzzle
        print('\nHint for puzzle word is: ', puzzle_hint, '                          ', 'Length of puzzle word is: ', len(screen_word),  '                          ', 'Number of wrong guesses left: ', obj_game.wrong_choice_counter,'\n')
        print(screen_word)
        # prompt for guess character
        guess_char = input('\nPlease enter an alphabet to guess the puzzle letters: ')
        screen_message, screen_word, in_play = obj_game.check_choice(guess_char.upper())
        print(screen_message)
        if in_play == 2:  # puzzle solved, display result and dashboard
            print(screen_word)
            print('\nYour total points: ', obj_game.player_point)
            print(obj_game.get_player_board())
            in_play = player_choice()  # set for next puzzle
            screen_word, puzzle_hint = obj_game.get_puzzle()
        elif in_play == 0:
            print(screen_word)
            print ('\nYour total points: ', obj_game.player_point)
            print(obj_game.get_player_board())
            in_play = player_choice()  # set for next puzzle
            screen_word, puzzle_hint = obj_game.get_puzzle()


def player_choice():
    """function will ask for player choice to play next game and return 1 for more puzzle and 0 to stop"""
    game_play = input('\n Do you want to play next puzzle, enter Y to continue or press any key to exit game: ')
    if game_play.upper() == 'Y':
        in_play = 1
    else:
        in_play = 0
    return in_play


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # initialise hangman game class for player
    game = gh.Hangman()
    # welcome message
    print('Welcome to the Hangman\n')
    # prompt player name on screen
    player_name = input('Please enter your name:  ') or 'Unknown Player'
    # set player name for game play
    game.set_player_name(player_name)
    game_play = 1
    try:
        hangman_puzzle(game, game_play)  # pass 1 to start game first time
    except KeyboardInterrupt:
        print('\nThanks for playing, Exiting Now..')
    game.clean_up()
    print('\nThanks for playing the game \n\nBye Bye')
