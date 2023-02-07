import os

class Board:
    def __init__(self):
        self.gameState = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.eval = None
        self.turn = "X"
    def print_gamestate(self):
        for line in self.gameState:
            print(line)
    def add_token(self, position):
        self.gameState[int(position[1])-1][int(position[0])-1] = self.turn
        self.change_turn()
    def change_turn(self):
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"


b1 = Board()
while True:
    position = list(input("what is your choice of position: "))
    os.system('cls')
    del position[1]
    b1.add_token(position)
    b1.print_gamestate()
