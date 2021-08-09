# Hangman
This project contains Hangman game code. Below is game flow:
- Click on run.bat file -> Console screen will open
- Input your name -> Puzzle information will be displayed
- Guess the character, based on hint -> you will have 6 chances to guess wrong character
- If you win 10 points will be awarded, if you loose no points will be given
- Once puzzle is over, screen will ask if you want to play more -> choose the option and enjoy
- Screen will also display the scoreboard in which players rank will display, when you win or loose

#### *Two players can play the game at same time and with same name, as game statistics is stored based on each game played.

# Project Structure
Hangman<br>
   ├── common<br>
   │   ├── dbconnect.py<br>
   │   └── secret.py<br>
   ├── game<br>
   │   ├── hangman.py<br>
   │   └── __init__.py<br>
   ├── data<br>
   │   ├── game.db<br>
   │   └── hangman_puzzle.csv<br>
   ├── secret<br>
   │   └── secret.key<br>
   ├── requirement.txt<br>
   ├── game.py<br>
   ├── run.bat<br>
   └── readme.md<br>
   
 # /common/dbconnect.py
 This file provides api to connect with sqlite database to expose hangman backend tables for CRUD operations.
 - <b>connect_to_game_db:</b> function will connect to game database /data/game.db and return cursor and connection for further operations
 - <b>close_connection:</b> function will close connection with database
 - <b>create_hangman_tables:</b> function will create tables in database. It should be run by admin for game setup only once.
 - <b>insert_player_name:</b> function will insert player name into database and return player_id for same. It will also insert inital score for player in database.
 - <b>update_player_score:</b> function will update player score in database. It can be used to write score of player on each win.
 - <b>get_players_dashboard:</b> function will return top players statistics in pandas dataframe. By default, it will return top 10 players
 - <b>reset_database_tables:</b> function will drop database tables and recreate all of them. It will remove players and puzzle information from database
 - <b>load_hangman_puzzle:</b> function will load /data/hangman_puzzle.csv file into sqlite database
 
 # /common/secret.py
 This file provide encryption and decryption functionality to store and read data.
 - <b>generate_key:</b> function will generate secret key and store the same in /secret/secret.key
 - <b>load_key:</b> function will load key form /secret/secret.key
 - <b>encrypt_message:</b> function will encrypt message based on key and return the encrypted message
 - <b>decrypt_message:</b> function will decrypt message based on key and return the original message
 
 # /game/hangman.py
 This file will provide Hangman game class and its methods for game functionality. It can be initiated for each player and help us to run games in parallel as every new player will be working on its own object.
 Class will use dbconnect module to enable database operations. Below are the class methods available for usage:
 - <b>set_player_name:</b> function will set player name and insert the same into database. It will also initialize player_id which will be set to track each individual player game.
 - <b>__save_winner_point__:</b> function will connect with database and update points on correct puzzle
 - <b>get_puzzle:</b> function will connect with database and return new puzzle and hint for same
 - <b>__validate_player_choice__:</b> function will validate if player has guessed the right letter and return the remaining puzzle 
 - <b>check_choice:</b> function will initialise message for player for next action and validate current choice
 - <b>get_player_board:</b> function will get top player stats from database
 - <b>__get_screen_puzzle__:</b> function will check current puzzle and return masked screen version for display
 - <b>clean_up:</b> function will close database connection and can be extended for any garbage collection task in future
 
 # /game.py
 This file will orchestrate game flow on console. It is a front end controller for game on console. 
 File will initialize Hangman class for each player and run the game flow for user input and class methods.
 - <b>hangman_puzzle:</b> function will run loop to process puzzle and orchestrate puzzle flow for user guess. Function will only exit once user choose to not to play further
 - <b>player_choice:</b> function will ask for user choice and map it to orchestration flow for next action
 
 # /data/game.db
 This is a sqlite database which will work as storage technology for Hangman game. It has three tables for data storage and track player games statistics.
 - <b>hangman_puzzles:</b> table will hold puzzle hint and encrypted solution
 - <b>hangman_players:</b> table will hold player names and player id to track each unique player game.
 - <b>hangman_players_score:</b> table will hold score of each player game
 
 # /data/hangman_puzzle.csv
 This is template file to load hint and puzzle into database. Current game.db has 119 entries and file has been kept empty to avoid leaking answers
 
 # /secret/secret.key
 This file will hold secret key which can be used to decrypt information. Key will change every time you refresh puzzle data in database with dbconnect.load_hangman_puzzle api

# /run.bat
This is a batch file to trigger game.py with no hassle. It will call game.py programme present in same directory.

# /requirement.txt
This file contains version of package required to create python environment. However, a standard Anaconda python setup will have all dependent packages installed.
 
