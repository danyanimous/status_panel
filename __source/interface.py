# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# НЕ ТРОГАЙ ЭТОТ ФАЙЛ. ОН СГЕНЕРИРОВАН АВТОМАТИЧЕСКИ И ВМЕШАТЕЛЬСТВА НЕ ТРЕБУЕТ. ВСЕ ИЗМЕНЕНИЯ ВНОСЯТСЯ В main.pyw


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_status_panel(object):
    def setupUi(self, status_panel):
        status_panel.setObjectName("status_panel")
        status_panel.resize(635, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(status_panel.sizePolicy().hasHeightForWidth())
        status_panel.setSizePolicy(sizePolicy)
        status_panel.setMinimumSize(QtCore.QSize(635, 800))
        status_panel.setMaximumSize(QtCore.QSize(635, 800))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 167, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 142, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 109, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 116, 116))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(182, 182, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 167, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 142, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 109, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 116, 116))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(182, 182, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 167, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 116, 116))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 116, 116))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(182, 182, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        status_panel.setPalette(palette)
        status_panel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        status_panel.setWindowTitle("status_panel")
        status_panel.setStatusTip("")
        status_panel.setWhatsThis("")
        status_panel.setAccessibleName("")
        status_panel.setAccessibleDescription("")
        status_panel.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.group_NaMeste = QtWidgets.QGroupBox(status_panel)
        self.group_NaMeste.setGeometry(QtCore.QRect(20, 20, 601, 221))
        self.group_NaMeste.setObjectName("group_NaMeste")
        self.btn_Idle = QtWidgets.QPushButton(self.group_NaMeste)
        self.btn_Idle.setGeometry(QtCore.QRect(20, 20, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Idle.setFont(font)
        self.btn_Idle.setObjectName("btn_Idle")
        self.btn_Headphones = QtWidgets.QPushButton(self.group_NaMeste)
        self.btn_Headphones.setGeometry(QtCore.QRect(320, 20, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Headphones.setFont(font)
        self.btn_Headphones.setObjectName("btn_Headphones")
        self.btn_Busy = QtWidgets.QPushButton(self.group_NaMeste)
        self.btn_Busy.setGeometry(QtCore.QRect(20, 120, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Busy.setFont(font)
        self.btn_Busy.setObjectName("btn_Busy")
        self.btn_Sleeping = QtWidgets.QPushButton(self.group_NaMeste)
        self.btn_Sleeping.setGeometry(QtCore.QRect(320, 120, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Sleeping.setFont(font)
        self.btn_Sleeping.setObjectName("btn_Sleeping")
        self.group_NetNaMeste = QtWidgets.QGroupBox(status_panel)
        self.group_NetNaMeste.setGeometry(QtCore.QRect(20, 260, 601, 321))
        self.group_NetNaMeste.setObjectName("group_NetNaMeste")
        self.btn_AnotherRoom = QtWidgets.QPushButton(self.group_NetNaMeste)
        self.btn_AnotherRoom.setGeometry(QtCore.QRect(20, 20, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_AnotherRoom.setFont(font)
        self.btn_AnotherRoom.setObjectName("btn_AnotherRoom")
        self.btn_Outdoor = QtWidgets.QPushButton(self.group_NetNaMeste)
        self.btn_Outdoor.setGeometry(QtCore.QRect(20, 120, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Outdoor.setFont(font)
        self.btn_Outdoor.setObjectName("btn_Outdoor")
        self.btn_Kitchen = QtWidgets.QPushButton(self.group_NetNaMeste)
        self.btn_Kitchen.setGeometry(QtCore.QRect(320, 120, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Kitchen.setFont(font)
        self.btn_Kitchen.setObjectName("btn_Kitchen")
        self.btn_Shitting = QtWidgets.QPushButton(self.group_NetNaMeste)
        self.btn_Shitting.setGeometry(QtCore.QRect(320, 20, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Shitting.setFont(font)
        self.btn_Shitting.setObjectName("btn_Shitting")
        self.btn_Otoshel = QtWidgets.QPushButton(self.group_NetNaMeste)
        self.btn_Otoshel.setGeometry(QtCore.QRect(20, 220, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Otoshel.setFont(font)
        self.btn_Otoshel.setObjectName("btn_Otoshel")
        self.group_CustomMsg = QtWidgets.QGroupBox(status_panel)
        self.group_CustomMsg.setGeometry(QtCore.QRect(20, 600, 601, 181))
        self.group_CustomMsg.setObjectName("group_CustomMsg")
        self.txt_CustomMsg = QtWidgets.QLineEdit(self.group_CustomMsg)
        self.txt_CustomMsg.setGeometry(QtCore.QRect(20, 40, 441, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.txt_CustomMsg.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.txt_CustomMsg.setFont(font)
        self.txt_CustomMsg.setText("")
        self.txt_CustomMsg.setMaxLength(128)
        self.txt_CustomMsg.setPlaceholderText("")
        self.txt_CustomMsg.setClearButtonEnabled(False)
        self.txt_CustomMsg.setObjectName("txt_CustomMsg")
        self.btn_SengCustomMsg = QtWidgets.QPushButton(self.group_CustomMsg)
        self.btn_SengCustomMsg.setGeometry(QtCore.QRect(480, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_SengCustomMsg.setFont(font)
        self.btn_SengCustomMsg.setObjectName("btn_SengCustomMsg")
        self.btn_ClearField = QtWidgets.QPushButton(self.group_CustomMsg)
        self.btn_ClearField.setGeometry(QtCore.QRect(20, 100, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ClearField.sizePolicy().hasHeightForWidth())
        self.btn_ClearField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ClearField.setFont(font)
        self.btn_ClearField.setObjectName("btn_ClearField")
        self.btn_ClearStatus = QtWidgets.QPushButton(self.group_CustomMsg)
        self.btn_ClearStatus.setGeometry(QtCore.QRect(420, 100, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ClearStatus.sizePolicy().hasHeightForWidth())
        self.btn_ClearStatus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ClearStatus.setFont(font)
        self.btn_ClearStatus.setObjectName("btn_ClearStatus")
        self.btn_ShowKeyboard = QtWidgets.QPushButton(self.group_CustomMsg)
        self.btn_ShowKeyboard.setGeometry(QtCore.QRect(220, 100, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ShowKeyboard.sizePolicy().hasHeightForWidth())
        self.btn_ShowKeyboard.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ShowKeyboard.setFont(font)
        self.btn_ShowKeyboard.setObjectName("btn_ShowKeyboard")

        self.retranslateUi(status_panel)
        QtCore.QMetaObject.connectSlotsByName(status_panel)

    def retranslateUi(self, status_panel):
        _translate = QtCore.QCoreApplication.translate
        self.group_NaMeste.setTitle(_translate("status_panel", "Категория \"НА МЕСТЕ\""))
        self.btn_Idle.setText(_translate("status_panel", "Свободен"))
        self.btn_Headphones.setText(_translate("status_panel", "В наушниках\n"
"(переговоры)"))
        self.btn_Busy.setText(_translate("status_panel", "Занят (не указано)"))
        self.btn_Sleeping.setText(_translate("status_panel", "Сплю"))
        self.group_NetNaMeste.setTitle(_translate("status_panel", "Категория \"НЕТ НА МЕСТЕ\""))
        self.btn_AnotherRoom.setText(_translate("status_panel", "В другой комнате"))
        self.btn_Outdoor.setText(_translate("status_panel", "Вне квартиры"))
        self.btn_Kitchen.setText(_translate("status_panel", "На кухне"))
        self.btn_Shitting.setText(_translate("status_panel", "В туалете"))
        self.btn_Otoshel.setText(_translate("status_panel", "Отошёл (не указано)"))
        self.group_CustomMsg.setTitle(_translate("status_panel", "Задать свой статус"))
        self.btn_SengCustomMsg.setText(_translate("status_panel", "Отправить"))
        self.btn_ClearField.setText(_translate("status_panel", "Очистить поле"))
        self.btn_ClearStatus.setText(_translate("status_panel", "Очистить статус \n"
"(на экране)"))
        self.btn_ShowKeyboard.setText(_translate("status_panel", "Показать экр.\n"
"клавиатуру"))
