from sys import flags
from typing import Collection
from PyQt5 import QtCore, QtGui, QtWidgets
from databaseModules import connector_01
from PyQt5.QtWidgets import QFileDialog, QHeaderView, QMessageBox , QTableWidgetItem
from PyQt5.QtGui import QCursor, QFont, QPixmap


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(860, 511)
                MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Arial Narrow")
                font.setPointSize(10)
                self.tabWidget.setFont(font)
                self.tabWidget.setTabletTracking(True)
                self.tabWidget.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
                self.tabWidget.setStyleSheet("")
                self.tabWidget.setObjectName("tabWidget")
                self.tab = QtWidgets.QWidget()
                self.tab.setStyleSheet("background-color: rgb(239, 239, 239);")
                self.tab.setObjectName("tab")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
                self.verticalLayout_2.setContentsMargins(6, -1, 6, -1)
                self.verticalLayout_2.setSpacing(4)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.frame = QtWidgets.QFrame(self.tab)
                self.frame.setMinimumSize(QtCore.QSize(0, 300))
                self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "border-radius:5px;")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.frame_3 = QtWidgets.QFrame(self.frame)
                self.frame_3.setMaximumSize(QtCore.QSize(450, 16777215))
                self.frame_3.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                                "border-radius:5px;")
                self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_3.setObjectName("frame_3")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.frame_5 = QtWidgets.QFrame(self.frame_3)
                self.frame_5.setMinimumSize(QtCore.QSize(20, 0))
                self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
                self.frame_5.setStyleSheet("background-color: rgb(58, 58, 58);\n"
                                                "border-radius:5px;\n"
                                                "color:white;")
                self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_5.setObjectName("frame_5")
                self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
                self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_7.setSpacing(0)
                self.verticalLayout_7.setObjectName("verticalLayout_7")
                self.label = QtWidgets.QLabel(self.frame_5)
                self.label.setObjectName("label")
                self.verticalLayout_7.addWidget(self.label)
                self.verticalLayout_3.addWidget(self.frame_5)
                self.frame_6 = QtWidgets.QFrame(self.frame_3)
                self.frame_6.setMinimumSize(QtCore.QSize(0, 200))
                self.frame_6.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                "border-radius:5px;")
                self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_6.setObjectName("frame_6")
                self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
                self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_8.setSpacing(0)
                self.verticalLayout_8.setObjectName("verticalLayout_8")
                self.label_2 = QtWidgets.QLabel(self.frame_6)
                self.label_2.setMinimumSize(QtCore.QSize(320, 250))
                self.label_2.setMaximumSize(QtCore.QSize(450, 450))
                self.label_2.setStyleSheet("")
                self.label_2.setText("")
                self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/ff.jpg"))
                self.label_2.setScaledContents(True)
                self.label_2.setWordWrap(True)
                self.label_2.setObjectName("label_2")
                self.verticalLayout_8.addWidget(self.label_2)
                self.verticalLayout_3.addWidget(self.frame_6)
                self.frame_7 = QtWidgets.QFrame(self.frame_3)
                self.frame_7.setMinimumSize(QtCore.QSize(0, 30))
                self.frame_7.setStyleSheet("background-color: rgb(241, 241, 241);\n"
                                                "border-radius:5px;")
                self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_7.setObjectName("frame_7")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setSpacing(4)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
                self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
                self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "border-radius:5px;")
                self.lineEdit.setObjectName("lineEdit")
                self.horizontalLayout_2.addWidget(self.lineEdit)


                self.pushButton = QtWidgets.QPushButton(self.frame_7)
                self.pushButton.setMinimumSize(QtCore.QSize(40, 25))
                self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
                self.pushButton.setStyleSheet("image: url(:/newPrefix/fileicon.png);")
                self.pushButton.setText("")
                self.pushButton.setIconSize(QtCore.QSize(30, 30))
                self.pushButton.setObjectName("pushButton")
                self.horizontalLayout_2.addWidget(self.pushButton)
                self.pushButton.setIcon(QtGui.QIcon(r'E:\Final_year_project\btd_final_project\uIModule\fileicon.png'))
                self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


                self.verticalLayout_3.addWidget(self.frame_7)
                self.horizontalLayout.addWidget(self.frame_3)
                self.frame_4 = QtWidgets.QFrame(self.frame)
                self.frame_4.setMinimumSize(QtCore.QSize(480, 0))
                self.frame_4.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                                "border-radius:5px;")
                self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_4.setObjectName("frame_4")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.frame_8 = QtWidgets.QFrame(self.frame_4)
                self.frame_8.setMinimumSize(QtCore.QSize(0, 0))
                self.frame_8.setMaximumSize(QtCore.QSize(16777215, 40))
                self.frame_8.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                                "border-radius:5px;")
                self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_8.setObjectName("frame_8")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.label_4 = QtWidgets.QLabel(self.frame_8)
                font = QtGui.QFont()
                font.setFamily("Myanmar Text")
                font.setPointSize(14)
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.horizontalLayout_4.addWidget(self.label_4)
                self.verticalLayout_4.addWidget(self.frame_8)
                self.frame_9 = QtWidgets.QFrame(self.frame_4)
                self.frame_9.setMinimumSize(QtCore.QSize(0, 210))
                self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "border-radius:5px;")
                self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_9.setObjectName("frame_9")
                self.gridLayout = QtWidgets.QGridLayout(self.frame_9)
                self.gridLayout.setObjectName("gridLayout")
                self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_9)
                self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 33))
                self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 70))
                self.lineEdit_2.setStyleSheet("border:1px solid grey;")
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.gridLayout.addWidget(self.lineEdit_2, 0, 0, 1, 1)


               



                self.comboBox = QtWidgets.QComboBox(self.frame_9)
                self.comboBox.setMinimumSize(QtCore.QSize(200, 33))
                self.comboBox.setMaximumSize(QtCore.QSize(16777215, 70))
                self.comboBox.setStyleSheet("border:1px solid grey;")
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
                self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_9)
                self.lineEdit_4.setMinimumSize(QtCore.QSize(200, 33))
                self.lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 70))
                self.lineEdit_4.setStyleSheet("border:1px solid grey;")
                self.lineEdit_4.setObjectName("lineEdit_4")
                self.gridLayout.addWidget(self.lineEdit_4, 1, 0, 1, 1)
                self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_9)
                self.lineEdit_5.setMinimumSize(QtCore.QSize(200, 33))
                self.lineEdit_5.setMaximumSize(QtCore.QSize(16777215, 70))
                self.lineEdit_5.setStyleSheet("border:1px solid grey;")
                self.lineEdit_5.setObjectName("lineEdit_5")
                self.gridLayout.addWidget(self.lineEdit_5, 1, 1, 1, 1)
                self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_9)
                self.lineEdit_6.setMinimumSize(QtCore.QSize(200, 33))
                self.lineEdit_6.setMaximumSize(QtCore.QSize(16777215, 70))
                self.lineEdit_6.setStyleSheet("border:1px solid grey;")
                self.lineEdit_6.setObjectName("lineEdit_6")
                self.gridLayout.addWidget(self.lineEdit_6, 2, 0, 1, 1)
                self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_9)
                self.lineEdit_7.setMinimumSize(QtCore.QSize(200, 33))
                self.lineEdit_7.setMaximumSize(QtCore.QSize(16777215, 70))
                self.lineEdit_7.setStyleSheet("border:1px solid grey;")
                self.lineEdit_7.setObjectName("lineEdit_7")
                self.gridLayout.addWidget(self.lineEdit_7, 2, 1, 1, 1)
                self.verticalLayout_4.addWidget(self.frame_9)
                self.frame_10 = QtWidgets.QFrame(self.frame_4)
                self.frame_10.setMinimumSize(QtCore.QSize(0, 25))
                self.frame_10.setMaximumSize(QtCore.QSize(16777215, 40))
                self.frame_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "border-radius:5px;")
                self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_10.setObjectName("frame_10")
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_10)
                self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.radioButton = QtWidgets.QRadioButton(self.frame_10)
                self.radioButton.setMinimumSize(QtCore.QSize(320, 20))
                self.radioButton.setStyleSheet("background-color: rgb(24, 141, 13);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "padding:10px;")
                self.radioButton.setObjectName("radioButton")
                self.horizontalLayout_5.addWidget(self.radioButton)
                self.pushButton_2 = QtWidgets.QPushButton(self.frame_10)
                self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
                self.pushButton_2.setStyleSheet("background-color: rgb(19, 141, 255);\n"
                                                "color: rgb(255, 255, 255);")
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                self.horizontalLayout_5.addWidget(self.pushButton_2)
                self.verticalLayout_4.addWidget(self.frame_10)
                self.horizontalLayout.addWidget(self.frame_4)
                self.verticalLayout_2.addWidget(self.frame)
                self.frame_2 = QtWidgets.QFrame(self.tab)
                self.frame_2.setMaximumSize(QtCore.QSize(16777215, 300))
                self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "border-radius:5px;")
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
                self.verticalLayout_5.setContentsMargins(-1, 4, -1, 4)
                self.verticalLayout_5.setSpacing(5)
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.frame_11 = QtWidgets.QFrame(self.frame_2)
                self.frame_11.setMinimumSize(QtCore.QSize(0, 5))
                self.frame_11.setMaximumSize(QtCore.QSize(16777215, 5))
                self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_11.setObjectName("frame_11")
                self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_11)
                self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_6.setSpacing(0)
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                self.progressBar = QtWidgets.QProgressBar(self.frame_11)
                self.progressBar.setMinimumSize(QtCore.QSize(0, 3))
                self.progressBar.setMaximumSize(QtCore.QSize(16777215, 3))
                self.progressBar.setProperty("value", 24)
                self.progressBar.setObjectName("progressBar")
                self.verticalLayout_6.addWidget(self.progressBar)
                self.verticalLayout_5.addWidget(self.frame_11)
                self.frame_12 = QtWidgets.QFrame(self.frame_2)
                self.frame_12.setMinimumSize(QtCore.QSize(0, 15))
                self.frame_12.setMaximumSize(QtCore.QSize(16777215, 20))
                self.frame_12.setStyleSheet("background-color: rgb(58, 58, 58);\n"
                                                "border-radius:5px;")
                self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_12.setObjectName("frame_12")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_12)
                self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_3.setSpacing(0)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.label_3 = QtWidgets.QLabel(self.frame_12)
                self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_3.setObjectName("label_3")
                self.horizontalLayout_3.addWidget(self.label_3)
                self.verticalLayout_5.addWidget(self.frame_12)
                self.frame_13 = QtWidgets.QFrame(self.frame_2)
                self.frame_13.setMinimumSize(QtCore.QSize(0, 70))
                self.frame_13.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                                "border-radius:5px;\n"
                                                "border:2px solid grey;")
                self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_13.setObjectName("frame_13")
                self.verticalLayout_5.addWidget(self.frame_13)
                self.verticalLayout_2.addWidget(self.frame_2)
                self.tabWidget.addTab(self.tab, "")
                self.tab_2 = QtWidgets.QWidget()
                self.tab_2.setObjectName("tab_2")
                self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_2)
                self.verticalLayout_9.setContentsMargins(6, 9, 6, 9)
                self.verticalLayout_9.setSpacing(4)
                self.verticalLayout_9.setObjectName("verticalLayout_9")
                self.frame_14 = QtWidgets.QFrame(self.tab_2)
                self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_14.setObjectName("frame_14")
                self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_14)
                self.verticalLayout_10.setObjectName("verticalLayout_10")
                self.frame_15 = QtWidgets.QFrame(self.frame_14)
                self.frame_15.setMinimumSize(QtCore.QSize(0, 280))
                self.frame_15.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                                "border-radius:5px;")
                self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_15.setObjectName("frame_15")
                self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_15)
                self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_11.setSpacing(0)
                self.verticalLayout_11.setObjectName("verticalLayout_11")

                self.tableWidget = QtWidgets.QTableWidget(self.frame_15)
                self.tableWidget.setMinimumSize(QtCore.QSize(0, 280))
                self.tableWidget.setObjectName("tableWidget")
                self.tableWidget.setColumnCount(0)
                self.tableWidget.setRowCount(0)
                self.verticalLayout_11.addWidget(self.tableWidget)
                self.tableWidget.setColumnCount(7)
                # self.tableWidget.setVerticalHeaderLabels([''])
                self.tableWidget.setHorizontalHeaderLabels(['ID',"First name","Last name","Age","Gender","Contact Number","Address"])
                

                # self.tableWidget.setItem(3, 5,QTableWidgetItem())
                # self.tableWidget.item(3, 5).setBackground(QtGui.QColor(100,100,150))
                
                # Making column Width Max width 
                header = self.tableWidget.horizontalHeader()       
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
                



                self.verticalLayout_10.addWidget(self.frame_15)
                self.frame_16 = QtWidgets.QFrame(self.frame_14)
                self.frame_16.setMinimumSize(QtCore.QSize(0, 200))
                self.frame_16.setMaximumSize(QtCore.QSize(16777215, 200))
                self.frame_16.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                                "border-radius:5px;")
                self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_16.setObjectName("frame_16")
                self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_16)
                self.verticalLayout_12.setObjectName("verticalLayout_12")
                self.frame_17 = QtWidgets.QFrame(self.frame_16)
                self.frame_17.setMinimumSize(QtCore.QSize(0, 10))
                self.frame_17.setMaximumSize(QtCore.QSize(16777215, 30))
                self.frame_17.setStyleSheet("background-color: rgb(58, 58, 58);\n"
                                                "border-radius:5px;")
                self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_17.setObjectName("frame_17")
                self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_17)
                self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_13.setSpacing(0)
                self.verticalLayout_13.setObjectName("verticalLayout_13")
                self.label_5 = QtWidgets.QLabel(self.frame_17)
                self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_5.setObjectName("label_5")
                self.verticalLayout_13.addWidget(self.label_5)
                self.verticalLayout_12.addWidget(self.frame_17)
                self.frame_18 = QtWidgets.QFrame(self.frame_16)
                self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_18.setObjectName("frame_18")
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_18)
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.frame_19 = QtWidgets.QFrame(self.frame_18)
                self.frame_19.setMinimumSize(QtCore.QSize(50, 0))
                self.frame_19.setMaximumSize(QtCore.QSize(150, 16777215))
                self.frame_19.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                                "border-radius:5px;")
                self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_19.setObjectName("frame_19")
                self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_19)
                self.verticalLayout_14.setObjectName("verticalLayout_14")
                self.label_6 = QtWidgets.QLabel(self.frame_19)
                self.label_6.setObjectName("label_6")
                self.verticalLayout_14.addWidget(self.label_6)
                self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_19)
                self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 35))
                self.lineEdit_3.setStyleSheet("border:1px solid grey;\n"
                                                "background-color: rgb(255, 255, 255);")
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.verticalLayout_14.addWidget(self.lineEdit_3)
                self.horizontalLayout_6.addWidget(self.frame_19)
                self.frame_20 = QtWidgets.QFrame(self.frame_18)
                self.frame_20.setStyleSheet("")
                self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_20.setObjectName("frame_20")
                self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_20)
                self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_15.setSpacing(5)
                self.verticalLayout_15.setObjectName("verticalLayout_15")
                self.frame_21 = QtWidgets.QFrame(self.frame_20)
                self.frame_21.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                                "border-radius:5px;")
                self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_21.setObjectName("frame_21")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_21)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_21)
                self.lineEdit_8.setMinimumSize(QtCore.QSize(180, 33))
                self.lineEdit_8.setMaximumSize(QtCore.QSize(16777215, 70))
                self.lineEdit_8.setStyleSheet("border:1px solid grey;")
                self.lineEdit_8.setObjectName("lineEdit_8")
                self.gridLayout_2.addWidget(self.lineEdit_8, 0, 0, 1, 1)
                self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_21)
                self.lineEdit_9.setMinimumSize(QtCore.QSize(180, 33))
                self.lineEdit_9.setMaximumSize(QtCore.QSize(16777215, 70))
                self.lineEdit_9.setStyleSheet("border:1px solid grey;")
                self.lineEdit_9.setObjectName("lineEdit_9")
                self.gridLayout_2.addWidget(self.lineEdit_9, 0, 1, 1, 1)
                self.comboBox_2 = QtWidgets.QComboBox(self.frame_21)
                self.comboBox_2.setMinimumSize(QtCore.QSize(180, 33))
                self.comboBox_2.setMaximumSize(QtCore.QSize(16777215, 70))
                self.comboBox_2.setStyleSheet("border:1px solid grey;")
                self.comboBox_2.setObjectName("comboBox_2")
                self.comboBox_2.addItem("")
                self.comboBox_2.addItem("")
                self.comboBox_2.addItem("")
                self.gridLayout_2.addWidget(self.comboBox_2, 0, 2, 1, 1)
                self.comboBox_2.setEnabled(False)
                self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_21)
                self.lineEdit_10.setMinimumSize(QtCore.QSize(180, 33))
                self.lineEdit_10.setMaximumSize(QtCore.QSize(16777215, 70))
                self.lineEdit_10.setStyleSheet("border:1px solid grey;")
                self.lineEdit_10.setObjectName("lineEdit_10")
                self.gridLayout_2.addWidget(self.lineEdit_10, 1, 0, 1, 1)
                self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_21)
                self.lineEdit_11.setMinimumSize(QtCore.QSize(180, 33))
                self.lineEdit_11.setMaximumSize(QtCore.QSize(16777215, 70))
                self.lineEdit_11.setStyleSheet("border:1px solid grey;")
                self.lineEdit_11.setObjectName("lineEdit_11")
                self.gridLayout_2.addWidget(self.lineEdit_11, 1, 1, 1, 1)
                self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_21)
                self.lineEdit_12.setMinimumSize(QtCore.QSize(180, 33))
                self.lineEdit_12.setMaximumSize(QtCore.QSize(16777215, 70))
                self.lineEdit_12.setStyleSheet("border:1px solid grey;")
                self.lineEdit_12.setObjectName("lineEdit_12")
                self.gridLayout_2.addWidget(self.lineEdit_12, 1, 2, 1, 1)
                self.verticalLayout_15.addWidget(self.frame_21)
                self.frame_22 = QtWidgets.QFrame(self.frame_20)
                self.frame_22.setMinimumSize(QtCore.QSize(0, 30))
                self.frame_22.setMaximumSize(QtCore.QSize(16777215, 40))
                self.frame_22.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                                "border-radius:5px;")
                self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_22.setObjectName("frame_22")
                self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_22)
                self.horizontalLayout_7.setObjectName("horizontalLayout_7")
                self.pushButton_3 = QtWidgets.QPushButton(self.frame_22)
                self.pushButton_3.setMinimumSize(QtCore.QSize(0, 25))
                self.pushButton_3.setStyleSheet("background-color: rgb(19, 141, 255);\n"
                                                "color: rgb(255, 255, 255);")
                self.pushButton_3.setObjectName("pushButton_3")
                self.horizontalLayout_7.addWidget(self.pushButton_3)
                self.pushButton_4 = QtWidgets.QPushButton(self.frame_22)
                self.pushButton_4.setMinimumSize(QtCore.QSize(0, 25))
                self.pushButton_4.setStyleSheet("background-color: rgb(19, 141, 255);\n"
                                                "color: rgb(255, 255, 255);")
                self.pushButton_4.setObjectName("pushButton_4")
                self.horizontalLayout_7.addWidget(self.pushButton_4)
                self.pushButton_5 = QtWidgets.QPushButton(self.frame_22)
                self.pushButton_5.setMinimumSize(QtCore.QSize(0, 25))
                self.pushButton_5.setStyleSheet("background-color: rgb(19, 141, 255);\n"
                                                "color: rgb(255, 255, 255);")
                self.pushButton_5.setObjectName("pushButton_5")
                self.horizontalLayout_7.addWidget(self.pushButton_5)
                self.pushButton_6 = QtWidgets.QPushButton(self.frame_22)
                self.pushButton_6.setMinimumSize(QtCore.QSize(0, 25))
                self.pushButton_6.setStyleSheet("background-color: rgb(19, 141, 255);\n"
                                                "color: rgb(255, 255, 255);")
                self.pushButton_6.setObjectName("pushButton_6")
                self.horizontalLayout_7.addWidget(self.pushButton_6)
                self.verticalLayout_15.addWidget(self.frame_22)
                self.horizontalLayout_6.addWidget(self.frame_20)
                self.verticalLayout_12.addWidget(self.frame_18)
                self.verticalLayout_10.addWidget(self.frame_16)
                self.verticalLayout_9.addWidget(self.frame_14)
                self.tabWidget.addTab(self.tab_2, "")
                self.tab_3 = QtWidgets.QWidget()
                self.tab_3.setObjectName("tab_3")
                self.tabWidget.addTab(self.tab_3, "")
                self.verticalLayout.addWidget(self.tabWidget)
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 21))
                self.menubar.setObjectName("menubar")
                self.menuFile = QtWidgets.QMenu(self.menubar)
                self.menuFile.setObjectName("menuFile")
                self.menuSettings = QtWidgets.QMenu(self.menubar)
                self.menuSettings.setObjectName("menuSettings")
                self.menuhelp = QtWidgets.QMenu(self.menubar)
                self.menuhelp.setObjectName("menuhelp")
                self.menuAbout = QtWidgets.QMenu(self.menubar)
                self.menuAbout.setObjectName("menuAbout")
                MainWindow.setMenuBar(self.menubar)
                self.menubar.addAction(self.menuFile.menuAction())
                self.menubar.addAction(self.menuSettings.menuAction())
                self.menubar.addAction(self.menuhelp.menuAction())
                self.menubar.addAction(self.menuAbout.menuAction())

                self.retranslateUi(MainWindow)
                self.tabWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate(
                        "MainWindow", "Brain Tumor Detector"))
                self.label.setText(_translate(
                        "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">MRI Image</span></p></body></html>"))
                self.lineEdit.setPlaceholderText(
                        _translate("MainWindow", "Add image  . . . "))
                self.label_4.setText(_translate(
                        "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Patient Details</span></p></body></html>"))
                self.lineEdit_2.setPlaceholderText(
                        _translate("MainWindow", "First name"))
                self.comboBox.setCurrentText(_translate("MainWindow", "Male"))
                self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
                self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
                self.comboBox.setItemText(2, _translate("MainWindow", "Others"))
                self.lineEdit_4.setPlaceholderText(
                        _translate("MainWindow", "Last name"))
                self.lineEdit_5.setPlaceholderText(
                        _translate("MainWindow", "Age"))
                self.lineEdit_6.setPlaceholderText(
                        _translate("MainWindow", "Contact number"))
                self.lineEdit_7.setPlaceholderText(
                        _translate("MainWindow", "Address"))
                self.radioButton.setText(_translate(
                        "MainWindow", "Add patients data to Dataset"))
                self.pushButton_2.setText(_translate("MainWindow", "Start Detection"))
                self.label_3.setText(_translate(
                        "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Analysis Results</span></p></body></html>"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(
                        self.tab), _translate("MainWindow", "Analysis"))
                self.label_5.setText(_translate(
                        "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Run Operations On Database</span></p></body></html>"))
                self.label_6.setText(_translate(
                        "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Search Patient ID</span></p></body></html>"))
                self.lineEdit_8.setPlaceholderText(
                        _translate("MainWindow", "First name  . . . "))
                self.lineEdit_9.setPlaceholderText(
                        _translate("MainWindow", "Last name  . . . "))
                self.comboBox_2.setCurrentText(_translate("MainWindow", "Male"))
                self.comboBox_2.setItemText(0, _translate("MainWindow", "Male"))
                self.comboBox_2.setItemText(1, _translate("MainWindow", "Female"))
                self.comboBox_2.setItemText(2, _translate("MainWindow", "Others"))
                self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "Age"))
                self.lineEdit_11.setPlaceholderText(
                        _translate("MainWindow", "Contact num"))
                self.lineEdit_12.setPlaceholderText(
                        _translate("MainWindow", "Address"))
                self.pushButton_3.setText(_translate("MainWindow", "Update"))
                self.pushButton_4.setText(_translate("MainWindow", "Delete"))
                self.pushButton_5.setText(_translate("MainWindow", "Clear"))
                self.pushButton_6.setText(_translate("MainWindow", "Refresh table"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(
                        self.tab_2), _translate("MainWindow", "Patient Records"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(
                        self.tab_3), _translate("MainWindow", "Model Analysis"))
                self.menuFile.setTitle(_translate("MainWindow", "File"))
                self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
                self.menuhelp.setTitle(_translate("MainWindow", "help"))
                self.menuAbout.setTitle(_translate("MainWindow", "About"))


                # Setting up the font sizes 
                self.lineEdit_2.setFont(QFont( "Timers" , 12 ,  QFont.Bold) )
                self.lineEdit_4.setFont(QFont( "Timers" , 12 ,  QFont.Bold) )
                self.lineEdit_5.setFont(QFont( "Timers" , 12 ,  QFont.Bold) )
                self.lineEdit_6.setFont(QFont( "Timers" , 12 ,  QFont.Bold) )
                self.lineEdit_7.setFont(QFont( "Timers" , 12 ,  QFont.Bold) )


                # Adding event Listers on button 
                self.pushButton_6.clicked.connect(self.load_table_data)

                # For search id event 
                self.lineEdit_3.textChanged.connect(self.on_id_search)

                # Update feature
                self.pushButton_3.clicked.connect(self.update_data)

                # Deleting row
                self.pushButton_4.clicked.connect(self.delete_data)

                # Add data in table
                self.pushButton_2.clicked.connect(self.add_data)

                # IMage Selector
                self.pushButton.clicked.connect(self.open_file_selector)

                # Clear lin-edit features
                self.pushButton_5.clicked.connect(self.clear_lineEdits)

        def load_table_data(self):  
                self.tableWidget.setRowCount(0)

                connection1 = connector_01.CustomConnector()

                connection1.execute('SELECT * FROM btd.patient;')
                data = connection1.myCursor.fetchall()


                self.tableWidget.verticalHeader().setVisible(False)
                print(data)
                for items in data:
                        # Creats empty row 
                        rowPosition = self.tableWidget.rowCount()
                        self.tableWidget.insertRow(rowPosition)

                        self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(f"{items[0]}"))
                        self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(f"{items[1]}"))
                        self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(f"{items[2]}"))
                        self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(f"{items[3]}"))
                        self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(f"{items[4]}"))
                        self.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(f"{items[5]}"))
                        self.tableWidget.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(f"{items[6]}"))

                        self.tableWidget.item(rowPosition,0).setBackground(QtGui.QColor(185, 255, 187))
                        self.tableWidget.item(rowPosition,1).setBackground(QtGui.QColor(185, 255, 187))
                        self.tableWidget.item(rowPosition,2).setBackground(QtGui.QColor(185, 255, 187))
                        self.tableWidget.item(rowPosition,3).setBackground(QtGui.QColor(185, 255, 187))
                        self.tableWidget.item(rowPosition,4).setBackground(QtGui.QColor(185, 255, 187))
                        self.tableWidget.item(rowPosition,5).setBackground(QtGui.QColor(185, 255, 187))
                        self.tableWidget.item(rowPosition,6).setBackground(QtGui.QColor(185, 255, 187))


                connection1.exit_database()

        def clear_lineEdits(self):
                self.lineEdit_8.clear()
                self.lineEdit_9.clear()
                self.lineEdit_10.clear()
                self.lineEdit_11.clear()
                self.lineEdit_12.clear()
                self.lineEdit_3.clear()
                self.comboBox_2.setEnabled(False)

        def on_id_search(self):
                connection1 = connector_01.CustomConnector()
                id = self.lineEdit_3.text()
                try:
                        if(id != '' and id != " " and int(id)):
                                connection1.execute(f'SELECT * FROM btd.patient WHERE id={id}')
                                data = connection1.myCursor.fetchall()


                                print(data)
                                self.lineEdit_8.setText(f"{data[0][1]}")
                                self.lineEdit_9.setText(f"{data[0][2]}")
                                self.lineEdit_10.setText(f"{data[0][3]}")
                                self.lineEdit_11.setText(f"{data[0][5]}")
                                self.lineEdit_12.setText(f"{data[0][6]}")
                                self.comboBox_2.setEnabled(True)
                                if(data[0][4]=='M'):
                                        self.comboBox_2.setCurrentIndex(0)
                                else:
                                        self.comboBox_2.setCurrentIndex(1)
                except Exception as e:
                        print(e)        


                                


                connection1.exit_database()

        def add_data(self):
                connection1 = connector_01.CustomConnector()

                fname = self.lineEdit_2.text()
                lname = self.lineEdit_4.text()
                age = self.lineEdit_5.text()
                contact_num = self.lineEdit_6.text()
                address = self.lineEdit_7.text()
                if(self.comboBox.currentIndex() == 0):
                        gender = 'M'
                else:
                        gender = 'F'
                
                try:
                       connection1.execute(f"INSERT INTO btd.patient (first_name,last_name,age,gender,contact_num,address) VALUES ('{fname}','{lname}',{age},'{gender}','{contact_num}','{address}')")
                       connection1.connection.commit()
                       self.messageBox("add")
                except Exception as e:
                        print(e)
                        self.messageBox("empty")


                print("Data Added")

               
                self.lineEdit_2.clear()
                self.lineEdit_4.clear()
                self.lineEdit_5.clear()
                self.lineEdit_6.clear()
                self.lineEdit_7.clear()
                self.comboBox.setCurrentIndex(0)
                
                
                self.load_table_data()


                connection1.exit_database()

        def update_data(self):
                connection1 = connector_01.CustomConnector()

                id = self.lineEdit_3.text()

                fname = self.lineEdit_8.text()
                lname = self.lineEdit_9.text()
                age = self.lineEdit_10.text()
                self.comboBox_2.setEnabled(True)
                contact_num = self.lineEdit_11.text()
                address = self.lineEdit_12.text()
                if(self.comboBox_2.currentIndex() == 0):
                        gender = 'M'
                else:
                        gender = 'F'

                if(id != '' and id != " "):
                        connection1.execute(f"UPDATE btd.patient SET first_name = '{fname}',last_name = '{lname}',age = {age},gender = '{gender}',contact_num = '{contact_num}',address = '{address}' WHERE id={id}")
                        # data = connection1.myCursor.fetchall()

                        connection1.connection.commit()

                        self.messageBox("update")
                else:
                        self.messageBox("empty")

                self.load_table_data()
                self.clear_lineEdits()


                connection1.exit_database()
                
        def delete_data(self):
                connection1 = connector_01.CustomConnector()

                id = self.lineEdit_3.text()

                if(id != '' and id != " "):
                        connection1.execute(f"DELETE FROM btd.patient WHERE id={id}")
                        connection1.connection.commit()


                        print("Data Deleted")
                        self.load_table_data()
                        self.clear_lineEdits()
                        
                        self.messageBox("delete")
                else:
                        self.messageBox("empty")
                
                
     
                connection1.exit_database()

        def open_file_selector(self):
                
                fname = QFileDialog.getOpenFileName(self.centralwidget,'Open File', 'c\\','Image files (*.png *.jpg *.jpeg)')
                imgPath = fname[0]
                print(imgPath)
                self.lineEdit.setText(imgPath)

                pixmap = QPixmap(f"{imgPath}")
                self.label_2.setPixmap(pixmap)
                

        def messageBox(self,text):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Brain Tumor Detection")
                msg.setStyleSheet(r"QLabel{width: 140px;}");

                if(text=='delete'):
                        msg.setText(f"Row has been deleted sucessfully")
                        msg.setIcon(QMessageBox.Information)
                        msg.exec_()
                elif(text=='add'):
                        msg.setText(f"Patient Details has been submitted sucessfully")
                        msg.setIcon(QMessageBox.Information)
                        msg.exec_()
                elif(text=='update'):
                        msg.setText(f"Row has been updated sucessfully")
                        msg.setIcon(QMessageBox.Information)
                        msg.exec_()
                elif(text=='empty'):
                        msg.setText(f"Cannto submit empty form")
                        msg.setIcon(QMessageBox.Critical)
                        msg.exec_()
                

                




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
