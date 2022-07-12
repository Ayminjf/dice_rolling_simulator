import sys
import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from DiceRollingSimulator import Ui_MainWindow_DiceRollingSimulator

class Ui_DiceRollingSimulator(QMainWindow):
    scorep1 , turnp1 = 0 , 0
    scorep2 , turnp2 = 0 , 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.uidicerollingsimulator = Ui_MainWindow_DiceRollingSimulator()
        self.uidicerollingsimulator.setupUi(self)
        self.uidicerollingsimulator.help_btn.clicked.connect(self.help)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.pushbutton()
        self.show()

    def help(self):

            message_box = QtWidgets.QMessageBox()

            message_box.setWindowTitle("Developer information")
            message_box.setWindowIcon(QtGui.QIcon('royal_lionn.ico'))
            message_box.setIcon(QMessageBox.Information)

            message_box.setText("Developer : Amin Jafari\n"
                                "---------------------------------\n"
                                "Gmail : Aminjjjeffrey@gmail.com\n")
            message_box.exec_()

    def mousePressEvent(self, evt):
        self.oldpos = evt.globalPos()

    def mouseMoveEvent(self, evt) :
        delta = QPoint(evt.globalPos() - self.oldpos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldpos = evt.globalPos()

    def pushbutton(self): # buttons
        self.uidicerollingsimulator.dice1.clicked.connect(self.rolling_dice_player1)
        self.uidicerollingsimulator.dice2.clicked.connect(self.rolling_dice_player2)
        self.uidicerollingsimulator.settime.clicked.connect(self.set_time)
        self.uidicerollingsimulator.resetgame1.clicked.connect(self.rest_player1)
        self.uidicerollingsimulator.resetgame2.clicked.connect(self.rest_player2)



    def set_time(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timerr)
        self.timer.start(1000)

    def timerr(self):
        self.timerp = int(self.uidicerollingsimulator.showtime.text())
        self.timerp -= 1 # One second will decrease from  "self.timerp" until the game ends
        self.timerp12 = str(self.timerp)
        self.uidicerollingsimulator.showtime.setText(self.timerp12)

        self.timerpx = int(self.uidicerollingsimulator.showtime.text())
        if (self.timerpx == 0):# \
            # When the "timerpx" reaches 0, "timer" stops and the game ends
            self.timer.stop() # /
            self.uidicerollingsimulator.showtime.setText("0")

            if self.scorep1 > self.scorep2 : # If "player1" had more "Score"
                self.player1 = self.uidicerollingsimulator.player1.text()
                self.uidicerollingsimulator.result.setText(f"{self.player1} Win!")

            elif self.scorep1 == self.scorep2 : # If "both players" had equal "Scores"
                self.player2 = self.uidicerollingsimulator.player2.text()
                self.uidicerollingsimulator.result.setText(f"You are Equal")

            elif self.scorep1 < self.scorep2 : # If "player2" had more "Score"
                self.player2 = self.uidicerollingsimulator.player2.text()
                self.uidicerollingsimulator.result.setText(f"{self.player2} Win!")

    def rolling_dice_player1(self):
        randomnumberp1 = random.randint(1, 6) # It chooses a random number between 1 and 6 for "player1"
        if (randomnumberp1 == 1):
            self.uidicerollingsimulator.dice1lbl.setPixmap(QtGui.QPixmap("PVS/Player1/dice1p1.png"))
            self.scorep1 += randomnumberp1
            self.scorep1str = str(self.scorep1)
            self.uidicerollingsimulator.score1.setText(self.scorep1str)
            self.turnp1 += 1 # After rolling the dice, the first player's turn increases by one unit
            self.turnp1str = str(self.turnp1)
            self.uidicerollingsimulator.turn1.setText(self.turnp1str)

        elif (randomnumberp1 == 2):
            self.uidicerollingsimulator.dice1lbl.setPixmap(QtGui.QPixmap("PVS/Player1/dice2p1.png"))
            self.scorep1 += randomnumberp1
            self.scorep1str = str(self.scorep1)
            self.uidicerollingsimulator.score1.setText(self.scorep1str)
            self.turnp1 += 1
            self.turnp1str = str(self.turnp1)
            self.uidicerollingsimulator.turn1.setText(self.turnp1str)

        elif (randomnumberp1 == 3):
            self.uidicerollingsimulator.dice1lbl.setPixmap(QtGui.QPixmap("PVS/Player1/dice3p1.png"))
            self.scorep1 += randomnumberp1
            self.scorep1str = str(self.scorep1)
            self.uidicerollingsimulator.score1.setText(self.scorep1str)
            self.turnp1 += 1
            self.turnp1str = str(self.turnp1)
            self.uidicerollingsimulator.turn1.setText(self.turnp1str)

        elif (randomnumberp1 == 4):
            self.uidicerollingsimulator.dice1lbl.setPixmap(QtGui.QPixmap("PVS/Player1/dice4p1.png"))
            self.scorep1 += randomnumberp1
            self.scorep1str = str(self.scorep1)
            self.uidicerollingsimulator.score1.setText(self.scorep1str)
            self.turnp1 += 1
            self.turnp1str = str(self.turnp1)
            self.uidicerollingsimulator.turn1.setText(self.turnp1str)

        elif (randomnumberp1 == 5):
            self.uidicerollingsimulator.dice1lbl.setPixmap(QtGui.QPixmap("PVS/Player1/dice5p1.png"))
            self.scorep1 += randomnumberp1
            self.scorep1str = str(self.scorep1)
            self.uidicerollingsimulator.score1.setText(self.scorep1str)
            self.turnp1 += 1
            self.turnp1str = str(self.turnp1)
            self.uidicerollingsimulator.turn1.setText(self.turnp1str)

        elif (randomnumberp1 == 6):
            self.uidicerollingsimulator.dice1lbl.setPixmap(QtGui.QPixmap("PVS/Player1/dice6p1.png"))
            self.scorep1 += randomnumberp1
            self.scorep1str = str(self.scorep1)
            self.uidicerollingsimulator.score1.setText(self.scorep1str)
            self.turnp1 += 1
            self.turnp1str = str(self.turnp1)
            self.uidicerollingsimulator.turn1.setText(self.turnp1str)

    def rolling_dice_player2(self):
        randomnumberp2 = random.randint(1, 6) # It chooses a random number between 1 and 6 for "player2"
        if (randomnumberp2 == 1):
            self.uidicerollingsimulator.dice2lbl.setPixmap(QtGui.QPixmap("PVS/Player2/dice1p2.png"))
            self.scorep2 += randomnumberp2
            self.scorep2str = str(self.scorep2)
            self.uidicerollingsimulator.score2.setText(self.scorep2str)
            self.turnp2 += 1 # After rolling the dice, the second  player's turn increases by one unit
            self.turnp2str = str(self.turnp2)
            self.uidicerollingsimulator.turn2.setText(self.turnp2str)

        elif (randomnumberp2 == 2):
            self.uidicerollingsimulator.dice2lbl.setPixmap(QtGui.QPixmap("PVS/Player2/dice2p2.png"))
            self.scorep2 += randomnumberp2
            self.scorep2str = str(self.scorep2)
            self.uidicerollingsimulator.score2.setText(self.scorep2str)
            self.turnp2 += 1
            self.turnp2str = str(self.turnp2)
            self.uidicerollingsimulator.turn2.setText(self.turnp2str)

        elif (randomnumberp2 == 3):
            self.uidicerollingsimulator.dice2lbl.setPixmap(QtGui.QPixmap("PVS/Player2/dice3p2.png"))
            self.scorep2 += randomnumberp2
            self.scorep2str = str(self.scorep2)
            self.uidicerollingsimulator.score2.setText(self.scorep2str)
            self.turnp2 += 1
            self.turnp2str = str(self.turnp2)
            self.uidicerollingsimulator.turn2.setText(self.turnp2str)

        elif (randomnumberp2 == 4):
            self.uidicerollingsimulator.dice2lbl.setPixmap(QtGui.QPixmap("PVS/Player2/dice4p2.png"))
            self.scorep2 += randomnumberp2
            self.scorep2str = str(self.scorep2)
            self.uidicerollingsimulator.score2.setText(self.scorep2str)
            self.turnp2 += 1
            self.turnp2str = str(self.turnp2)
            self.uidicerollingsimulator.turn2.setText(self.turnp2str)

        elif (randomnumberp2 == 5):
            self.uidicerollingsimulator.dice2lbl.setPixmap(QtGui.QPixmap("PVS/Player2/dice5p2.png"))
            self.scorep2 += randomnumberp2
            self.scorep2str = str(self.scorep2)
            self.uidicerollingsimulator.score2.setText(self.scorep2str)
            self.turnp2 += 1
            self.turnp2str = str(self.turnp2)
            self.uidicerollingsimulator.turn2.setText(self.turnp2str)

        elif (randomnumberp2 == 6):
            self.uidicerollingsimulator.dice2lbl.setPixmap(QtGui.QPixmap("PVS/Player2/dice6p2.png"))
            self.scorep2 += randomnumberp2
            self.scorep2str = str(self.scorep2)
            self.uidicerollingsimulator.score2.setText(self.scorep2str)
            self.turnp2 += 1
            self.turnp2str = str(self.turnp2)
            self.uidicerollingsimulator.turn2.setText(self.turnp2str)

    def rest_player1(self): # It resets everything for player1 and starts the game from the beginning
        self.turnp1 = 0
        self.scorep1 = 0
        self.timer.stop()
        self.uidicerollingsimulator.result.setText("▼  Result  ▼")
        self.uidicerollingsimulator.showtime.setText("")
        self.uidicerollingsimulator.player1.setText("")
        self.uidicerollingsimulator.score1.setText("0")
        self.uidicerollingsimulator.turn1.setText("0")
        self.uidicerollingsimulator.dice1lbl.setPixmap(QtGui.QPixmap("PVS/Player1/DiceP1.png"))


    def rest_player2(self): # It resets everything for player2 and starts the game from the beginning
        self.turnp2 = 0
        self.scorep2 = 0
        self.timer.stop()
        self.uidicerollingsimulator.result.setText("▼  Result  ▼")
        self.uidicerollingsimulator.showtime.setText("")
        self.uidicerollingsimulator.player2.setText("")
        self.uidicerollingsimulator.score2.setText("0")
        self.uidicerollingsimulator.turn2.setText("0")
        self.uidicerollingsimulator.dice2lbl.setPixmap(QtGui.QPixmap("PVS/Player2/DiceP2.png"))








if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = Ui_DiceRollingSimulator()
    sys.exit(app.exec_())