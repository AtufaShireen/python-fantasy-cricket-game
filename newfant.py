# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newfant.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from points_calculator import player_points
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from open import Ui_Dialog as Open  # importing open window dialogbox
from new import Ui_Dialog as New  # importing new window dialogbox
from neweva import Ui_MainWindow as Eva  # importing evaluate window

import sqlite3
import logging

fant = sqlite3.connect('fandatabase.db')  # connecting to database file(fandatabase.db)
fantcurs = fant.cursor()
logging.basicConfig(level=logging.INFO)

class Ui_MainWindow(object):
    def __init__(self):
        # INITIALISING WINDOWS
        self.newDialog = QtWidgets.QMainWindow()
        self.new_screen = New()
        self.new_screen.setupUi(self.newDialog)

        self.EvaluateWindow = QtWidgets.QMainWindow()
        self.eval_screen = Eva()
        self.eval_screen.setupUi(self.EvaluateWindow)

        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = Open()
        self.open_screen.setupUi(self.openDialog)

        # FILE OPENING MENU

    def file_open(self):
        self.open_screen.setupUi(self.openDialog)
        self.openDialog.show()
        self.open_screen.openbtn.clicked.connect(self.openteam)

        # EVALUATE TEAM MENU

    def file_evaluate(self):
        self.eval_screen.setupUi(self.EvaluateWindow)
        self.EvaluateWindow.show()

    # NEW FILE MENU
    def file_new(self):
        self.newDialog.show()

    def setupUi(self, MainWindow):
        # INITIALISING POINTS AND COUNTS
        self.avail_points = 1000
        self.used_points = 0
        self.totalcount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.alrdscount = 0
        self.wicketerscount = 0

        # INITIALIZING LISTS
        self.a = []  # bowler names list
        self.b = []  # batsman nameslist
        self.c = []  # allrounder names list
        self.d = []  # wicketer names list
        self.list1 = []  # selectedplayer's list

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 692)
        MainWindow.setMinimumSize(QtCore.QSize(708, 692))
        MainWindow.setMaximumSize(QtCore.QSize(708, 692))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.team_name = QtWidgets.QLabel(self.centralwidget)
        self.team_name.setGeometry(QtCore.QRect(150, 12, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        # TEAMNAME
        self.team_name.setFont(font)
        self.team_name.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.team_name.setAlignment(QtCore.Qt.AlignCenter)
        self.team_name.setObjectName("team_name")
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:rgb(210, 212, 73)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(395, 300, 16, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.wicketcount = QtWidgets.QLabel(self.centralwidget)
        self.wicketcount.setGeometry(QtCore.QRect(300, 80, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.wicketcount.setFont(font)
        self.wicketcount.setStyleSheet("background-color:rgb(210, 212, 73);color:rgb(133, 255, 174)")
        self.wicketcount.setIndent(10)
        self.wicketcount.setObjectName("wicketcount")

        self.Batsman = QtWidgets.QLabel(self.centralwidget)
        self.Batsman.setGeometry(QtCore.QRect(10, 80, 130, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.Batsman.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Batsman.setFont(font)
        self.Batsman.setStyleSheet("background-color:rgb(210, 212, 73)")
        self.Batsman.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Batsman.setIndent(1)
        self.Batsman.setObjectName("Batsman")

         #BATSMEN COUNTER
        self.batcount = QtWidgets.QLabel(self.centralwidget)
        self.batcount.setGeometry(QtCore.QRect(140, 80, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.batcount.setFont(font)
        self.batcount.setStyleSheet("background-color:rgb(210, 212, 73);\n"
                                    "color:rgb(133, 255, 174);")
        self.batcount.setObjectName("batcount")

        self.Bowlers = QtWidgets.QLabel(self.centralwidget)
        self.Bowlers.setGeometry(QtCore.QRect(520, 80, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Bowlers.setFont(font)
        self.Bowlers.setStyleSheet("background-color:rgb(210, 212, 73)")
        self.Bowlers.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Bowlers.setObjectName("Bowlers")

        #ALROUNDERS COUNTER
        self.alrcount = QtWidgets.QLabel(self.centralwidget)
        self.alrcount.setGeometry(QtCore.QRect(480, 80, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.alrcount.setFont(font)
        self.alrcount.setStyleSheet("background-color:rgb(210, 212, 73);color:rgb(133, 255, 174)")
        self.alrcount.setIndent(10)
        self.alrcount.setObjectName("alrcount")

        # BOWLERS COUNTER
        self.bowlcount = QtWidgets.QLabel(self.centralwidget)
        self.bowlcount.setGeometry(QtCore.QRect(650, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bowlcount.setFont(font)
        self.bowlcount.setStyleSheet("background-color:rgb(210, 212, 73);color:rgb(133, 255, 174)")
        self.bowlcount.setIndent(10)
        self.bowlcount.setObjectName("bowlcount")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 170, 331, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

                #RADDO BUTTONS
        #WICKETKEEPER
        self.wk_rb = QtWidgets.QRadioButton(self.widget)
        self.wk_rb.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.wk_rb.setFont(font)
        self.wk_rb.setObjectName("wk_rb")
        self.horizontalLayout.addWidget(self.wk_rb)

        #BATSMAN
        self.bat_rb = QtWidgets.QRadioButton(self.widget)
        self.bat_rb.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bat_rb.setFont(font)
        self.bat_rb.setTabletTracking(False)
        self.bat_rb.setAcceptDrops(False)
        self.bat_rb.setToolTipDuration(20)
        self.bat_rb.setStyleSheet("Batmans")
        self.bat_rb.setObjectName("bat_rb")
        self.horizontalLayout.addWidget(self.bat_rb)

        #ALLROUNDER

        self.ar_rb = QtWidgets.QRadioButton(self.widget)
        self.ar_rb.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ar_rb.setFont(font)
        self.ar_rb.setChecked(False)
        self.ar_rb.setObjectName("ar_rb")
        self.horizontalLayout.addWidget(self.ar_rb)

        #BOWLER
        self.bow_rb = QtWidgets.QRadioButton(self.widget)
        self.bow_rb.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bow_rb.setFont(font)
        self.bow_rb.setObjectName("bow_rb")

        self.horizontalLayout.addWidget(self.bow_rb)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 140, 691, 19))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Totalplayers = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Totalplayers.setFont(font)
        self.Totalplayers.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Totalplayers.setIndent(30)
        self.Totalplayers.setObjectName("Totalplayers")
        self.horizontalLayout_2.addWidget(self.Totalplayers)

            #AVAILABLE POINTS

        self.points_available = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.points_available.setFont(font)
        self.points_available.setStyleSheet("color:rgb(133, 255, 174)")
        self.points_available.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.points_available.setIndent(-10)
        self.points_available.setObjectName("points_available")
        self.horizontalLayout_2.addWidget(self.points_available)
        self.TeamName = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TeamName.setFont(font)
        self.TeamName.setIndent(100)
        self.TeamName.setObjectName("TeamName")
        self.horizontalLayout_2.addWidget(self.TeamName)
        # POINTS USED
        self.points_used = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

            #POINTS USED COUNTER
        self.points_used.setFont(font)
        self.points_used.setStyleSheet("color:rgb(133, 255, 174)")
        self.points_used.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.points_used.setIndent(60)
        self.points_used.setObjectName("points_used")
        self.horizontalLayout_2.addWidget(self.points_used)
        self.Allrounder = QtWidgets.QLabel(self.centralwidget)
        self.Allrounder.setGeometry(QtCore.QRect(330, 80, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Allrounder.setFont(font)
        self.Allrounder.setStyleSheet("background-color:rgb(210, 212, 73)")
        self.Allrounder.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Allrounder.setObjectName("Allrounder")
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 210, 691, 421))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

            #LISTWIDGET
        #AVAILABLEPLAYERS
        self.availplayers_lw = QtWidgets.QListWidget(self.widget2)
        self.availplayers_lw.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.availplayers_lw.setObjectName("availplayers_lw")
        self.horizontalLayout_3.addWidget(self.availplayers_lw)
        self.label_7 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.selectedplayers_lw = QtWidgets.QListWidget(self.widget2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)

        # SELECTEDPLAYERS
        self.selectedplayers_lw.setPalette(palette)
        self.selectedplayers_lw.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.selectedplayers_lw.setObjectName("selectedplayers_lw")
        self.horizontalLayout_3.addWidget(self.selectedplayers_lw)
        self.Wicketkeeepr = QtWidgets.QLabel(self.centralwidget)
        self.Wicketkeeepr.setGeometry(QtCore.QRect(164, 80, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Wicketkeeepr.setFont(font)
        self.Wicketkeeepr.setStyleSheet("background-color:rgb(210, 212, 73)")
        self.Wicketkeeepr.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Wicketkeeepr.setObjectName("Wicketkeeepr")
        self.label_4.raise_()
        self.team_name.raise_()
        self.label_7.raise_()
        self.availplayers_lw.raise_()
        self.Allrounder.raise_()
        self.Wicketkeeepr.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
                # SHORTCUTS
        # NEWTEAM
        self.new_team = QtWidgets.QAction(MainWindow)
        self.new_team.setShortcutVisibleInContextMenu(True)
        self.new_team.setObjectName("new_team")
        self.new_team.triggered.connect(self.file_new)
        # OPENTEAM
        self.open_team = QtWidgets.QAction(MainWindow)
        self.open_team.setShortcutVisibleInContextMenu(True)
        self.open_team.setObjectName("open_team")
        self.open_team.triggered.connect(self.file_open)
        # SAVETEAM
        self.save_team = QtWidgets.QAction(MainWindow)
        self.save_team.setShortcutVisibleInContextMenu(True)
        self.save_team.setObjectName("save_team")
        self.save_team.triggered.connect(self.file_save)
        # EVALUATETEAM
        self.evaluate_team = QtWidgets.QAction(MainWindow)
        self.evaluate_team.setShortcutVisibleInContextMenu(True)
        self.evaluate_team.setObjectName("evaluate_team")
        self.evaluate_team.triggered.connect(self.file_evaluate)
        # QUITWINDOW
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(self.quit)
        self.menuManage_Teams.addAction(self.new_team)
        self.menuManage_Teams.addAction(self.open_team)
        self.menuManage_Teams.addAction(self.evaluate_team)
        self.menuManage_Teams.addAction(self.save_team)
        self.menuManage_Teams.addAction(self.actionQuit)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # DOUBLE CLICK
        self.availplayers_lw.itemDoubleClicked.connect(self.removelist1)
        self.selectedplayers_lw.itemDoubleClicked.connect(self.removelist2)

        # -----stats of player
        self.stats = {}

        self.new_screen.savename.clicked.connect(self.namechange)

        # RADIOBUTTONS  CLICK
        self.bat_rb.clicked.connect(self.load_names)
        self.wk_rb.clicked.connect(self.load_names)
        self.bow_rb.clicked.connect(self.load_names)
        self.ar_rb.clicked.connect(self.load_names)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FantasyCricketGame"))
        self.team_name.setText(_translate("MainWindow", " TEAM NAME "))
        self.label_4.setText(_translate("MainWindow", "Your Selections"))
        self.wicketcount.setText(_translate("MainWindow", "##"))
        self.Batsman.setText(_translate("MainWindow", "Batsmen(Bat)"))
        self.batcount.setText(_translate("MainWindow", "##"))
        self.Bowlers.setText(_translate("MainWindow", "Bowlers(Bow)"))
        self.alrcount.setText(_translate("MainWindow", "##"))
        self.bowlcount.setText(_translate("MainWindow", "##"))
        self.wk_rb.setText(_translate("MainWindow", "WK"))
        self.bat_rb.setText(_translate("MainWindow", "BAT"))
        self.ar_rb.setText(_translate("MainWindow", "AR"))
        self.bow_rb.setText(_translate("MainWindow", "BOW"))
        self.Totalplayers.setText(_translate("MainWindow", "Points Available"))
        self.points_available.setStatusTip(_translate("MainWindow", "max point=100"))
        self.points_available.setText(_translate("MainWindow", "00"))
        self.TeamName.setText(_translate("MainWindow", "Points Used"))
        self.points_used.setText(_translate("MainWindow", "00"))
        self.Allrounder.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.label_7.setText(_translate("MainWindow", ">"))
        self.Wicketkeeepr.setText(_translate("MainWindow", "WicketKeeper(WK)"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.new_team.setText(_translate("MainWindow", "New Team"))
        self.new_team.setStatusTip(_translate("MainWindow", "enter team name"))
        self.new_team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.open_team.setText(_translate("MainWindow", "Open Team"))
        self.open_team.setStatusTip(_translate("MainWindow", "opening team"))
        self.open_team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.save_team.setText(_translate("MainWindow", "Save Team"))
        self.save_team.setStatusTip(_translate("MainWindow", "saving team.."))
        self.save_team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.evaluate_team.setText(_translate("MainWindow", "Evaluate Team"))
        self.evaluate_team.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))



    def namechange(self):
        teamname = self.new_screen.team_name.text()
        fantcurs.execute("SELECT DISTINCT name FROM teams")
        l = fantcurs.fetchall()
        for i in l:
            logging.debug('team names',i)
            if i[0] == teamname:
                logging.debug('inder same name')
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team with same name already exists!!\nPlease choose another name")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
                return 0
        if len(teamname) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You cannot leave the field blank!!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        elif teamname.isnumeric():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        else:
            self.reset()
            self.tname = self.new_screen.team_name.text()
            self.team_name.setText(self.tname)
            self.newDialog.close()

    # TO RESET ALL COUNTS AND LISTS
    def reset(self):
        self.enablebuttons()
        self.load_names()
        self.used_points = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.totalcount = 0
        self.avail_points = 1000
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.bowlcount.setText(str(self.bowlerscount))
        self.batcount.setText(str(self.batsmencount))
        self.alrcount.setText(str(self.alrdscount))
        self.wicketcount.setText(str(self.wicketerscount))
        self.list1.clear()
        self.load_names()

        self.selectedplayers_lw.clear()

        # SAVE TEAM MENU

    def file_save(self):
        if not self.error():  # IF THERE IS AN ERROR
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(' 😪Insufficient Players OR Points !!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()
        elif self.error():  # IF NO ERROR
            try:
                fantcurs.execute("SELECT DISTINCT name FROM teams;")
                x = fantcurs.fetchall()
                for i in x:
                    if self.team_name.text() == i[0]:  # CHECKING IF THE TEAMNAME ALREADY EXISTS
                        logging.debug('Updating already there')
                        fantcurs.execute(
                            "DELETE  FROM teams WHERE name='" + self.team_name.text() + "';")  # DELETING TO UPDATE TEAM
            except:
                logging.debug('error')
            for i in range(self.selectedplayers_lw.count()):
                logging.debug('----addding--')
                logging.debug('teamnane: ',self.team_name.text())
                logging.debug('playername: ',self.list1[i])
                logging.debug('points: ', player_points[self.list1[i]])
                try:
                    fantcurs.execute("INSERT INTO teams (name,players,value) VALUES (?,?,?)",
                                     (self.team_name.text(), self.list1[i], player_points[self.list1[i]]))


                except:
                    logging.debug('error in operation!')
            fant.commit()
            self.file_evaluate()
        else:
            logging.debug('---error in operation')

    # QUITING METHOD
    def quit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setInformativeText(' Bye 😙')
        msg.setWindowTitle("Fantasy Cricket")
        msg.exec_()
        logging.debug('exit')
        sys.exit()

    # ON RADIOBUTTONS CLICKED
    def load_names(self):
        Batsman = 'BAT'
        WicketKeeper = 'WK'
        Allrounder = 'AR'
        Bowler = 'BWL'
        sql1 = "SELECT player,value from stats WHERE ctg = '" + Batsman + "';"
        sql2 = "SELECT Player,value from stats WHERE ctg = '" + WicketKeeper + "';"
        sql3 = "SELECT Player,value from stats WHERE ctg ='" + Allrounder + "';"
        sql4 = "SELECT Player,value from stats WHERE ctg = '" + Bowler + "';"

        fantcurs.execute(sql1)
        x = fantcurs.fetchall()
        fantcurs.execute(sql4)
        y = fantcurs.fetchall()
        fantcurs.execute(sql3)
        z = fantcurs.fetchall()
        fantcurs.execute(sql2)
        w = fantcurs.fetchall()

        batsmen = []
        bowlers = []
        allrounders = []
        wcktkeepers = []

        for k in x:
            batsmen.append(k[0])
            self.b.append(k[0])
            self.stats[k[0]] = k[1]
        for k in y:
            bowlers.append(k[0])
            self.stats[k[0]] = k[1]
            self.a.append(k[0])
        for k in w:
            wcktkeepers.append(k[0])
            self.stats[k[0]] = k[1]
            self.d.append(k[0])
        for k in z:
            allrounders.append(k[0])
            self.stats[k[0]] = k[1]
            self.c.append(k[0])
        for i in self.list1:
            if i in allrounders:
                allrounders.remove(i)
            elif i in batsmen:
                batsmen.remove(i)
            elif i in bowlers:
                bowlers.remove(i)
            elif i in wcktkeepers:
                wcktkeepers.remove(i)

        if self.bat_rb.isChecked() == True:
            self.availplayers_lw.clear()
            for i in range(len(batsmen)):
                item = QtWidgets.QListWidgetItem(batsmen[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.availplayers_lw.addItem(item)
        elif self.bow_rb.isChecked() == True:
            self.availplayers_lw.clear()
            for i in range(len(bowlers)):
                item = QtWidgets.QListWidgetItem(bowlers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.availplayers_lw.addItem(item)
        elif self.ar_rb.isChecked() == True:
            self.availplayers_lw.clear()
            for i in range(len(allrounders)):
                item = QtWidgets.QListWidgetItem(allrounders[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.availplayers_lw.addItem(item)

        elif self.wk_rb.isChecked() == True:
            self.availplayers_lw.clear()
            for i in range(len(wcktkeepers)):
                item = QtWidgets.QListWidgetItem(wcktkeepers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.availplayers_lw.addItem(item)

    def removelist1(self, item):  # REMOVE FROM AVAILABLE PLAYERS AND ADD TO SELECTED PLAYERS
        self.conditions_1(item.text())
        self.availplayers_lw.takeItem(self.availplayers_lw.row(item))
        self.selectedplayers_lw.addItem(item.text())
        self.totalcount = self.selectedplayers_lw.count()
        self.list1.append(item.text())
        self.error()

    def conditions_1(self, cat):  # Adding and Deducting respective points from points_calculator.py
        self.avail_points -= self.stats[cat]
        self.used_points += self.stats[cat]
        if cat in self.a:
            self.bowlerscount += 1
        elif cat in self.d:
            self.wicketerscount += 1
        elif cat in self.c:
            self.alrdscount += 1
        elif cat in self.b:
            self.batsmencount += 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.bowlcount.setText(str(self.bowlerscount))
        self.batcount.setText(str(self.batsmencount))
        self.alrcount.setText(str(self.alrdscount))
        self.wicketcount.setText(str(self.wicketerscount))

    def conditions_2(self, cat):  # Adding and Deducting respective poinrs from points_calculator.py
        self.avail_points += self.stats[cat]
        self.used_points -= self.stats[cat]
        if cat in self.a:
            self.bowlerscount -= 1
        elif cat in self.d:
            self.wicketerscount -= 1
        elif cat in self.c:
            self.alrdscount -= 1
        elif cat in self.b:
            self.batsmencount -= 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.bowlcount.setText(str(self.bowlerscount))
        self.batcount.setText(str(self.batsmencount))
        self.alrcount.setText(str(self.alrdscount))
        self.wicketcount.setText(str(self.wicketerscount))

    def removelist2(self, item):  # REMOVE FROM SELECTED PLAYERS AND ADD TO AVAIALBLE PLAYERS
        self.selectedplayers_lw.takeItem(self.selectedplayers_lw.row(item))
        self.availplayers_lw.addItem(item.text())
        self.list1.remove(item.text())
        # self.error()
        self.totalcount = self.selectedplayers_lw.count()
        self.conditions_2(item.text())

    def openteam(self):  # upon open team selected
        self.reset()
        teamname = self.open_screen.open_cb.currentText()
        self.team_name.setText(teamname)
        self.enablebuttons()
        fantcurs.execute("SELECT players from teams WHERE name= '" + teamname + "';")
        x = fantcurs.fetchall()
        score = []
        for i in x:
            fantcurs.execute("SELECT value from stats WHERE player='" + i[0] + "';")
            y = fantcurs.fetchone()
            score.append(y[0])
        logging.debug(score)
        sum = 0
        for i in score:
            sum += i
        self.selectedplayers_lw.clear()
        self.load_names()
        for i in x:
            self.selectedplayers_lw.addItem(i[0])
            self.list1.append(i[0])
            self.conditions_1(i[0])
        self.used_points = sum
        self.avail_points = 1000 - sum
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.openDialog.close()

    def enablebuttons(self):
        self.bat_rb.setEnabled(True)
        self.bow_rb.setEnabled(True)
        self.ar_rb.setEnabled(True)
        self.wk_rb.setEnabled(True)

    def error(self):  # Handling and displaying error messages
        msg = QMessageBox()
        if self.avail_points <= 0:
            self.points_available.setText('0')
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Not enough points!')
            msg.setWindowTitle("Selection Cricket")
            msg.exec_()
            return 0
        if self.wicketerscount > 1:
            msg.setIcon(QMessageBox.Critical)
            # msg.setText("Error")
            msg.setInformativeText('Only 1 wicketkeeper is allowed!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return 0
        if self.totalcount > 11:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('No more than 11 players allowed!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()
            logging.debug('available points',self.avail_points)
            return 0
        if self.totalcount < 11:
            return 0
        if self.wicketerscount < 1:
            return 0
        return 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
