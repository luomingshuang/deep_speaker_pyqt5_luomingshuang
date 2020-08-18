from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon 
 
class Ui_MainWindow_audio(object):
    def setupUi(self, MainWindow_audio):
        ###设置窗口名字和窗口大小
        MainWindow_audio.setObjectName("MainWindow_audio")
        MainWindow_audio.resize(1400, 800)
        MainWindow_audio.setMinimumSize(QtCore.QSize(1000, 580))
        MainWindow_audio.setMaximumSize(QtCore.QSize(1000, 580))

        self.centralwidget = QtWidgets.QWidget(MainWindow_audio)
        self.centralwidget.setObjectName("centralwidget")
        self.transcription_pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.transcription_pushButton.setStyleSheet("QPushButton{border-image: url(pngs/enroll2.png)}")
        self.transcription_pushButton.setToolTip('Please enroll audio data for recognition!')

        #self.transcription_pushButton.setGeometry(QtCore.QRect(300, 90, 140, 81))
        self.transcription_pushButton.move(250, 210)
        self.transcription_pushButton.resize(200, 200)

        #设置窗口标题与初始大小
        MainWindow_audio.setWindowTitle
        ("界面背景图片设置")
        MainWindow_audio.setWindowIcon(QIcon('pngs/windows0.jpeg')) #设置窗体标题图标
        ##设置窗口背景图片
        MainWindow_audio.setStyleSheet("#MainWindow_audio{border-image:url(./pngs/windows1.jpg);}")

        font = QtGui.QFont()
        font.setPointSize(20)
        self.transcription_pushButton.setFont(font)
        self.transcription_pushButton.setObjectName("transcription_pushButton")

        self.player_pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.player_pushButton.setStyleSheet("QPushButton{border-image: url(pngs/test2.png)}")
        self.player_pushButton.setToolTip('Please record audio data for recognition!')

        #self.player_pushButton.setGeometry(QtCore.QRect(600, 90, 141, 81))
        self.player_pushButton.move(600, 210)
        self.player_pushButton.resize(200, 200)

        
        font = QtGui.QFont()
        font.setPointSize(20)
        self.player_pushButton.setFont(font)
        self.player_pushButton.setObjectName("player_pushButton")

        MainWindow_audio.setCentralWidget(self.centralwidget)
 
        self.retranslateUi(MainWindow_audio)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_audio)
 
    def retranslateUi(self, MainWindow_audio):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_audio.setWindowTitle(_translate("MainWindow_audio", "声纹识别"))
        #self.transcription_pushButton.setText(_translate("MainWindow_audio", "Enroll"))
        #self.player_pushButton.setText(_translate("MainWindow_audio", "Test"))