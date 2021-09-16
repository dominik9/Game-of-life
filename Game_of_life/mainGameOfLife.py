
import sys
import threading

from PyQt5.QtWidgets import QApplication
from Game_of_life.engineGameOfLife import GameOfLifeEngine
from Game_of_life.gui import MainWindow


class MainGameOfLife:
    def __init__(self):
        self.points_width = 20
        self.points_height = 20
        self.engine_work = False
        self.newBoardGOL()
        self.startGUI()

    def startGUI(self):
        App = QApplication(sys.argv)
        self.mainGUI = MainWindow(self.engine.board)

        #Connect funs
        self.mainGUI.randomizeClick.connect(self.randomizeBoard)
        self.mainGUI.startClick.connect(self.startStopEngine)
        self.mainGUI.oneStepClick.connect(self.oneStep)
        self.mainGUI.widthSpinChange.connect(self.widthChange)
        self.mainGUI.heightSpinChange.connect(self.heightChange)

        sys.exit(App.exec())

    def updateGuiBoard(self):
        self.mainGUI.updateBoard(self.engine.board)

    def randomizeBoard(self):
        self.engine.randomPoints()
        self.updateGuiBoard()

    def oneStep(self):
        self.engine.one_step_engine()
        self.updateGuiBoard()

    def startStopEngine(self):
        if not self.engine_work:
            self.interval = self.mainGUI.getInterval()
            self.mainGUI.disableWidgets()
            self.engine_work = True
            self.interval_run()
        else:
            self.engine_work = False
            self.mainGUI.enableWidgets()

    def interval_run(self):
        if self.engine_work:
            self.oneStep()
            threading.Timer(self.interval, self.interval_run).start()

    def widthChange(self):
        self.setNewWidthInPoints(self.mainGUI.getWidthSpin())

    def heightChange(self):
        self.setNewHeightInPoints(self.mainGUI.getHeightSpin())

    def newBoardGOL(self):
        self.engine = GameOfLifeEngine(self.points_width, self.points_height)

    def setNewWidthInPoints(self, width):
        self.points_width = width
        self.newBoardGOL()
        self.updateGuiBoard()

    def setNewHeightInPoints(self, height):
        self.points_height = height
        self.newBoardGOL()
        self.updateGuiBoard()

