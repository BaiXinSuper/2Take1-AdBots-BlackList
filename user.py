import requests
import getpass
import os
import re
import wmi
import hashlib
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
username = os.getenv('APPDATA')
__DEBUG = False
if not __DEBUG:
    url = "http://Server Ip:6471"
else:
    url = "http://127.0.0.1:6471"


class Upload(QtCore.QThread):
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Upload, self).__init__()

    def difference(self, t1, t2):  # V10 本地校验
        return [x for x in t1 if x not in t2]

    def upload(self, AG):
        c = requests.post(f'{url}/sentScids',
                          data=AG.encode("utf-8"), headers=header)
        msg = c.text
        c.close()
        return msg

    def run(self):
        self._signal.emit("上传中，稍安勿躁")
        with open(f'{username}\\PopstarDevs\\2Take1Menu\\cfg\\scid.cfg', 'r', encoding='utf-8') as f:
            all_info = f.read().strip()
            f.close()
            uploadinfo = ''
            x = all_info.split('\n')
            try:
                x.remove('[SCID]')
            except:
                pass
            if os.path.exists(f'{username}\\PopstarDevs\\2Take1Menu\\cfg\\old_scid.cfg'):
                with open(f'{username}\\PopstarDevs\\2Take1Menu\\cfg\\old_scid.cfg', "r", encoding="utf-8") as f:
                    old_scids = f.read().strip().split("\n")
                    f.close()
                try:
                    old_scids.remove('[SCID]')
                except:
                    pass
                x = self.difference(x, old_scids)

            print(x)
            if x != []:
                for i in range(len(x)):
                    x[i] = x[i].split(':')
                    if len(x[i]) == 3 and x[i][2] == 'c':
                        uploadinfo = uploadinfo+x[i][1]+'\n'
                with open(f'{username}\\PopstarDevs\\2Take1Menu\\cfg\\old_scid.cfg', 'w', encoding='utf-8') as f:
                    f.write(all_info)
                    f.close()
            if uploadinfo != '':
                c = self.upload(uploadinfo[:-1])
                self._signal.emit(str(c))
            else:
                self._signal.emit("上传失败:无新数据")


class Download(QtCore.QThread):
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Download, self).__init__()

    def run(self):
        sc = all = fl = 0
        with open(f'{username}\\PopstarDevs\\2Take1Menu\\cfg\\scid.cfg', 'r', encoding='utf-8') as f:
            all_local_info = f.read()
            f.close()
            c = requests.get(f'{url}/getADBotScid', headers=header)
            cloud_msg = c.text.split('\n')
            c.close()
            with open(f'{username}\\PopstarDevs\\2Take1Menu\\cfg\\scid.cfg', 'a', encoding='utf-8') as f:
                for i in cloud_msg:
                    if i not in all_local_info:
                        f.write('ad_bot:'+i+':c\n')
                        sc += 1
                    else:
                        fl += 1
                    all += 1
            self._signal.emit(
                f'成功下载广告机{sc}个 本地重复广告机{fl-1}个 服务器云端广告机个数:{all-1}')


class Clean_err(QtCore.QThread):
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Clean_err, self).__init__()

    def run(self):
        er = 0
        with open(f'{username}\\PopstarDevs\\2Take1Menu\\cfg\\scid.cfg', 'r', encoding='utf-8') as f:
            all_info = f.read()
            f.close()
            if all_info != '':
                x = all_info.split('\n')
                self._signal.emit("查找异常中")
                try:
                    x.remove('[SCID]')
                except:
                    pass
                if x != []:
                    for i in range(len(x)):
                        x[i] = x[i].split(':')
                        if len(x[i]) == 3 and x[i][2] == 'c':
                            if 9 >= len(x[i][1]) >= 5:
                                if re.match('.*[A-Z].*', x[i][1]):
                                    er += 1
                                    all_info = all_info.replace(
                                        x[i][0]+':'+x[i][1]+':'+'c\n', '')
                            else:
                                er += 1
                                all_info = all_info.replace(
                                    x[i][0]+':'+x[i][1]+':'+'c\n', '')
                with open(f'{username}\\PopstarDevs\\2Take1Menu\\cfg\\scid.cfg', 'w', encoding='utf-8') as f:
                    f.write(all_info)
                    f.close()
                self._signal.emit(f'本次共计清理{er}个异常广告机')


class Clean_dou(QtCore.QThread):
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Clean_dou, self).__init__()

    def run(self):
        self._signal.emit("重复检测中")
        cf = 0
        cflist = []
        with open(f'{username}\\PopstarDevs\\2Take1Menu\\cfg\\scid.cfg', 'r', encoding='utf-8') as f:
            all_info = f.read()
            f.close()
            if all_info != '':
                x = all_info.split('\n')
                self._signal.emit(f"查找重复id中")
                try:
                    x.remove('[SCID]')
                except:
                    pass
                if x != []:
                    for i in range(len(x)):
                        x[i] = x[i].split(':')
                        if len(x[i]) == 3 and x[i][2] == 'c':
                            if 8 >= len(x[i][1]) >= 5:
                                if x[i][1] not in cflist:
                                    cflist.append(x[i][1])
                                else:
                                    cf += 1
                                    all_info = all_info.replace(
                                        x[i][0]+':'+x[i][1]+':'+'c\n', '', 1)
                                    self._signal.emit(f"已检查到{cf}个重复id")
        if cf:
            with open(f'{username}\\PopstarDevs\\2Take1Menu\\cfg\\scid.cfg', 'w', encoding='utf-8') as f:
                f.write(all_info)
                f.close()
        self._signal.emit(f"本次共计清理重复广告机{cf}个")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(737, 200)
        if os.path.exists('temp.ico'):
            icon = QtGui.QIcon("./temp.ico")
            MainWindow.setWindowIcon(icon)
            os.remove('./temp.ico')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 0, 500, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignTop | Qt.AlignRight)
        # self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 30, 461, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 721, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 120, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 120, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 120, 101, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(632, 120, 101, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 150, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(530, 150, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setFixedSize(737, 200)
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.start_upload)
        self.pushButton_2.clicked.connect(self.download_files)
        self.pushButton_3.clicked.connect(self.clean_err)
        self.pushButton_4.clicked.connect(self.clean_dou)
        self.pushButton_5.clicked.connect(lambda: self.copy("872986398"))
        self.pushButton_6.clicked.connect(lambda: self.copy(uuid))
        self.t1 = None
        self.t2 = None
        self.t3 = None
        self.t4 = None
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2Take1广告机云黑 V1"))
        self.label_2.setText(_translate(
            "MainWindow", "欢迎加入2T交流群872986398 https://github.com/BaiXinSuper/2Take1-AdBots-BlackList"))
        self.label_3.setText(_translate("MainWindow", "你的UUID:"))
        self.pushButton.setText(_translate("MainWindow", "上传数据"))
        self.pushButton_2.setText(_translate("MainWindow", "下载数据"))
        self.pushButton_3.setText(_translate("MainWindow", "清理异常数据"))
        self.pushButton_4.setText(_translate("MainWindow", "清除重复数据"))
        self.label.setToolTip(_translate("MainWindow", "你不需要做除按按钮以外的任何操作"))
        self.pushButton.setToolTip(_translate("MainWindow", "从本地读取数据，发送给服务器"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "从云端服务器下载数据到本地"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "删除本地的不合法数据"))
        self.pushButton_4.setToolTip(_translate("MainWindow", "删除本地重复的广告机数据"))
        self.pushButton_5.setText(_translate("MainWindow", "复制群号"))
        self.pushButton_5.setToolTip(_translate("MainWindow", "复制群号"))
        self.pushButton_6.setText(_translate("MainWindow", "复制UUID"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "复制你的设备唯一识别码"))

    def check(self):
        if self.t1 or self.t2 or self.t3 or self.t4:
            return False
        return True

    def start_upload(self):
        if self.check():
            self.t1 = Upload()
            self.t1._signal.connect(self.changeTxt)
            self.t1.start()

    def changeTxt(self, msg):
        self.t1 = None
        self.t2 = None
        self.t3 = None
        self.t4 = None
        self.label.setText(
            QtCore.QCoreApplication.translate("MainWindow", msg))

    def download_files(self):
        if self.check():
            self.t2 = Download()
            self.t2._signal.connect(self.changeTxt)
            self.t2.start()

    def clean_err(self):
        if self.check():
            self.t3 = Clean_err()
            self.t3._signal.connect(self.changeTxt)
            self.t3.start()

    def clean_dou(self):
        if self.check():
            self.t4 = Clean_dou()
            self.t4._signal.connect(self.changeTxt)
            self.t4.start()

    def copy(self, msg):
        pyperclip.copy(msg)


app = QtWidgets.QApplication(sys.argv)         # 创建一个QApplication，即将开发的软件app
MainWindow = QtWidgets.QMainWindow()  # QMainWindow装载需要的组件
ui = Ui_MainWindow()
ui.setupUi(MainWindow)  # 执行类中的setupUi方法
MainWindow.show()


def enj(idhash):
    for i in range(50):
        idhash = hashlib.sha256(idhash.encode("utf-8")).hexdigest()
        idhash = hashlib.md5(idhash.encode("utf-8")).hexdigest()
        idhash = hashlib.sha1(idhash.encode("utf-8")).hexdigest()
    return idhash


def spawn_uuid(h1, h2):
    h = h1+h2
    for i in range(10):
        h = hashlib.sha384(h.encode('utf-8')).hexdigest()
    return hashlib.sha256(h.encode('utf-8')).hexdigest().upper()


ui.label_3.setText(QtCore.QCoreApplication.translate("MainWindow", "正在初始化"))
if not username:
    username = getpass.getuser()
ui.label_3.setText(QtCore.QCoreApplication.translate(
    "MainWindow", "正在获取CPUid"))
for cpu in wmi.WMI().Win32_Processor():
    cpuid = cpu.ProcessorId.strip()
ui.label_3.setText(QtCore.QCoreApplication.translate(
    "MainWindow", f"获取完成CPUid:{cpuid}"))
ui.label_3.setText(QtCore.QCoreApplication.translate(
    "MainWindow", f"开始加密CPUid"))
cpuid = enj(cpuid)
ui.label_3.setText(QtCore.QCoreApplication.translate(
    "MainWindow", f"加密完成CPUid:{cpuid}"))
ui.label_3.setText(QtCore.QCoreApplication.translate(
    "MainWindow", f"开始获取主板id"))
for b in wmi.WMI().Win32_BaseBoard():
    boardid = b.SerialNumber
ui.label_3.setText(QtCore.QCoreApplication.translate(
    "MainWindow", f"获取完成主板id:{boardid}"))
ui.label_3.setText(QtCore.QCoreApplication.translate(
    "MainWindow", f"开始加密主板id"))
boardid = enj(boardid)
ui.label_3.setText(QtCore.QCoreApplication.translate(
    "MainWindow", f"加密完成主板id:{boardid}"))
ui.label_3.setText(QtCore.QCoreApplication.translate(
    "MainWindow", f"开始生成uuid"))
uuid = spawn_uuid(cpuid, boardid)

header = {
    "UUID": uuid,
    "Ver": "No_offical_Admin_V1"
}  # 切勿修改此项


ui.label_3.setText(QtCore.QCoreApplication.translate(
    "MainWindow", f"如有问题请带上你的UUID:{uuid}"))
# print(f"如有问题请带上你的唯一识别码:{uuid}")
sys.exit(app.exec_())
