# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'neweva.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from score import Ui_Dialog as Score  # Score window
import sqlite3
import logging
logging.basicConfig(level=logging.INFO)
match = sqlite3.connect("fandatabase.db")
matchcur = match.cursor()


class Ui_MainWindow(object):
    def __init__(self):  # initialising score window
        self.scoreDialog = QtWidgets.QMainWindow()
        self.score_screen = Score()
        self.score_screen.setupUi(self.scoreDialog)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 748)
        MainWindow.setMinimumSize(QtCore.QSize(821, 748))
        MainWindow.setMaximumSize(QtCore.QSize(821, 748))
        MainWindow.setStyleSheet("rgb(231, 231, 231)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 557, 28))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("rgb(231, 231, 231)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 130, 801, 20))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.calcscore_btn = QtWidgets.QPushButton(self.centralwidget)
        self.calcscore_btn.setEnabled(True)
        self.calcscore_btn.setGeometry(QtCore.QRect(350, 660, 137, 33))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.calcscore_btn.setFont(font)
        self.calcscore_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.calcscore_btn.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.calcscore_btn.setAutoDefault(False)
        self.calcscore_btn.setObjectName("calcscore_btn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 170, 801, 471))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("rgb(231, 231, 231)")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.players_lw = QtWidgets.QListWidget(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.players_lw.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.players_lw.setFont(font)
        self.players_lw.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.players_lw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.players_lw.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.players_lw.setObjectName("players_lw")
        self.verticalLayout_4.addWidget(self.players_lw)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("rgb(231, 231, 231)")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.scores_lw_2 = QtWidgets.QListWidget(self.widget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scores_lw_2.setFont(font)
        self.scores_lw_2.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.scores_lw_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scores_lw_2.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.scores_lw_2.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.scores_lw_2.setObjectName("scores_lw_2")
        self.verticalLayout_3.addWidget(self.scores_lw_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 90, 791, 36))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # COMBOBOXES
        # TEAMNAME COMBOBOX
        self.selectteam_cb = QtWidgets.QComboBox(self.widget1)
        self.selectteam_cb.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.selectteam_cb.setCurrentText("")
        self.selectteam_cb.setObjectName("selectteam_cb")
        self.horizontalLayout.addWidget(self.selectteam_cb)
        self.selectmatch_cb = QtWidgets.QComboBox(self.widget1)
        self.selectmatch_cb.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        # MATCHNAME COMBOBX
        self.selectmatch_cb.setFont(font)
        self.selectmatch_cb.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.selectmatch_cb.setObjectName("selectmatch_cb")
        self.selectmatch_cb.addItem("")
        self.horizontalLayout.addWidget(self.selectmatch_cb)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # score button
        self.calcscore_btn.clicked.connect(self.final_score)
        selected_team = self.selectteam_cb.currentText()

        self.changedname(selected_team)

        # upon current team name- changed
        self.selectteam_cb.currentTextChanged.connect(self.changedname)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Evaluate Score"))
        self.label.setText(_translate("MainWindow", " ~~~~Evaluate the Performance of your Fantasy Team~~~~~"))
        self.calcscore_btn.setStatusTip(_translate("MainWindow", "calculating score"))
        self.calcscore_btn.setText(_translate("MainWindow", "Calculate Score"))
        self.label_3.setText(_translate("MainWindow", "Players"))
        self.label_2.setText(_translate("MainWindow", "Points"))
        self.selectmatch_cb.setItemText(0, _translate("MainWindow", "Match1"))

        x = matchcur.execute("SELECT  DISTINCT name from teams;")
        team = x.fetchall()
        for i in team:
            self.selectteam_cb.addItem(i[0])

    def changedname(self, t):
        self.players_lw.clear()
        self.scores_lw_2.clear()
        y = matchcur.execute("SELECT players from teams WHERE name='" + t + "';")
        player = y.fetchall()
        logging.debug('player',player)
        for j in player:
            self.players_lw.addItem(j[0])
        z = matchcur.execute("SELECT value from teams WHERE name='" + t + "';")
        value = z.fetchall()
        for k in value:
            self.scores_lw_2.addItem(str(k[0]))

    def final_score(self):
        total_score = 0
        t = self.selectteam_cb.currentText()  # current teamname
        logging.debug(t)
        z = matchcur.execute("SELECT value from teams WHERE name='" + t + "';")
        value = z.fetchall()
        logging.debug('value', value)
        for k in value:
            total_score += k[0]
        self.score_screen.finalscore.setText(str(total_score))  # opening score dialog box and setting final score
        self.scoreDialog.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
