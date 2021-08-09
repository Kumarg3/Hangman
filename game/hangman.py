"""This module is built to create hangman game class,
class can be initialised with parameter to create own game version """

# import libraries
from common import dbconnect
from common import secret


class Hangman:

    def __init__(self, wrong_choice_counter=6, winner_point=10):
        """Initialise parameter in constructor for each game
            player_guess_counter: number of choices that can be wrong during word guess, reset counter at each puzzle
            winner_point: point to award if player guesses the right word
            player_guess_list: list of letters guessed by player
            player_point: number of points for player during game
            in_play: 1 if game is playing, 0 if player lost, 2 for next puzzle
            key: key to display puzzle solution
        """
        self.player_name = ''  # default value, will not be used
        self.player_id = -1  # default value, will not be used
        self.player_guess_counter = wrong_choice_counter
        self.winner_point = winner_point
        self.player_point = 0
        self.player_guess_list = []
        self.in_play = 1
        self.cur, self.con = dbconnect.connect_to_game_db()
        self.key = secret.load_key()

    def set_player_name(self, player_name='Unknown Player'):
        """function will set player name and update database"""
        self.player_name = player_name
        # connect to database and update database with player name and return player id
        self.player_id = dbconnect.insert_player_name(self.cur, self.con, self.player_name)

    def __get_player_name__(self):
        """function will return player name for current player"""
        return self.player_name

    def __reset_number_of_wrong_choices__(self, wrong_choice_counter):
        """function will reset number of wrong choices during game"""
        self.wrong_choice_counter = wrong_choice_counter

    def __get_number_of_wrong_choices__(self):
        """function will return number of wrong choices left"""
        return self.wrong_choice_counter

    def __save_winner_point__(self):
        """function will save player point in database and return updated point for player"""
        self.player_point = self.player_point + self.winner_point
        # update player point in database
        dbconnect.update_player_score(self.cur, self.con, self.player_id, self.player_point)
        self.in_play = 2

    def get_puzzle(self):
        """function will get puzzle and hint for same from database"""
        puzzle = dbconnect.get_puzzle(self.cur)
        self.puzzle_word = secret.decrypt_message(puzzle[1], self.key)
        self.puzzle_word_index = {index: True if word == ' ' else False for index, word in enumerate(self.puzzle_word)}
        self.puzzle_hint = puzzle[0]
        screen_word = self.__get_screen_puzzle__()
        self.wrong_choice_counter = self.player_guess_counter  # counter to track number of wrong guess by player
        self.player_guess_list = []  # reset player guess list at each new puzzle
        self.in_play = 1  # set to 1 to set status in play
        return screen_word, self.puzzle_hint

    def __validate_player_choice__(self, player_guess_word):
        """function will validate if player guess is correct"""
        if player_guess_word in self.puzzle_word:
            self.puzzle_word_index = {key: True if self.puzzle_word[key] == player_guess_word else value for key, value in self.puzzle_word_index.items()}
            # increase the points if puzzle is completed and reset the wrong choices and get new puzzle
            screen_word = self.__get_screen_puzzle__()
            if '*' in screen_word:  # more word needs to be guessed
                pass
            else:
                self.__save_winner_point__()
        else:
            self.wrong_choice_counter = self.wrong_choice_counter - 1
            if self.wrong_choice_counter == 0:  # game over, Player lost
                self.in_play = 0  # no more puzzle display once it is set to 0
                self.puzzle_word_index = {key: True for key, value in self.puzzle_word_index.items()}
            else:
                pass

    def check_choice(self, player_guess_word):
        """function will check if player choice is valid"""
        if player_guess_word in self.player_guess_list:
            message = 'Please choose another character, You have already guessed this letter'
        elif len(player_guess_word) != 1:
            message = 'Please enter only one character'
        elif player_guess_word.isalpha():
            self.player_guess_list.append(player_guess_word)
            self.__validate_player_choice__(player_guess_word)
            if self.in_play == 0:
                message = 'You tried well, No more guess left, Here is the solution'
            elif self.in_play == 2:
                message = 'Well done, You are a star '+self.player_name
            else:
                message = 'Keep Going'
        else:
            message = 'Please enter characters only'
        screen_word = self.__get_screen_puzzle__()
        return message, screen_word, self.in_play

    def get_player_board(self):
        """function will get top 10 player based on points from database"""
        return dbconnect.get_players_dashboard(self.con)

    def __get_screen_puzzle__(self):
        """function will return the word to display on console screen"""
        word = [self.puzzle_word[key] if value else '*' for (key, value) in self.puzzle_word_index.items()]
        return ''.join(word)

    def clean_up(self):
        """function will close db connection, any further activity can be added if required"""
        dbconnect.close_connection(self.cur, self.con)