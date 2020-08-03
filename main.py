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

    def start_game(self) -> None:
        self.board.clear_board()
        human_turn = True
        while True:
            try:
                champion = input("Choose your chamption: X or O: ")
                if champion.upper() in self.board.pieces:
                    self.human.piece = champion.upper()   
                    self.arti.piece = "O" if (self.human.piece.upper() == "X") else "X"
                    break
                print("Invalid champion")
            except Exception as e:
                print(e)

        while not self.board.is_board_full() and self.board.check_winner() == None:
            if human_turn:
                human_turn = False
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
                human_turn = True
        
        self.board.print_board()
        if self.board.is_board_full():
            winner = "TIE"
            print("-------------")
            print("TIE GAME")
            print("-------------")
        else:
            winner = self.human.piece if not human_turn else self.arti.piece
            print("-------------")
            print("WINNER!!! " + winner )
            print("-------------")

        newGame =  input("New Game? Y or N: ")
        if newGame.upper() == "Y":
            self.start_game()


if __name__ == "__main__":
    board = Board()
    game = Game(board)
    game.start_game()

    

