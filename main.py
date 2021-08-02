# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import game.hangman as gh

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    g = gh.hangman()
    g.__set_player_name__('Gaurav')
    print(g.__get_player_name__())
    print(g.__get_number_of_wrong_choices__())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
