import player

class Board():

    def __init__(self):
        self.board = {
            1:" ", 2:" ", 3:" ",
            4:" ", 5:" ", 6:" ",
            7:" ", 8:" ", 9:" "       
        }
        self.pieces = ["X","O"]
        self.moves = [move == " " for move  in self.board.values()]
    
    """
    Basic function to print the board in the terminal
    """
    def print_board(self) -> None:     
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-+-+-')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-+-+-')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
    
    """
    Checks if the move is valid
    """
    def valid_move(self,move:int) -> bool:
        return self.board[move] == " "
    
    """
    Clears the current board 
    """
    def clear_board(self) -> None:
        self.moves.clear()
        for i in self.board:
            self.board[i] = " " 

    """
    Clears moves and repopulates with all current available
    moves
    """
    def get_moves(self) -> None:
        self.moves.clear()
        for item in self.board:
            if self.board[item] == " ":
                self.moves.append(item)
    
    """
    Checks all spaces of the board to find a winner
    Covers all scenarios and returns which piece was won.
    If no winner was chosen, a tie is made
    """
    def check_winner(self) -> str:
        winner = None
        if self.is_board_full():
            winner = "TIE"
        for piece in self.pieces:
            if ((self.board[1] == (piece) and self.board[2] == (piece) and self.board[3] == (piece)) or  
                (self.board[4] == (piece) and self.board[5] == (piece) and self.board[6] == (piece)) or  
                (self.board[7] == (piece) and self.board[8] == (piece) and self.board[9] == (piece)) or 
                (self.board[1] == (piece) and self.board[4] == (piece) and self.board[7] == (piece)) or  
                (self.board[2] == (piece) and self.board[5] == (piece) and self.board[8] == (piece)) or  
                (self.board[3] == (piece) and self.board[6] == (piece) and self.board[9] == (piece)) or  
                (self.board[1] == (piece) and self.board[5] == (piece) and self.board[9] == (piece)) or  
                (self.board[3] == (piece) and self.board[5] == (piece) and self.board[7] == (piece))):
                    winner = piece
        return winner
                

    """
    Asks the player to make a valid move on the
    board. If the move is valid, the space is replaced
    by the players character
    """
    def make_move(self,player_move:int,player:object) -> None:
        self.board[player_move] = player.piece
        
    """
    Checks to see if the board is full
    If the board is full a tie is the result.
    """    
    def is_board_full(self) -> bool:
        for key in self.board:
            if self.board[key] == " ":
                return False
        return True
   