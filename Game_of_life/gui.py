from PyQt5.QtWidgets import QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QDoubleSpinBox, QSpinBox
from PyQt5 import QtCore
from Game_of_life.GOLVisualWidget import GOLViewEngine

class MainWindow(QWidget):
    randomizeClick = QtCore.pyqtSignal()
    oneStepClick = QtCore.pyqtSignal()
    startClick = QtCore.pyqtSignal()
    widthSpinChange = QtCore.pyqtSignal()
    heightSpinChange = QtCore.pyqtSignal()

    def __init__(self, first_board):
        super().__init__()
        self.InitWindow(first_board)

    def InitWindow(self, first_board):
        self.setMinimumSize(600, 400)

        #View widget setup
        self.gol_widget = GOLViewEngine(first_board)

        #Time interval
        intervalLayout = QHBoxLayout()
        intervalLabel = QLabel("Interval", self)
        self.intervalSpin = QDoubleSpinBox()
        self.intervalSpin.setRange(0.1, 100.00)
        self.intervalSpin.setSingleStep(0.1)
        self.intervalSpin.setValue(1.00)
        intervalLayout.addWidget(intervalLabel)
        intervalLayout.addWidget(self.intervalSpin)
        self.intervalSpin.setFixedHeight(50)
        font = self.intervalSpin.font()
        font.setPointSize(20)
        self.intervalSpin.setFont(font)
        intervalLabel.setFont(font)

        #Spins to width and height in points
        width_spin_layout = QHBoxLayout()
        height_spin_layout = QHBoxLayout()
        width_spin_label = QLabel("Width", self)
        height_spin_label = QLabel("Height", self)
        width_spin_label.setFont(font)
        height_spin_label.setFont(font)
        self.width_spin = QSpinBox()
        self.height_spin = QSpinBox()
        self.width_spin.setRange(10, 300)
        self.height_spin.setRange(10, 300)
        self.width_spin.setSingleStep(1)
        self.height_spin.setSingleStep(1)
        self.width_spin.setValue(20)
        self.height_spin.setValue(20)
        self.width_spin.setFixedHeight(50)
        self.height_spin.setFixedHeight(50)
        self.width_spin.setFont(font)
        self.height_spin.setFont(font)

        #self.width_spin.
        self.width_spin.valueChanged.connect(self.widthSpinChange)
        self.height_spin.valueChanged.connect(self.heightSpinChange)
        width_spin_layout.addWidget(width_spin_label)
        width_spin_layout.addWidget(self.width_spin)
        height_spin_layout.addWidget(height_spin_label)
        height_spin_layout.addWidget(self.height_spin)
        # Button random
        self.btn_random = QPushButton('Random', self)
        self.btn_random.clicked.connect(self.randomizeClick)
        self.btn_random.setFixedHeight(60)
        # Button one step
        self.btn_one_step = QPushButton('One step', self)
        self.btn_one_step.clicked.connect(self.oneStepClick)
        self.btn_one_step.setFixedHeight(60)
        #Button start
        self.btn_start = QPushButton('Start', self)
        self.btn_start.clicked.connect(self.startClick)
        self.btn_start.setFixedHeight(60)
        # Right VBox layout init
        right_layout = QVBoxLayout()
        right_layout.addLayout(intervalLayout)
        right_layout.addLayout(width_spin_layout)
        right_layout.addLayout(height_spin_layout)
        right_layout.addWidget(self.btn_random)
        right_layout.addWidget(self.btn_one_step)
        right_layout.addWidget(self.btn_start)
        # Set layouts
        left_layout = QHBoxLayout()
        left_layout.addWidget(self.gol_widget)
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(left_layout)
        mainLayout.addLayout(right_layout)
        self.setLayout(mainLayout)

        self.show()

    def updateBoard(self, board):
        self.gol_widget.updateBoard(board)

    def getInterval(self):
        return self.intervalSpin.value()

    def getHeightSpin(self):
        return self.height_spin.value()

    def getWidthSpin(self):
        return self.width_spin.value()

    def disableWidgets(self):
        self.btn_random.setDisabled(True)
        self.btn_start.setText("Stop")
        self.btn_one_step.setDisabled(True)
        self.width_spin.setDisabled(True)
        self.height_spin.setDisabled(True)
        self.intervalSpin.setDisabled(True)

    def enableWidgets(self):
        self.btn_random.setDisabled(False)
        self.btn_start.setText("Start")
        self.btn_one_step.setDisabled(False)
        self.width_spin.setDisabled(False)
        self.height_spin.setDisabled(False)
        self.intervalSpin.setDisabled(False)
