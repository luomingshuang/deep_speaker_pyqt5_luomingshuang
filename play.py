from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon 
 
class Ui_MainWindow_player(object):
    def setupUi(self, MainWindow_player):
        MainWindow_player.setObjectName("MainWindow_player")
       # MainWindow_player.resize(507, 318)
        MainWindow_player.resize(1400, 600)
        MainWindow_player.setMinimumSize(QtCore.QSize(1000, 580))
        MainWindow_player.setMaximumSize(QtCore.QSize(1000, 580))

        MainWindow_player.setWindowIcon(QIcon('pngs/mainwindows.jpeg')) #设置窗体标题图标
        ##设置窗口背景图片
        MainWindow_player.setStyleSheet("#MainWindow_player{border-image:url(./pngs/mainwindows.jpeg);}")

        self.centralwidget = QtWidgets.QWidget(MainWindow_player)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(180, 0, 21, 321))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.player_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.player_pushButton.setGeometry(QtCore.QRect(290, 120, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.player_pushButton.setFont(font)
        self.player_pushButton.setObjectName("player_pushButton")
        MainWindow_player.setCentralWidget(self.centralwidget)
 
        self.retranslateUi(MainWindow_player)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_player)
 
    def retranslateUi(self, MainWindow_player):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_player.setWindowTitle(_translate("MainWindow_player", "声纹识别"))
        self.comboBox.setItemText(0, _translate("MainWindow_player", "音频文件列表"))
        self.player_pushButton.setText(_translate("MainWindow_player", "播放"))