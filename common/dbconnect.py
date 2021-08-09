# import library
import sqlite3
# importing only required function to boost performance and optimise memory utilisation
from pandas import read_sql, read_csv
import secret


def connect_to_game_db():
    """this function will connect to sqlite database game and return cursor to execute queries"""
    con = sqlite3.connect('./data/game.db')
    cur = con.cursor()
    return cur, con


def close_connection(cur, con):
    """this function will close connection to database"""
    cur.close()
    con.close()


def create_hangman_tables(cur):
    """this function will be executed by admin user first time while setting up hangman game"""
    # hangman_player table will keep the record for each player name whoever played games
    qry_table1 = 'create table hangman_players ' \
                 '(PLAYER_ID INTEGER PRIMARY KEY AUTOINCREMENT, ' \
                 'PLAYER_NAME TEXT NOT NULL)'
    # hangman_players_score table will keep the core for player
    qry_table2 = 'create table hangman_players_score ' \
                 '(PLAYER_ID INTEGER, ' \
                 'PLAYER_SCORE INTEGER)'
    # hangman_puzzle table will keep hint and solution for puzzle
    qry_table3 = 'create table hangman_puzzles ' \
                 '(PUZZLE_HINT TEXT NOT NULL, ' \
                 'PUZZLE_SOLUTION TEXT PRIMARY KEY)'
    # this game will keep score at game level for each player 
    # and if same player plays again, it will be considered a new player
    # create table
    cur.execute(qry_table1)
    cur.execute(qry_table2)
    cur.execute(qry_table3)


def insert_player_name(cur, con, player_name='Unknown Player'):
    """this function will run query in game database"""
    cur.execute("insert into hangman_players(player_name) values(?)", [player_name])
    cur.execute("select max(player_id) from hangman_players")
    player_id = cur.fetchone()[0]
    player_score = 0  # player score will be 0 as player is just starting the game
    cur.execute("insert into hangman_players_score(player_id, player_score) values(?, ?)", [player_id, player_score])
    con.commit()
    return player_id


def update_player_score(cur, con, player_id, player_score):
    """this function will update player score in hangman_players_score table"""
    cur.execute("update hangman_players_score set player_score =(?) where player_id =(?)",
                [player_score, player_id])
    con.commit()


def get_players_dashboard(con, top_rank=10):
    """function will return top ranking players based on their score"""
    qry = "select hangman_players.player_name as 'PlayerName', hangman_players_score.player_score as 'Score'" \
          "from hangman_players, hangman_players_score " \
          "where hangman_players.player_id = hangman_players_score.player_id " \
          "order by hangman_players_score.player_score desc, hangman_players_score.player_id asc " \
          "limit ?"
    df_qry_result_dataframe = read_sql(qry, params=[top_rank], con=con)
    df_qry_result_dataframe.index += 1
    df_qry_result_dataframe.reset_index(inplace=True)
    df_qry_result_dataframe.rename(columns={'index':'Rank'},inplace=True)
    return df_qry_result_dataframe


def reset_database_tables(cur):
    """function will reset database tables to brand new setup"""
    qry_table1 = 'drop table hangman_players'
    qry_table2 = 'drop table hangman_players_score'
    qry_table3 = 'drop table hangman_puzzles'
    # drop table
    cur.execute(qry_table1)
    cur.execute(qry_table2)
    cur.execute(qry_table3)
    create_hangman_tables(cur)


def load_hangman_puzzle(con):
    """this function will load puzzle file into database, should only be executed by admin or during installation"""
    # load hangman puzzle file
    df_puzzle_file = read_csv('../data/hangman_puzzle.csv')
    # generate key, encrypt data
    key = secret.generate_key()
    df_puzzle_file['PUZZLE_SOLUTION'] = df_puzzle_file['PUZZLE_SOLUTION'].apply(lambda x: secret.encrypt_message(x.upper(), key))
    # load data into table
    df_puzzle_file.to_sql('hangman_puzzles', con=con, if_exists='append', index=False)


def get_puzzle(cur):
    """function will return puzzle and puzzle hint"""
    qry = 'select * from hangman_puzzles order by random() limit 1'
    cur.execute(qry)
    puzzle = cur.fetchone()
    return puzzle
