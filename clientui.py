# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Messenger(object):
    def setupUi(self, Messenger):
        Messenger.setObjectName("Messenger")
        Messenger.resize(369, 481)
        self.centralwidget = QtWidgets.QWidget(Messenger)
        self.centralwidget.setObjectName("centralwidget")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(300, 410, 51, 32))
        self.sendButton.setObjectName("sendButton")
        self.textInput = QtWidgets.QTextEdit(self.centralwidget)
        self.textInput.setGeometry(QtCore.QRect(20, 410, 271, 31))
        self.textInput.setObjectName("textInput")
        self.messagesBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.messagesBrowser.setGeometry(QtCore.QRect(20, 100, 331, 291))
        self.messagesBrowser.setObjectName("messagesBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 17, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput.setGeometry(QtCore.QRect(238, 60, 113, 21))
        self.nameInput.setObjectName("nameInput")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(203, 63, 31, 16))
        self.label_2.setObjectName("label_2")
        Messenger.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Messenger)
        self.statusbar.setObjectName("statusbar")
        Messenger.setStatusBar(self.statusbar)

        self.retranslateUi(Messenger)
        QtCore.QMetaObject.connectSlotsByName(Messenger)

    def retranslateUi(self, Messenger):
        _translate = QtCore.QCoreApplication.translate
        Messenger.setWindowTitle(_translate("Messenger", "Messenger"))
        self.sendButton.setText(_translate("Messenger", ">"))
        self.textInput.setPlaceholderText(_translate("Messenger", "Введите текст..."))
        self.label.setText(_translate("Messenger", "Skillbox Messenger"))
        self.nameInput.setPlaceholderText(_translate("Messenger", "Введите имя..."))
        self.label_2.setText(_translate("Messenger", "Имя:"))

