import numpy
import chess
import chess.svg
from chessboard import display

board = chess.Board()
boardsvg = chess.svg.board(board=board, squares=chess.BB_ALL)
print(board)
print(board.fen)
position = board.fen()

while True:
    display.start(board.fen())
