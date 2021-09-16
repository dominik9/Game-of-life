import random


class GameOfLifeEngine:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = [[self.generateBoard(i, j) for i in range(self.width)] for j in range(self.height)]

    def __str__(self):
        s = ''
        for wid in range(len(self.board)):
            for h in self.board[wid]:
                if h:
                    s = s + '#'
                else:
                    s = s + '-'
            s = s + '\n\r'
        return s

    def change_point(self, x, y):
        if x < self.width and x >= 0 and y < self.height and y >= 0:
            if self.board[y][x] == 1:
                self.board[y][x] = 0
            else:
                self.board[y][x] = 1

    def get_new_point(self, x, y):
        nei = 0
        for i_y in range(y - 1, y + 2):
            if i_y < 0 or i_y >= self.height:
                continue
            for i_x in range(x - 1, x + 2):
                if i_x < 0 or i_x >= self.width:
                    continue
                nei = nei + self.board[i_y][i_x]
        nei = nei - self.board[y][x]
        if self.board[y][x] == 1:
            if nei == 2 or nei == 3:
                return 1
            else:
                return 0
        else:
            if nei == 3:
                return 1
            else:
                return 0

    def one_step_engine(self):
        new_position_list = []
        for i_position_y in range(self.height):
            new_row = []
            for i_position_x in range(self.width):
                new_row.append(self.get_new_point(i_position_x, i_position_y))
            new_position_list.append(new_row)
        self.board = new_position_list

    def randomPoints(self):
        self.board = [[random.randrange(1, 100) % 2 for i in range(self.width)] for j in range(self.height)]

    def generateBoard(self, i, j):
        if i % 2 == 0 and j % 2 == 0:
            return 1
        else:
            return 0

