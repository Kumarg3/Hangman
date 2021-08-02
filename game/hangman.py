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

    def __get_number_of_wrong_choices__(self):
        '''function will return number of wrong choices left'''
        return self.wrong_choice_counter

    def __save_winner_point__(self,player_point):
        '''function will save player point in database and return updated point for player'''
        self.player_point = self.player_point + player_point
        #update player point in database
        return self.player_point