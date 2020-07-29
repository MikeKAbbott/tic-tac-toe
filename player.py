import math
import board

class Player:
    
    def __init__(self, piece:str, board:object) -> object:
        self.piece = piece
        self.board = board

    def best_move(self) -> None:
        bestScore = -math.inf
        bestMove = None
        for index in self.board.board:
            if self.board.valid_move(index):
                temp = self.board.board[index]
                self.board.board[index] = self.piece
                score = self.mini_max(self.board,0,False)
                self.board.board[index] = temp
                if score > bestScore:
                    bestScore = score
                    bestMove = index
        return bestMove
    
    def mini_max(self,board,depth:int, isMax:bool) -> int:
        result = board.check_winner()
        if result != None:
            return board.scores[result]
            
        bestScore = -math.inf if isMax else math.inf
        if isMax:
            for index in board.board:
                if board.valid_move(index):
                    temp = board.board[index]
                    board.board[index] = self.piece
                    score = self.mini_max(board, depth + 1, False)
                    board.board[index] = temp
                    bestScore = max(score,bestScore)
            return bestScore
        else:
            for index in board.board:
                if board.valid_move(index):
                    temp = board.board[index]
                    board.board[index] = "X" if self.piece == "O" else "O"
                    score = self.mini_max(board, depth + 1, True)
                    board.board[index] = temp
                    bestScore = min(score,bestScore)
            return bestScore






