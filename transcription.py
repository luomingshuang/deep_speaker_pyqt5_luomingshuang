from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
from PyQt5.QtCore import pyqtSlot, Qt

class Ui_MainWindow_transcription(object):
    def setupUi(self, MainWindow_transcription):
        MainWindow_transcription.setObjectName("MainWindow_transcription")
        MainWindow_transcription.resize(1500, 600)
        #MainWindow_player.resize(1400, 600)
        MainWindow_transcription.setMinimumSize(QtCore.QSize(1500, 580))
        MainWindow_transcription.setMaximumSize(QtCore.QSize(1500, 580))
        
        MainWindow_transcription.setLayoutDirection(QtCore.Qt.LeftToRight)

        MainWindow_transcription.setWindowIcon(QIcon('pngs/windows0.jpeg')) #设置窗体标题图标
        ##设置窗口背景图片

        MainWindow_transcription.setStyleSheet("#MainWindow_transcription{border-image:url(./pngs/windows_enroll.jpg);}")

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
        pe.setColor(QPalette.WindowText,Qt.white)

        #####显示说话人和分数
        font = QtGui.QFont()
        font.setPointSize(10)

        self.speaker_label = QLabel(self)
        self.speaker_label.setText('您请说：8346175')
        self.speaker_label.setFont(font)

        self.speaker_label.resize(300, 30)
        self.speaker_label.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label.move(20, 100)

        self.speaker_label.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label.setPalette(pe)
        #speaker_label.show()

        self.speaker_label1 = QLabel(self)
        self.speaker_label1.setText('您请说：白日依山尽，黄河入海流')
        self.speaker_label1.setFont(font)

        self.speaker_label1.resize(600, 30)
        self.speaker_label1.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label1.move(20, 150)

        self.speaker_label1.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label1.setPalette(pe)

        self.speaker_label2 = QLabel(self)
        self.speaker_label2.setText('您请说：风雨送春归，飞雪迎春到')
        self.speaker_label2.setFont(font)

        self.speaker_label2.resize(600, 30)
        self.speaker_label2.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label2.move(20, 200)

        self.speaker_label2.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label2.setPalette(pe)

        self.speaker_label3 = QLabel(self)
        self.speaker_label3.setText('您请说：京东数科')
        self.speaker_label3.setFont(font)

        self.speaker_label3.resize(300, 30)
        self.speaker_label3.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label3.move(20, 250)

        self.speaker_label3.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label3.setPalette(pe)

        self.speaker_label4 = QLabel(self)
        self.speaker_label4.setText('您请说：周瑜打黄盖-一个愿打一个愿挨')
        self.speaker_label4.setFont(font)

        self.speaker_label4.resize(600, 30)
        self.speaker_label4.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label4.move(20, 300)

        self.speaker_label4.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label4.setPalette(pe)

        self.speaker_label5 = QLabel(self)
        self.speaker_label5.setText('您请说：中华人民共和国')
        self.speaker_label5.setFont(font)

        self.speaker_label5.resize(600, 30)
        self.speaker_label5.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label5.move(20, 350)

        self.speaker_label5.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label5.setPalette(pe)

        self.speaker_label6 = QLabel(self)
        self.speaker_label6.setText('您请说：京东购物季')
        self.speaker_label6.setFont(font)

        self.speaker_label6.resize(600, 30)
        self.speaker_label6.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label6.move(20, 400)

        self.speaker_label6.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label6.setPalette(pe)

        self.speaker_label7 = QLabel(self)
        self.speaker_label7.setText('您请说：空山新雨后，天气晚来秋')
        self.speaker_label7.setFont(font)

        self.speaker_label7.resize(600, 30)
        self.speaker_label7.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label7.move(20, 450)

        self.speaker_label7.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label7.setPalette(pe)

        self.speaker_label8 = QLabel(self)
        self.speaker_label8.setText('您请说：西塞山前白鹭飞')
        self.speaker_label8.setFont(font)

        self.speaker_label8.resize(600, 30)
        self.speaker_label8.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label8.move(20, 500)

        self.speaker_label8.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label8.setPalette(pe)

        self.speaker_label9 = QLabel(self)
        self.speaker_label9.setText('您请说：中国特色社会主义')
        self.speaker_label9.setFont(font)

        self.speaker_label9.resize(600, 30)
        self.speaker_label9.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label9.move(20, 550)

        self.speaker_label9.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label9.setPalette(pe)

        self.speaker_label10 = QLabel(self)
        self.speaker_label10.setText('您请说：1949年10月1日')
        self.speaker_label10.setFont(font)

        self.speaker_label10.resize(600, 30)
        self.speaker_label10.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label10.move(900, 100)

        self.speaker_label10.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label10.setPalette(pe)

        self.speaker_label11 = QLabel(self)
        self.speaker_label11.setText('您请说：坐地日行八万里，巡天遥望一千河')
        self.speaker_label11.setFont(font)

        self.speaker_label11.resize(600, 30)
        self.speaker_label11.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label11.move(900, 150)

        self.speaker_label11.setAutoFillBackground(True)   
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label11.setPalette(pe)

        self.speaker_label12 = QLabel(self)
        self.speaker_label12.setText('您请说：扩大改革开放')
        self.speaker_label12.setFont(font)

        self.speaker_label12.resize(600, 30)
        self.speaker_label12.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label12.move(900, 200)

        self.speaker_label12.setAutoFillBackground(True)   
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label12.setPalette(pe)

        self.speaker_label13 = QLabel(self)
        self.speaker_label13.setText('您请说：今天晚上吃什么')
        self.speaker_label13.setFont(font)

        self.speaker_label13.resize(600, 30)
        self.speaker_label13.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label13.move(900, 250)

        self.speaker_label13.setAutoFillBackground(True)   
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label13.setPalette(pe)

        self.speaker_label14 = QLabel(self)
        self.speaker_label14.setText('您请说：携来百侣曾游，忆往昔峥嵘岁月稠')
        self.speaker_label14.setFont(font)

        self.speaker_label14.resize(600, 30)
        self.speaker_label14.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label14.move(900, 300)

        self.speaker_label14.setAutoFillBackground(True)   
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label14.setPalette(pe)

        self.speaker_label15 = QLabel(self)
        self.speaker_label15.setText('您请说：南方主要种植水稻')
        self.speaker_label15.setFont(font)

        self.speaker_label15.resize(600, 30)
        self.speaker_label15.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label15.move(900, 350)

        self.speaker_label15.setAutoFillBackground(True)   
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label15.setPalette(pe)

        self.speaker_label16 = QLabel(self)
        self.speaker_label16.setText('您请说：今天的会议可能会持续一个上午')
        self.speaker_label16.setFont(font)

        self.speaker_label16.resize(600, 30)
        self.speaker_label16.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label16.move(900, 400)

        self.speaker_label16.setAutoFillBackground(True)   
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label16.setPalette(pe)

        self.speaker_label17 = QLabel(self)
        self.speaker_label17.setText('您请说：红雨随心翻作浪，青山着意化为桥')
        self.speaker_label17.setFont(font)

        self.speaker_label17.resize(600, 30)
        self.speaker_label17.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label17.move(900, 450)

        self.speaker_label17.setAutoFillBackground(True)   
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label17.setPalette(pe)

        self.speaker_label18 = QLabel(self)
        self.speaker_label18.setText('您请说：下雨天留客天天留客不留')
        self.speaker_label18.setFont(font)

        self.speaker_label18.resize(600, 30)
        self.speaker_label18.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label18.move(900, 500)

        self.speaker_label18.setAutoFillBackground(True)   
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label18.setPalette(pe)

        self.speaker_label19 = QLabel(self)
        self.speaker_label19.setText('您请说：承前启后，继往开来')
        self.speaker_label19.setFont(font)

        self.speaker_label19.resize(600, 30)
        self.speaker_label19.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label19.move(900, 550)

        self.speaker_label19.setAutoFillBackground(True)   
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label19.setPalette(pe)

        self.record_pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.record_pushButton.setGeometry(QtCore.QRect(260, 160, 61, 41))
        #font = QtGui.QFont()
        #font.setPointSize(14)
        #self.record_pushButton.setFont(font)
        self.record_pushButton.setObjectName("record_pushButton")

        self.record_pushButton.setStyleSheet("QPushButton{border-image: url(images/mic_2.png)}")
        self.record_pushButton.setToolTip('START!')

        #self.transcription_pushButton.setGeometry(QtCore.QRect(300, 90, 140, 81))
        self.record_pushButton.move(550, 200)
        self.record_pushButton.resize(120, 120)
        
        ###显示时间###
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(640, 50, 160, 81))
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setObjectName("lcdNumber")

        self.pause_pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.pause_pushButton.setGeometry(QtCore.QRect(370, 160, 61, 41))
        #font = QtGui.QFont()
        #font.setPointSize(14)
        #self.pause_pushButton.setFont(font)
        self.pause_pushButton.setObjectName("pause_pushButton")

        self.pause_pushButton.setStyleSheet("QPushButton{border-image: url(images/stop_2.png)}")
        self.pause_pushButton.setToolTip('STOP!')

        #self.transcription_pushButton.setGeometry(QtCore.QRect(300, 90, 140, 81))
        self.pause_pushButton.move(780, 200)
        self.pause_pushButton.resize(120, 120)

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
        MainWindow_transcription.setWindowTitle(_translate("MainWindow_transcription", "ENROLL"))
        #self.record_pushButton.setText(_translate("MainWindow_transcription", "录制"))
        #self.pause_pushButton.setText(_translate("MainWindow_transcription", "停止"))
        self.comboBox.setItemText(0, _translate("MainWindow_transcription", "注册音频文件列表"))