#import libraries
import game.hangman as gh

def hangman_puzzle(obj_game, play_status):
    screen_word, puzzle_hint = obj_game.get_puzzle()
    in_play = play_status
    while in_play == 1:
        # Show puzzle
        print()
        print('Hint for puzzle word is: ', puzzle_hint, '                          ', 'Length of puzzle word is: ', len(screen_word))
        print()
        print(screen_word)
        # prompt for guess character
        guess_char = input ('Please enter an alphabet to guess the puzzle letters: ')
        screen_message, screen_word, in_play = obj_game.check_choice(guess_char)
        print(screen_message)
        if in_play == 2:  # puzzle solved, display result and dashboard
            print (screen_word)
            print('Your total points: ',obj_game.player_point)
            print('Top players after your win')
            print(obj_game.get_player_board())
            in_play = 1  # set for next puzzle
            screen_word, puzzle_hint = obj_game.get_puzzle()
        elif in_play == 0:
            print (screen_word)
            print (obj_game.get_player_board ())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # initialise hangman game class for player
    game = gh.hangman()
    # welcome message
    print ('Welcome to the Hangman')
    # prompt player name on screen
    player_name = input ('Please enter your name:  ')
    # set player name for game play
    game.set_player_name (player_name)
    try:
        hangman_puzzle (game, 1)  # pass 1 to start game first time
    except KeyboardInterrupt:
        game.clean_up()
    print ('Bye Bye')



