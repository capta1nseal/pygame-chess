from abc import ABC, abstractmethod

class Piece(ABC):
    '''base class for chess pieces'''
    def __init__(self, colour, position) -> None:
        self.color = colour
        self.position = position
    
    def move(self, target):
        '''logic for moving the chess piece'''
        self.check_move(target)

    def check_move(self, target):
        pass

    @abstractmethod
    def valid_moves(self):
        pass