from board import Board
from player import Player
        
""""
Main game loop, player selects a champion,
plays against the AI until there is a winner or
a tie is made
"""
class Game: 
    def __init__(self,board):
        self.board = board
        self.human = Player("", self.board)
        self.arti = Player("", self.board)
        self.turn = False

    def start_game(self) -> None:
        self.board.clear_board()
        #Human chooses a character
        while True:
            try:
                character = input("Choose your character: X or O: ")
                if character.upper() in self.board.pieces:
                    self.human.piece = character.upper()   
                    self.arti.piece = "O" if (self.human.piece.upper() == "X") else "X"
                    break
                print("Invalid character")
            except Exception as e:
                print(e)
        #main game loop that breaks if the bool is full, or there is a winner
        self.turn = False if self.human.piece == "O" else True
        while not self.board.is_board_full() and self.board.check_winner() == None:
            if self.turn:
                self.turn = False
                self.board.get_moves()
                while True:
                    try:
                        self.board.print_board()
                        player_move = int(input("Choose a space "))
                        if player_move in self.board.moves:
                            self.board.make_move(player_move,self.human)
                            break
                        print("Invalid Move")
                    except Exception as e:
                        print(e)
            else:
                best_move = self.arti.best_move()
                self.board.make_move(best_move,self.arti)
                self.turn = True
        
        self.board.print_board()
        #if the game is a tie
        if self.board.is_board_full():
            winner = "TIE"
            print("-------------")
            print("TIE GAME")
            print("-------------")
        #if there isa  winner
        else:
            winner = self.human.piece if not self.turn else self.arti.piece
            print("-------------")
            print("WINNER!!! " + winner )
            print("-------------")
       
        #Ask the player if they want to play another game
        newGame =  input("New Game? Y/N: ")
        if newGame.upper() == "Y":
            self.start_game()


if __name__ == "__main__":
    board = Board()
    game = Game(board)
    game.start_game()

    

