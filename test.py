from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QFont, QPalette
from PyQt5.QtCore import pyqtSlot, Qt

speaker_label = 'who?'

class Ui_MainWindow_test(object):
    def setupUi(self, MainWindow_transcription):
        #self.speaker_label = 'who?'
        MainWindow_transcription.setObjectName("MainWindow_transcription")
        MainWindow_transcription.resize(1000, 600)
        MainWindow_transcription.setMinimumSize(QtCore.QSize(1000, 580))
        MainWindow_transcription.setMaximumSize(QtCore.QSize(1000, 580))
        
        MainWindow_transcription.setLayoutDirection(QtCore.Qt.LeftToRight)

        MainWindow_transcription.setWindowIcon(QIcon('pngs/windows2.jpg')) #设置窗体标题图标
        ##设置窗口背景图片
        MainWindow_transcription.setStyleSheet("#MainWindow_transcription{border-image:url(./pngs/windows0.jpeg);}")

        self.centralwidget = QtWidgets.QWidget(MainWindow_transcription)
        self.centralwidget.setObjectName("centralwidget")

        # self.line = QtWidgets.QFrame(self.centralwidget)
        # self.line.setGeometry(QtCore.QRect(210, 0, 15, 600))
        # self.line.setLineWidth(2)
        # self.line.setFrameShape(QtWidgets.QFrame.VLine)
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line.setObjectName("line")
        ###设置颜色
        pe = QPalette()
        pe.setColor(QPalette.WindowText,Qt.red)

        #####显示说话人和分数
        font = QtGui.QFont()
        font.setPointSize(20)

        self.speaker_label = QLabel(self)
        self.speaker_label.setText('Speaker: ?')
        self.speaker_label.setFont(font)

        self.speaker_label.resize(400, 50)
        self.speaker_label.setFont(QFont("Roman times", 20, QFont.Bold))
        self.speaker_label.move(350, 350)

        self.speaker_label.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        pe.setColor(QPalette.Background,Qt.gray)
        self.speaker_label.setPalette(pe)
        #speaker_label.show()

        self.score_label = QLabel(self)
        self.score_label.setText('Score: ?')
        self.score_label.setFont(font)

        self.score_label.resize(400, 50)
        self.score_label.setFont(QFont("Roman times", 20, QFont.Bold))
        self.score_label.move(350, 420)

        self.score_label.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        pe.setColor(QPalette.Background,Qt.gray)
        self.score_label.setPalette(pe)

        self.speaking_content = QLabel(self)
        self.speaking_content.setText('Content: ?')
        self.speaking_content.setFont(font)

        self.speaking_content.resize(400, 50)
        self.speaking_content.setFont(QFont("Roman times", 20, QFont.Bold))
        self.speaking_content.move(350, 490)

        self.speaking_content.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        pe.setColor(QPalette.Background,Qt.gray)
        self.speaking_content.setPalette(pe)

        self.record_pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.record_pushButton.setGeometry(QtCore.QRect(260, 160, 61, 41))
        #font = QtGui.QFont()
        #font.setPointSize(14)
        #self.record_pushButton.setFont(font)
        self.record_pushButton.setObjectName("record_pushButton")

        self.record_pushButton.setStyleSheet("QPushButton{border-image: url(pngs/start1.png)}")
        self.record_pushButton.setToolTip('START!')

        #self.transcription_pushButton.setGeometry(QtCore.QRect(300, 90, 140, 81))
        self.record_pushButton.move(260, 200)
        self.record_pushButton.resize(140, 140)
        
        ###显示时间###
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(460, 80, 160, 81))
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setObjectName("lcdNumber")

        self.pause_pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.pause_pushButton.setGeometry(QtCore.QRect(370, 160, 61, 41))
        #font = QtGui.QFont()
        #font.setPointSize(14)
        #self.pause_pushButton.setFont(font)
        self.pause_pushButton.setObjectName("pause_pushButton")

        self.pause_pushButton.setStyleSheet("QPushButton{border-image: url(pngs/stop1.png)}")
        self.pause_pushButton.setToolTip('STOP!')

        #self.transcription_pushButton.setGeometry(QtCore.QRect(300, 90, 140, 81))
        self.pause_pushButton.move(700, 200)
        self.pause_pushButton.resize(140, 140)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(5, 40, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")

        MainWindow_transcription.setCentralWidget(self.centralwidget)
 
        self.retranslateUi(MainWindow_transcription)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_transcription)
 
    def retranslateUi(self, MainWindow_transcription):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_transcription.setWindowTitle(_translate("MainWindow_transcription", "TEST"))
        #self.record_pushButton.setText(_translate("MainWindow_transcription", "录制"))
        #self.pause_pushButton.setText(_translate("MainWindow_transcription", "停止"))
        self.comboBox.setItemText(0, _translate("MainWindow_transcription", "测试音频文件列表"))