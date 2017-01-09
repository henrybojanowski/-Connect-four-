# Henry Bojanowski


class Board:
    """creates a connect 4 game"""
    def __init__(self,height,width):
        self.height=height
        self.width=width
        self.slots= [[' '] * self.width for row in range(self.height)]

        
    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.
        s+='-'
        s+='--'*self.width
        s+='\n'
        for col in range(self.width):
            s+= ' ' +str(col%10)
            

        return s        

    def add_checker(self, checker, col):
        """ put your docstring here
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        
        # put the rest of the method here
        if checker=='X':
            
            for row in range(self.height):
                if self.slots[self.height-1][col]==' ': # dealing with the entire column as empty
                    
                    self.slots[self.height-1][col] ='X'
                    return
                elif self.slots[row+1][col]=='X' or self.slots[row+1][col]=='O':  # the entire column is not empty
                    
                    self.slots[row][col] = 'X'
                    return
        elif checker=='O':
            for row in range(self.height):
                if self.slots[self.height-1][col]==' ': # dealing with the entire column as empty
                    
                    self.slots[self.height-1][col] ='O'
                    return
                elif self.slots[row+1][col]=='X' or self.slots[row+1][col]=='O':  # the entire column is not empty
                    
                    self.slots[row][col] = 'O'
                    return



                
    def reset(self):
        """ a method reset(self) that should reset the Board object on which it is called by setting all slots to
        contain a space character."""
        self.slots= [[' '] * self.width for row in range(self.height)]


        
 
    
    def add_checkers(self,colnums):
        """ takes in"""
        checker='X'
        for col_str in colnums:
            col=int(col_str)
            if 0<=col<self.width:
                self.add_checker( checker, col)

            if checker=='X':
                checker='O'
            else:
                checker='X'
    def can_add_to(self,col):
        """a method can_add_to(self, col) that returns True if it is valid to place a checker in the column col on the calling
    Board object. Otherwise, it should return False."""
        for row in range(self.height):
            if col>=self.width:
                print('The column number is too high, this should return False')
                return False # if the column is too high
            elif self.slots[0][col]=='X' or self.slots[0][col]=='O':
                return False # if the column is full
            elif col<0: 
                return False # if the column is negative
            
            else:
                return True
            
    def is_full(self):
        """a method is_full(self) that returns True if the called Board object is completely full of checkers,
    and returns False otherwise."""
        count=0
        for col in range(self.width):
            if self.can_add_to(col)==False:
                count+=1

                
        if count==self.width:
            return True
        else:
            return False
            
                
        
    def remove_checker(self,col):
        """a method remove_checker(self, col) that removes the top checker from column col of the called
    Board object. If the column is empty, then the method should do nothing."""
        for row in range(self.height):
                if self.slots[self.height-1][col]==' ': # dealing with the entire column as empty
                    print('dealing with the entire empty column has been executed')
                    return
                
                elif self.slots[row][col]=='X' or self.slots[row][col]=='O':
                    self.slots[row][col]=' '
                    return 
    
    def is_horizontal_win(self, checker):
        """checks for a horizontal win"""
        
        for row in range(self.height):
            for col in range(self.width-3):
                if self.slots[row][col]==checker and \
                   self.slots[row][col+1] ==checker and \
                   self.slots[row][col+2] == checker and \
                   self.slots[row][col+3]==checker:
                    return True
        
        return False
                

    def is_vertical_win(self,checker):
        """checks for a vertical win"""
        for col in range(self.width):
            for row in range(self.height-3):
                if self.slots[row][col]==checker and \
                   self.slots[row+1][col]==checker and \
                   self.slots[row+2][col]==checker and \
                   self.slots[row+3][col]==checker:
                    return True
        
        return False


    def is_up_diagonal_win(self,checker):
        """checks for a diagonal-up win"""
        for row in range(self.height-3):
            for col in range(self.width-3):
                r=self.height-row-1 # flips rows so it starts from the bottom
##                print(row, col)
                if self.slots[r][col]==checker and \
                   self.slots[r-1][col+1]==checker and \
                   self.slots[r-2][col+2]==checker and \
                   self.slots[r-3][col+3] ==checker:
                    return True
        return False

    
    def is_down_diagonal_win(self,checker):
       
        """checks for a diagonal-down win"""
        for row in range(self.height-3):
            for col in range(self.width-3):
                
                #r=self.height-row -1
                r=row
              
                if self.slots[r][col]==checker and \
                   self.slots[r+1][col+1]==checker and \
                   self.slots[r+2][col+2]==checker and \
                   self.slots[r+3][col+3] ==checker:
                    return True
        return False

    
    def is_win_for(self,checker):
        """a method is_win_for(self, checker) that accepts a parameter checker that is either 'X' or 'O', and
    returns True if there are four consecutive slots containing checker on the board. Otherwise, it should return
    False."""
        assert(checker=='X' or checker=='O')
        if self.is_horizontal_win(checker)==True or \
           self.is_vertical_win(checker)==True or \
           self.is_down_diagonal_win(checker)==True or \
           self.is_up_diagonal_win(checker)==True:
            return True
        else:
            return False
        

def test():
    
    print(b.is_up_diagonal_win('X'))
    print(b.is_down_diagonal_win('X'))
    print(b)
        
        

                
                    
        
