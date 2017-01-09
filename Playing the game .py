# Henry Bojanowski henryboj@bu.edu

#
# Playing the Game  
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board
def process_move(player,board):
    """ a function process_move(player, board) that takes two parameters: a
    Player object for the player whose move is being processed, and a Board
    object for the game that is being played"""
    print(player.__repr__()+"'s", 'turn')
    players_next_move= player.next_move(board)
    board.add_checker(player.checker, players_next_move)
    print('\n') # prints blank line
    print(board)
    
    if board.is_win_for(player.checker)==True:
        print('Player', player.checker, 'wins in', player.num_moves, 'moves')
        # how do I change the amount of moves it takes for the player to win?
        print('Congratulations!')
        return True
    elif board.is_full()==True:
        print("It's a tie!")
        return True
    else:
        return False
        

class RandomPlayer(Player):
    """a class called RandomPlayer that can be used for an unintelligent computer
    player that chooses at random from the available columns"""
    
    

    
    def next_move(self,board):
        """ a method next_move(self, board) that overrides (i.e., replaces) the
    next_move method that is inherited from Player. Rather than asking the user for
    the next move, this version of next_move should choose at random from the columns
    in the specified board that are not yet full, and return the index of that randomly
    selected column"""
        mylist=[x for x in range(board.width) if board.can_add_to(x)==True ]
        print(mylist)
        random_number_from_index=random.choice(mylist)
        
        return random_number_from_index
    
        
    
    
    
    



    
