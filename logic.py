from piece import Piece

class Logic:
    '''logical operations for chess'''
    def __init__(self) -> None:
        self.pieces = []

        self.create_board()

    def create_board(self) -> None:
        
        piece_layout = [(piece, 0, (x, 8)) for piece, x in (("rook", 1), ("knight", 2), ("bishop", 3), ("queen", 4), ("king", 5), ("bishop", 6), ("knight", 7), ("rook", 8))]\
            + [("pawn", 0, (x, 7)) for x in range(1, 9)]\
            + [("pawn", 1, (x, 2)) for x in range(1, 9)]\
            + [(piece, 0, (x, 1)) for piece, x in (("rook", 1), ("knight", 2), ("bishop", 3), ("queen", 4), ("king", 5), ("bishop", 6), ("knight", 7), ("rook", 8))]

        print(piece_layout)

        for piece, colour, position in piece_layout:
            print(piece)