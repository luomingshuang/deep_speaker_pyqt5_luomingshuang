import wave
from os import path, system, popen
from time import strftime, localtime, time
from sys import argv, exit
from pyaudio import PyAudio, paInt16
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QInputDialog, QGridLayout, QLabel, QPushButton, QFrame
from PyQt5.Qt import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtCore import QTimer, pyqtSignal
from threading import Thread
 
from main import Ui_MainWindow_audio
from transcription import Ui_MainWindow_transcription
from test import Ui_MainWindow_test

import os, glob

import librosa

enroll_wav_path = 'media'
speakers = []

#Ui_MainWindow, QtBaseClass = 

'''
本文主要实现了一个可以录音和播放录音文件的小程序
所用到的库有：pyqt5（界面）、pyaudio（录音和播放音频）、wave（读取写入wav格式的音频文件）、threading（线程）……
'''
 
# 重构QMainWindow
# 子界面关闭时，产生关闭事件（closeEvent），正常的关闭事件就是直接关闭该界面
# 但是我们重构之后，子界面关闭，按照代码逻辑，却可以重新打开主界面
class QMainWindowNew(QMainWindow):
    def closeEvent(self, event):
        event.accept()
        main_face.show()
 
 
# audio界面
class MyAudio(QMainWindow, Ui_MainWindow_audio):
    def __init__(self):
        super(MyAudio, self).__init__()
        self.setupUi(self)
        # 创建注册数据界面对象
        self.transcription_window = Transcription()
        # 创建识别界面对象
        #self.player_window = Player()
        self.test_window = Test()
        # 绑定录音机按钮槽函数
        self.transcription_pushButton.clicked.connect(self.transcription_window.open)
        self.player_pushButton.clicked.connect(self.test_window.open)
 
 
# 录音界面
class Transcription(QMainWindowNew, Ui_MainWindow_transcription):
    def __init__(self):
        super(Transcription, self).__init__()
        self.setupUi(self)
        self.name = 'lms'
        # 声明PyAudio对象
        self.pa = None
        # 关联槽函数
        self.record_pushButton.clicked.connect(self.transcription)
        self.pause_pushButton.clicked.connect(self.pause)
        # 创建定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_time)
        # 创建定时器，检测media文件夹是否有wav文件
        self.timer_dec = QTimer()
        self.timer_dec.timeout.connect(self.discover)
        # 计时时间
        self.h = 0
        self.m = 0
        self.s = 0
        # 计时器停止标志，为真则停止，为假则继续
        self.pause_flag = True
        # 创建线程对象
        self.t_record = None
        self.t_discover = None
    
    def open(self):
        # btn = QMessageBox.question(self, '请输入您的名字(英文简写)', 'yes = 停止录制，no = 继续录制', QMessageBox.Yes | QMessageBox.No)
        # if btn == QMessageBox.Yes:
        #     self.pause_flag = True
        # elif btn == QMessageBox.No:
        #     self.pause_flag = False
        text, ok = QInputDialog().getText(self, "名字","User name (英文缩写):", QLineEdit.Normal, QDir().home().dirName())
        if ok and text is not None:
            self.lcdNumber.setDigitCount(4)
            self.lcdNumber.display('0:0')
            self.show()
            main_face.close()
            self.timer_dec.start(1000)
            self.name = text
        
    def show_time(self):
        if self.pause_flag is False:
            self.s += 1
            if self.s == 60:
                self.s = 0
                self.m = self.m + 1
            if self.m == 60:
                self.m = 0
                self.h = self.h + 1
 
            text = ''
            self.lcdNumber.setDigitCount(5)
            if self.h != 0:
                self.lcdNumber.setDigitCount(8)
 
            if self.s % 2 != 0 and self.h == 0:
                text = str(self.m) + ':' + str(self.s)
            if self.s % 2 == 0 and self.h == 0:
                text = str(self.m) + ' ' + str(self.s)
            if self.h != 0:
                text = str(self.h) + ':' + text
 
            self.lcdNumber.display(text)
 
    def discover(self):
        self.t_discover = Thread(target=self.discover_demo)
        self.t_discover.start()
 
    def discover_demo(self):
        if not path.exists('./media'):
            system('MD media')
        fd = popen('dir media\*.wav /b')
        data = fd.readlines()
        list_old = []
        # 获取下拉框有多少item
        item_num = self.comboBox.count()
        for i in range(item_num):
            list_old.append(self.comboBox.itemText(i))
        # 比較下拉框中文件和获取到的文件是否一样，一样的就不加入列表
        flag = True
        for j in data:
            j = j.split('\n')[0]
            if j != '\n' and j != '\r\n':
                for i in range(item_num):
                    if j == self.comboBox.itemText(i):
                        flag = False
                        break
                if flag is True:
                    self.comboBox.addItem(j)
                else:
                    flag = True
 
    def transcription(self):
        self.record_pushButton.setEnabled(False)
        # if btn == QMessageBox.Yes:
        #     self.pause_flag = True
        # elif btn == QMessageBox.No:
        #     self.pause_flag = False

        self.timer.start(999)
        self.t_record = Thread(target=self.record)
        self.t_record.start()
 
    def record(self):
        self.pause_flag = False
        #self.record_pushButton.setText('停止')
        # 创建PyAudio对象
        self.pa = PyAudio()
        # 打开声卡，设置 采样深度为16位、声道数为2、采样率为16、模式为输入、采样点缓存数量为2048
        stream = self.pa.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=3200)
        ## speaker name:
        # text = self.open()
        print(self.name)
        if self.name not in speakers:
            speakers.append(self.name)

        # 新建一个列表，用来存储采样到的数据
        record_buf = []
        while True:
            if self.pause_flag is True:
                break
            audio_data = stream.read(3200)  # 读出声卡缓冲区的音频数据
            record_buf.append(audio_data)  # 将读出的音频数据追加到record_buf列表
        my_path = 'media/' + self.name + '_' + strftime("%Y%m%d%H%M%S", localtime(time())) + '.wav'
        wf = wave.open(my_path, 'wb')  # 创建一个音频文件
        wf.setnchannels(1)  # 设置声道数为1
        wf.setsampwidth(2)  # 设置采样深度为
        wf.setframerate(16000)  # 设置采样率为16000
        # 将数据写入创建的音频文件
        wf.writeframes("".encode().join(record_buf))
        # 写完后将文件关闭
        wf.close()
        # 停止声卡
        stream.stop_stream()
        # 关闭声卡
        stream.close()
        # 终止pyaudio
        self.pa.terminate()
        self.pa = None
        #self.record_pushButton.setText('录制')
        self.record_pushButton.setEnabled(True)

 
    def pause(self):
        if self.pa is None:
            QMessageBox.information(self, '提示', '目前没有录音', QMessageBox.Close)
            return
        # btn = QMessageBox.question(self, '选择', 'yes = 停止录制，no = 继续录制', QMessageBox.Yes | QMessageBox.No)
        # if btn == QMessageBox.Yes:
        #     self.pause_flag = True
        # elif btn == QMessageBox.No:
        #     self.pause_flag = False
        self.pause_flag = True

import torch
import random
import numpy as np

from deep_speaker.audio import read_mfcc
from deep_speaker.batcher import sample_from_mfcc
from deep_speaker.constants import SAMPLE_RATE, NUM_FRAMES
from deep_speaker.conv_models import DeepSpeakerModel
from deep_speaker.test import batch_cosine_similarity

def get_centroid(embeddings, utterance_num):
        centroid = 0
        for utterance_id, utterance in enumerate(embeddings):
            if utterance_id <= (utterance_num-1):
                #print(utterance.shape)
                centroid = centroid + utterance 
            else: break
        centroid = centroid/utterance_num
        return centroid

model_path = 'weights/epoch_3450_iteration_1487381_EER_0.05986112356185913.pth' 

# 测试界面
class Test(QMainWindowNew, Ui_MainWindow_test):
    player_signal = pyqtSignal(str)
    def __init__(self):
        super(Test, self).__init__()
        self.setupUi(self)
        # 声明PyAudio对象
        self.pa = None
        # 关联槽函数
        self.record_pushButton.clicked.connect(self.transcription)
        self.pause_pushButton.clicked.connect(self.pause)
        # 创建定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_time)
        # 创建定时器，检测media文件夹是否有wav文件
        self.timer_dec = QTimer()
        self.timer_dec.timeout.connect(self.discover)
        # 计时时间
        self.h = 0
        self.m = 0
        self.s = 0
        # 计时器停止标志，为真则停止，为假则继续
        self.pause_flag = True
        # 创建线程对象
        self.t_record = None
        self.t_discover = None
 
    def open(self):
        self.lcdNumber.setDigitCount(4)
        self.lcdNumber.display('0:0')
        self.show()
        main_face.close()
        self.timer_dec.start(1000)
 
    def show_time(self):
        if self.pause_flag is False:
            self.s += 1
            if self.s == 60:
                self.s = 0
                self.m = self.m + 1
            if self.m == 60:
                self.m = 0
                self.h = self.h + 1
 
            text = ''
            self.lcdNumber.setDigitCount(5)
            if self.h != 0:
                self.lcdNumber.setDigitCount(8)
 
            if self.s % 2 != 0 and self.h == 0:
                text = str(self.m) + ':' + str(self.s)
            if self.s % 2 == 0 and self.h == 0:
                text = str(self.m) + ' ' + str(self.s)
            if self.h != 0:
                text = str(self.h) + ':' + text
 
            self.lcdNumber.display(text)
 
    def discover(self):
        self.t_discover = Thread(target=self.discover_demo)
        self.t_discover.start()
 
    def discover_demo(self):
        if not path.exists('./test'):
            system('MD test')
        fd = popen('dir test\*.wav /b')
        data = fd.readlines()
        list_old = []

        #获取下拉框有多少item
        item_num = self.comboBox.count()
        for i in range(item_num):
            list_old.append(self.comboBox.itemText(i))
        # 比較下拉框中文件和获取到的文件是否一样，一样的就不加入列表
        flag = True
        for j in data:
            j = j.split('\n')[0]
            if j != '\n' and j != '\r\n':
                for i in range(item_num):
                    if j == self.comboBox.itemText(i):
                        flag = False
                        break
                if flag is True:
                    self.comboBox.addItem(j)
                else:
                    flag = True
 
    def transcription(self):
        self.record_pushButton.setEnabled(False)
        self.timer.start(999)
        self.t_record = Thread(target=self.record)
        self.t_record.start()
 
    def record(self):
        ####计算enroll centeriod embedding####
        dict_spkid_embeddings = {}
        all_wavs = glob.glob(os.path.join(enroll_wav_path, '*.wav'))

        model = DeepSpeakerModel()
        #model.m.load_weights('weights/ResCNN_triplet_training_checkpoint_265.h5', by_name=True)
        model.m.load_weights('weights/ResCNN_softmax_pre_training_checkpoint_102.h5', by_name=True)
        ## speakers###
        speakers = ['lms','zq', 'wry', 'lzh']

        # enroll_centroid_embeddings_npy = np.zeros((3, 256),dtype=float)
        # enroll_dict= {}
        i = 0
        for speaker in speakers:
            #print(speaker)
            speaker_wavs = glob.glob(os.path.join(enroll_wav_path, speaker+'_*.wav'))[:6]
            #print(speaker_wavs)
            speaker_embeddings = []
            for wav in speaker_wavs:
                mfcc_feat = sample_from_mfcc(read_mfcc(wav, SAMPLE_RATE), NUM_FRAMES)
                mfcc_feat = model.m.predict(np.expand_dims(mfcc_feat, axis=0))
                speaker_embeddings.append(mfcc_feat)
            num_utterances = len(speaker_wavs)
            enroll_centroid_embeddings = get_centroid(speaker_embeddings, num_utterances)
            dict_spkid_embeddings[speaker] = enroll_centroid_embeddings
            i += 1
        #np.save('enroll_3.npy', enroll_dict)

        score_speakers = {}
        thres = 0.10

        self.pause_flag = False
        #self.record_pushButton.setText('停止')
        # 创建PyAudio对象
        self.pa = PyAudio()
        # 打开声卡，设置 采样深度为16位、声道数为2、采样率为16、模式为输入、采样点缓存数量为2048
        stream = self.pa.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=3200)
        # 新建一个列表，用来存储采样到的数据
        record_buf = []
        while True:
            if self.pause_flag is True:
                break
            audio_data = stream.read(3200)  # 读出声卡缓冲区的音频数据
            record_buf.append(audio_data)  # 将读出的音频数据追加到record_buf列表
        my_path = 'test/' + strftime("%Y%m%d%H%M%S", localtime(time())) + '.wav'
        wf = wave.open(my_path, 'wb')  # 创建一个音频文件
        wf.setnchannels(1)  # 设置声道数为2
        wf.setsampwidth(2)  # 设置采样深度为
        wf.setframerate(16000)  # 设置采样率为16000
        # 将数据写入创建的音频文件
        wf.writeframes("".encode().join(record_buf))
        # 写完后将文件关闭
        wf.close()
        # 停止声卡
        stream.stop_stream()
        # 关闭声卡
        stream.close()
        # 终止pyaudio
        self.pa.terminate()
        self.pa = None
        #self.record_pushButton.setText('录制')
        self.record_pushButton.setEnabled(True)

        test_wav = my_path
        mfcc_feat = sample_from_mfcc(read_mfcc(test_wav, SAMPLE_RATE), NUM_FRAMES)
        output_feat = model.m.predict(np.expand_dims(mfcc_feat, axis=0))
        
        score = 0
        name = 'Who?'
        for speaker_name in dict_spkid_embeddings.keys():
            score_speaker = batch_cosine_similarity(dict_spkid_embeddings[speaker_name], output_feat)
            print('speaker: ', speaker_name, 'score: ', score_speaker)
            if score_speaker > score :
                score = score_speaker
                name = speaker_name
        print('speaker: ', name)
        print('score: ', score)

        self.speaker_label.setText('Speaker: %s'%name)
        self.score_label.setText('Score: %.4f'%score)
        #self.speaking_content.setText('Content: xxxxxx')
        # speaker_score_label.show()
 
    def pause(self):
        if self.pa is None:
            QMessageBox.information(self, '提示', '目前没有录音', QMessageBox.Close)
            return
        # btn = QMessageBox.question(self, '选择', 'yes = 停止录制，no = 继续录制', QMessageBox.Yes | QMessageBox.No)
        # if btn == QMessageBox.Yes:
        #     self.pause_flag = True
        # elif btn == QMessageBox.No:
        #     self.pause_flag = False
        self.pause_flag = True

if __name__ == '__main__':
    app = QApplication(argv)
    main_face = MyAudio()
    main_face.show()
    exit(app.exec_())

###1. add vad
###2. 分离
###3. add asr
