from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess

WeChat_path = 'C:\\"Program Files (x86)\\Tencent\\WeChat\\WeChat.exe"'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(170, 90)
        MainWindow.setWindowIcon(QtGui.QIcon("Multi-WeChat.ico"))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(170, 90))
        MainWindow.setMaximumSize(QtCore.QSize(170, 90))
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(10, 10, 70, 21))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 10, 70, 21))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 170, 23))
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_1 = QtWidgets.QMenu(self.menubar)
        self.menu_1.setObjectName("menu_1")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        self.versionLabel = QtWidgets.QLabel(self.statusbar)
        self.versionLabel.setGeometry(QtCore.QRect(5, 0, 160, 20))
        self.versionLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.versionLabel.setObjectName("versionLabel")
        MainWindow.setStatusBar(self.statusbar)
        self.helpAction = QtWidgets.QAction(MainWindow)
        self.helpAction.setObjectName("helpAction")
        self.updateAction = QtWidgets.QAction(MainWindow)
        self.updateAction.setObjectName("updateAction")
        self.aboutAction = QtWidgets.QAction(MainWindow)
        self.aboutAction.setObjectName("aboutAction")
        self.fileAction = QtWidgets.QAction(MainWindow)
        self.fileAction.setObjectName("fileAction")
        self.menu_2.addAction(self.helpAction)
        self.menu_2.addAction(self.updateAction)
        self.menu_2.addAction(self.aboutAction)
        self.menu_1.addAction(self.fileAction)
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu_2.setEnabled(False)
        self.fileAction.triggered.connect(self.locate_path)
        self.pushButton.clicked.connect(self.run_cmd)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "微信多开"))
        self.pushButton.setText(_translate("MainWindow", "一键多开"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.menu_1.setTitle(_translate("MainWindow", "文件"))
        self.versionLabel.setText(_translate("MainWindow", "Version 1.0"))
        self.helpAction.setText(_translate("MainWindow", "使用说明"))
        self.updateAction.setText(_translate("MainWindow", "检查更新"))
        self.aboutAction.setText(_translate("MainWindow", "关于"))
        self.fileAction.setText(_translate("MainWindow", "选择微信位置..."))

    def locate_path(self):
        global WeChat_path
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "请选择 WeChat.exe ...", "", "WeChat.exe (*.exe)"
        )
        if filename:
            if os.path.basename(filename) != "WeChat.exe":
                QtWidgets.QMessageBox.warning(None, "错误", "请选择 WeChat.exe 文件!")
            else:
                filename = filename.strip('"')
                drive = filename[:2]
                rest = filename[2:]
                new_path = drive + "\"" + rest + "\""
                WeChat_path = new_path
                QtWidgets.QMessageBox.information(
                    None, "成功", f"微信路径已更新为: \n{WeChat_path}!"
                )

    def run_cmd(self):
        global WeChat_path
        try:
            run_time = int(self.spinBox.value())
            run_command = f'start {WeChat_path}'
            for i in range(1, run_time):
                run_command += f' && start {WeChat_path}'
            result = subprocess.run(
                run_command, shell=True, capture_output=True, text=True
            )
            if result.returncode != 0:
                QtWidgets.QMessageBox.warning(
                    None, "错误", f"执行命令时出错: \n{result.stderr}\n请重新设置文件目录!"
                )
            else:
                QtWidgets.QMessageBox.information(None, "成功", "微信已多开!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                None, "错误", f"[Error] 发生了一个错误: {str(e)}!"
            )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
