from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt


class GOLViewEngine(QWidget):

    def __init__(self,list_view):
        super().__init__()
        self.board = list_view
        self.rect_height = 0
        self.rect_width = 0

    def paintEvent(self, event):
        self.setup_rectSize()
        qp = QPainter()
        qp.begin(self)
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        self.paintTable(qp)
        qp.end()

    def paintTable(self, qp):
        for i_y in range(len(self.board)):
            for i_x in range(len(self.board[0])):
                if self.board[i_y][i_x] == 1:
                    qp.drawRect(i_x * self.rect_width, i_y * self.rect_height, self.rect_width, self.rect_height)

    def updateBoard(self, board):
        self.setup_rectSize()
        self.board = board
        self.update()

    def setup_rectSize(self):
        size = self.size()
        self.rect_width = size.width() / len(self.board[0])
        self.rect_height = size.height() / len(self.board)
