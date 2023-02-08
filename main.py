import os
import math

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

    def change_turn(self):
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"
    def check_for_win(self):
        for x in range(3):
            if self.gameState[0][x] == self.turn and self.gameState[1][x] == self.turn and self.gameState[2][x] == self.turn:  # check columns
                return True
            if self.gameState[x][0] == self.turn and self.gameState[x][1] == self.turn and self.gameState[x][2] == self.turn:  # check rows
                return True
        if self.gameState[0][0] == self.turn and self.gameState[1][1] == self.turn and self.gameState[2][2] == self.turn:  # check diagonal
            return True
        if self.gameState[0][2] == self.turn and self.gameState[1][1] == self.turn and self.gameState[2][0] == self.turn:  # check other diagonal
            return True
        return False
    def check_for_draw(self):
        for line in self.gameState:
            for sq in line:
                if sq == '-':
                    return False
        return True

    def evaluate(self):
        if self.check_for_win():
            if self.turn == "X":
                self.eval = math.inf
            elif self.turn == "O":
                self.eval = -math.inf
            else:
                self.eval = 0

b1 = Board()
win = False
print("\n" * 50)
while True:
    b1.print_gamestate()
    position = list(input("what is your choice of position: "))
    try:
        del position[1]
        if b1.gameState[int(position[1])-1][int(position[0])-1] == '-':
            b1.add_token(position)
            print("\n" * 50)  # clear screen

            if b1.check_for_win():
                print(b1.turn, " Won!")  #player wins
                b1.print_gamestate()
                win = True
            if b1.check_for_draw():
                print("Draw")  # draw
                b1.print_gamestate()
                win = True

            b1.change_turn()
        else:
            print("\n" * 50)
            print("can't place token there")
    except:
        print("\n" * 50)  # clear screen
        print("invalid input")
    if win == True:
        exit()




