#Henry Bojanowski

#
# AI Player for use in Connect Four
#

import random  
from ps10pr3 import *

class AIPlayer(Player):
    """ “AI player” will look ahead some number of moves into the future to
    assess the impact of each possible move that it could make for its next
    move, and it will assign a score to each possible move. And since each
    move corresponds to a column number, it will effectively assign a score
    to each column"""
    def __init__(self,checker,tiebreak,lookahead):
        """constructs AI player object, uses new inputs and they must be defined
"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak=tiebreak
        self.lookahead=lookahead


    def __repr__(self):
        """a method __repr__(self) that returns a string representing an AIPlayer
    object. This method will override/replace the __repr__ method that is inherited
    from Player. In addition to indicating which checker the AIPlayer object is using,
    the returned string should also indicate the player’s tiebreaking strategy and lookahead"""
        #return str(self.lookahead)
        return 'Player'+' '+self.checker+ ' ' + '('+self.tiebreak+','+' '+str(self.lookahead)+')'
    
    def max_score_column(self,scores):
        """a method max_score_column(self, scores) that takes a list scores containing a score for
    each column of the board, and that returns the index of the column with the maximum score. If
    one or more columns are tied for the maximum score, the method should apply the called AIPlayer‘s
    tiebreaking strategy to break the tie. Make sure that you return the index of the appropriate column,
    and not the column’s score"""
        lc=[x for x in range(len(scores)) if scores[x]==max(scores)] #creates list of indicies
        if self.tiebreak=='LEFT':
            return lc[0]
        elif self.tiebreak=='RIGHT':
            return lc[-1]
        else:
            return random.choice(lc)


        
    def min_score_column(self,scores):
        """returns the index of the column with the minimum score"""
    
        lc=[x for x in range(len(scores)) if scores[x]==min(scores) and x>=0] #creates list of indicies
        if self.tiebreak=='LEFT':
            return lc[0]
        elif self.tiebreak=='RIGHT':
            return lc[-1]
        else:
            return random.choice(lc)
        
        



    def scores_for(self,board):
        """a method scores_for(self, board) that takes a Board object board and determines the called AIPlayer‘s
    scores for the columns in board"""

        scores=[50] * board.width
        for col in range(board.width):
            if board.can_add_to(col)==False:
                scores[col]= -1
            elif board.is_win_for(self.checker)==True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker())==True:
                scores[col]=0
            elif self.lookahead==0:
                scores[col]=50

            
            else:   # for lookahead >1
                board.add_checker(self.checker,col) # add a checker

                
               
                opponent =AIPlayer(self.opponent_checker(),self.tiebreak,self.lookahead-1) # recursive call
                opp_scores=opponent.scores_for(board)                 
                scores[col]=100-max(opp_scores)
    
                
                board.remove_checker(col)
               
                
    
            
        return scores
        
                
    def next_move(self,board):
        """a method next_move(self, board) that overrides (i.e., replaces) the next_move method that is inherited from Player.
    Rather than asking the user for the next move, this version of next_move should return the called AIPlayer‘s judgment of
    its best possible move. This method won’t need to do much work, because it should use your scores_for and max_score_column
    methods to determine the column number that should be returned"""
        return self.max_score_column(self.scores_for(board))
    
    
        
            




