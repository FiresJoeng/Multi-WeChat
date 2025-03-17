@echo off
title https://github.com/FiresJoeng/Multi-WeChat
echo 安装依赖库...
pip install -r requirements.txt
echo 转换UI文件...
pyuic5 -x MainWindow.ui -o MainWindow.py
echo 使用PyInstaller编译...
pyinstaller --onefile --name Multi-WeChat --noconsole --icon=Multi-WeChat.ico main.py
echo End!
pause
