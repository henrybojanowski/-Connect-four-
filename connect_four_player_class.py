# Henry Bojanowski 

#
# A Connect-Four Player class 
#

from ps10pr1 import Board



class Player:
    def __init__(self,checker):
        """initializes the following attributes: 1.) attribute checker a
    one-character string that represents the gamepiece for the player, as
    specified by the parameter checker 2.) n attribute num_moves – an integer
    that stores how many moves the player has made so far. This attribute
    should be initialized to zero to signify that the Player object has not
    yet made any Connect Four moves"""
        self.checker=checker
        self.num_moves=0

    def __repr__(self):
        """a method __repr__(self) that returns a string representing a Player
    object. The string returned should indicate which checker the Player object
    is using"""
        return 'Player'+ ' ' + self.checker
    
    def opponent_checker(self):
        """method opponent_checker(self) that returns a one-character string
    representing the checker of the Player object’s opponent. The method may
    assume that the calling Player object has a checker attribute that is
    either 'X' or 'O'"""
        if self.checker=='X':
            return 'O'
        else:
            return 'X'
    def next_move(self,board):
        """a method named next_move(self, board) that accepts a Board object
    as a parameter and returns the column where the player wants to make the
    next move. To do this, the method should ask the user to enter a column
    number that represents where the user wants to place a checker on the board.
    The method should repeatedly ask for a column number until a valid column
    number is given"""
        while True:
            user_input= int(input('Which column: '))
            if board.can_add_to(user_input)==True:
                self.num_moves +=1
                break
            
            else:
                print('Try again')
        return user_input
            
            
        
