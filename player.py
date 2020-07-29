import math
import board

class Player:
    
    def __init__(self, piece:str, board:object) -> object:
        self.piece = piece
        self.board = board


    def best_move(self) -> int:
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
        scores = {
            "O": 1,
            "X": -1,
            "TIE":0
        }
        result = board.check_winner()
        if result != None:
            return scores[result]   
        bestScore = -math.inf if isMax else math.inf
        human = "X" if self.piece == "O" else "O"
        for index in board.board:
            if board.valid_move(index):
                temp = board.board[index]
                board.board[index] = self.piece if isMax else human
                score = self.mini_max(board, depth + 1, isMax = False if isMax else True)
                board.board[index] = temp
                bestScore = max(score,bestScore) if isMax else min(score,bestScore)
        return bestScore







