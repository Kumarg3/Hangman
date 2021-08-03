'''This module is built to create hangman game class,
class can be initialised with parameter to create own game version '''

class hangman:

    def __init__(self, wrong_choice_counter=5,winner_point=10):
        '''Initialise parameter in constructor for each game
            wrong_choice_counter: number of choices that can be wrong while guessing a letter
            winner_point: point to award if player guesses the right word
            player_guess_list: list of letters guessed by player
            player_point: number of points for player during game
        '''
        self.wrong_choice_counter = wrong_choice_counter
        self.winner_point = winner_point
        self.player_guess_list = []
        self.player_point = 0

    def __doc__(self):
        '''This module is built to create hangman game class,
        class can be initialised with parameter to create own game version '''

    def __set_player_name__(self,player_name):
        '''function will set player name and update database'''
        self.player_name = player_name
        #connect to database and update database with player name and return player id
        #self.player_id =

    def __get_player_name__(self):
        '''function will return player name for current player'''
        return self.player_name

    def __reset_number_of_wrong_choices__(self,wrong_choice_counter):
        '''function will reset number of wrong choices during game'''
        self.wrong_choice_counter = wrong_choice_counter

    @property
    def __get_number_of_wrong_choices__(self):
        '''function will return number of wrong choices left'''
        return self.wrong_choice_counter

    def __save_winner_point__(self,player_point):
        '''function will save player point in database and return updated point for player'''
        self.player_point = self.player_point + player_point
        #update player point in database
        return self.player_point

    def __get_puzzle__(self):
        '''function will get puzzle and hint for same from database'''
        self.puzzle_word = ''
        self.puzzle_hint = ''

    def __validate_player_choice__(self, player_guess_word):
        '''function will validate if player guess is correct'''
        if player_guess_word in self.puzzle_word:
            self.puzzle_word = {key: True if key == player_guess_word else value for key, value in self.puzzle_word }
            # increase the points if puzzle is completed and reset the wrong choices and get new puzzle
        else:
            self.wrong_choice_counter = self.wrong_choice_counter + 1

    def __check_choice__(self,player_guess_word):
        '''function will check if player choice is valid'''
        if player_guess_word in self.player_guess_list:
            message = 'Please choose another word, You have already guessed this one'
        elif player_guess_word.isalpha():
            self.__validate_player_choice__ (self, player_guess_word)
            message = 'Good Job'
        else:
            message = 'Please enter characters only'
        return message, self.puzzle_word

    def __get_palyer_board__(self):
        '''function will get top 10 player based on points from database'''