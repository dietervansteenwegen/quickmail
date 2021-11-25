# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quickmail/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuickMail(object):
    def setupUi(self, QuickMail):
        QuickMail.setObjectName("QuickMail")
        QuickMail.resize(647, 312)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QuickMail.sizePolicy().hasHeightForWidth())
        QuickMail.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QuickMail.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(QuickMail)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_mail = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_mail.setGeometry(QtCore.QRect(20, 20, 607, 110))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_mail.sizePolicy().hasHeightForWidth())
        self.txt_mail.setSizePolicy(sizePolicy)
        self.txt_mail.setObjectName("txt_mail")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 185, 91, 16))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 235, 61, 16))
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 140, 200, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_send = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_send.setObjectName("btn_send")
        self.horizontalLayout.addWidget(self.btn_send)
        self.btn_parse_cred = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_parse_cred.setObjectName("btn_parse_cred")
        self.horizontalLayout.addWidget(self.btn_parse_cred)
        self.lblLogo = QtWidgets.QLabel(self.centralwidget)
        self.lblLogo.setGeometry(QtCore.QRect(490, 160, 121, 101))
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(":/logo/logo.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setObjectName("lblLogo")
        self.lbl_server = QtWidgets.QLabel(self.centralwidget)
        self.lbl_server.setGeometry(QtCore.QRect(110, 185, 200, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_server.sizePolicy().hasHeightForWidth())
        self.lbl_server.setSizePolicy(sizePolicy)
        self.lbl_server.setObjectName("lbl_server")
        self.lbl_user = QtWidgets.QLabel(self.centralwidget)
        self.lbl_user.setGeometry(QtCore.QRect(110, 210, 200, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_user.sizePolicy().hasHeightForWidth())
        self.lbl_user.setSizePolicy(sizePolicy)
        self.lbl_user.setObjectName("lbl_user")
        self.lbl_recipient = QtWidgets.QLabel(self.centralwidget)
        self.lbl_recipient.setGeometry(QtCore.QRect(110, 235, 200, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_recipient.sizePolicy().hasHeightForWidth())
        self.lbl_recipient.setSizePolicy(sizePolicy)
        self.lbl_recipient.setObjectName("lbl_recipient")
        QuickMail.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QuickMail)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 20))
        self.menubar.setObjectName("menubar")
        QuickMail.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QuickMail)
        self.statusbar.setObjectName("statusbar")
        QuickMail.setStatusBar(self.statusbar)

        self.retranslateUi(QuickMail)
        QtCore.QMetaObject.connectSlotsByName(QuickMail)

    def retranslateUi(self, QuickMail):
        _translate = QtCore.QCoreApplication.translate
        QuickMail.setWindowTitle(_translate("QuickMail", "Quickmail"))
        self.label_1.setText(_translate("QuickMail", "Mailserver:"))
        self.label_2.setText(_translate("QuickMail", "User:"))
        self.label_3.setText(_translate("QuickMail", "Recipient:"))
        self.btn_send.setText(_translate("QuickMail", "Send email"))
        self.btn_send.setShortcut(_translate("QuickMail", "Ctrl+S, Ctrl+S"))
        self.btn_parse_cred.setText(_translate("QuickMail", "Parse credentials"))
        self.lbl_server.setText(_translate("QuickMail", "Unknown"))
        self.lbl_user.setText(_translate("QuickMail", "Unknown"))
        self.lbl_recipient.setText(_translate("QuickMail", "Unknown"))
import resources_rc
