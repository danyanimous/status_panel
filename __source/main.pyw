import sys
import io
#import os
from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_status_panel as panel #импортируем класс из файла с интерфейсом

ui = panel()

def initUI():
    ui.btn_Idle.clicked.connect(lambda: sendStatus("Свободен")) #прикручиваем к кнопкам из класса функции из этого файла
    ui.btn_Headphones.clicked.connect(lambda: sendStatus("В наушниках")) #поскольку функции принимают аргументы, здесь нужно именно lambda-выражение
    ui.btn_Busy.clicked.connect(lambda: sendStatus("Занят"))
    ui.btn_Sleeping.clicked.connect(lambda: sendStatus("Сплю"))
    ui.btn_AnotherRoom.clicked.connect(lambda: sendStatus("В другой комнате"))
    ui.btn_Outdoor.clicked.connect(lambda: sendStatus("Вне квартиры"))
    ui.btn_Kitchen.clicked.connect(lambda: sendStatus("На кухне"))
    ui.btn_Shitting.clicked.connect(lambda: sendStatus("В туалете"))
    ui.btn_Otoshel.clicked.connect(lambda: sendStatus("Нет на месте"))
    ui.btn_SengCustomMsg.clicked.connect(lambda: sendStatus(ui.txt_CustomMsg.text()))
    ui.btn_ClearField.clicked.connect(clearField)
    ui.btn_ShowKeyboard.clicked.connect(showKeyboard)
    ui.btn_ClearStatus.clicked.connect(lambda: sendStatus(""))
      
def sendStatus(btn_status):
    f = io.open("web/status.txt", mode="w", encoding="utf-8") #принудительно выставляем кодировку, иначе эта тварь будет писать в ANSI и русский язык будет ломаться
    f.write(btn_status)
    f.close()
    
def clearField():
    ui.txt_CustomMsg.setText("")
    
def showKeyboard():
    #os.system("C:\Windows\System32\osk.exe")
    ui.txt_CustomMsg.setText("Функция временно недоступна!") #как бы не пытался заставить её работать - не получается
        
def startApp():
    app = QtWidgets.QApplication(sys.argv)
    status_panel = QtWidgets.QMainWindow()
    ui.setupUi(status_panel)
    initUI()
    status_panel.show()
    app.exec_()
    #return status_panel

startApp()
