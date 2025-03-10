# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(279, 187)
        Main.setMinimumSize(QtCore.QSize(279, 187))
        Main.setMaximumSize(QtCore.QSize(279, 187))
        Main.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        Main.setAutoFillBackground(False)
        Main.setStyleSheet("")
        Main.setIconSize(QtCore.QSize(24, 24))
        self.mainwidget = QtWidgets.QWidget(Main)
        self.mainwidget.setStyleSheet("")
        self.mainwidget.setObjectName("mainwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.mainwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.buttons = QtWidgets.QHBoxLayout()
        self.buttons.setContentsMargins(-1, -1, 0, -1)
        self.buttons.setSpacing(20)
        self.buttons.setObjectName("buttons")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.buttons.addItem(spacerItem)
        self.btn_general = QtWidgets.QPushButton(self.mainwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_general.setFont(font)
        self.btn_general.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_general.setMouseTracking(True)
        self.btn_general.setTabletTracking(False)
        self.btn_general.setAutoFillBackground(False)
        self.btn_general.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    color:black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   color:blue; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(23, 154, 255); \n"
"}\n"
"\n"
"")
        self.btn_general.setIconSize(QtCore.QSize(19, 19))
        self.btn_general.setCheckable(False)
        self.btn_general.setObjectName("btn_general")
        self.buttons.addWidget(self.btn_general)
        self.btn_username = QtWidgets.QPushButton(self.mainwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_username.setFont(font)
        self.btn_username.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_username.setMouseTracking(True)
        self.btn_username.setTabletTracking(False)
        self.btn_username.setAutoFillBackground(False)
        self.btn_username.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    color:black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   color:blue; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(23, 154, 255); \n"
"}\n"
"\n"
"")
        self.btn_username.setIconSize(QtCore.QSize(19, 19))
        self.btn_username.setCheckable(False)
        self.btn_username.setObjectName("btn_username")
        self.buttons.addWidget(self.btn_username)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.buttons)
        self.line = QtWidgets.QFrame(self.mainwidget)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.general = QtWidgets.QWidget()
        self.general.setObjectName("general")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.general)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget = QtWidgets.QWidget(self.general)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.input_ip_address = QtWidgets.QLineEdit(self.widget)
        self.input_ip_address.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.input_ip_address.setFont(font)
        self.input_ip_address.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.input_ip_address.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.input_ip_address.setInputMask("")
        self.input_ip_address.setText("")
        self.input_ip_address.setMaxLength(50)
        self.input_ip_address.setDragEnabled(True)
        self.input_ip_address.setClearButtonEnabled(True)
        self.input_ip_address.setObjectName("input_ip_address")
        self.horizontalLayout_4.addWidget(self.input_ip_address)
        self.input_port = QtWidgets.QLineEdit(self.widget)
        self.input_port.setMaximumSize(QtCore.QSize(80, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.input_port.setFont(font)
        self.input_port.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.input_port.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.input_port.setInputMask("")
        self.input_port.setText("")
        self.input_port.setMaxLength(50)
        self.input_port.setDragEnabled(True)
        self.input_port.setClearButtonEnabled(True)
        self.input_port.setObjectName("input_port")
        self.horizontalLayout_4.addWidget(self.input_port)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.input_password = QtWidgets.QLineEdit(self.widget)
        self.input_password.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.input_password.setFont(font)
        self.input_password.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.input_password.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.input_password.setInputMask("")
        self.input_password.setMaxLength(50)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.input_password.setDragEnabled(True)
        self.input_password.setClearButtonEnabled(True)
        self.input_password.setObjectName("input_password")
        self.verticalLayout.addWidget(self.input_password)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_7.addWidget(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btn_connect = QtWidgets.QPushButton(self.general)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_connect.setFont(font)
        self.btn_connect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_connect.setMouseTracking(True)
        self.btn_connect.setTabletTracking(False)
        self.btn_connect.setAutoFillBackground(False)
        self.btn_connect.setStyleSheet("color:\'#0005ff\'\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/connect.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_connect.setIcon(icon1)
        self.btn_connect.setIconSize(QtCore.QSize(19, 19))
        self.btn_connect.setCheckable(False)
        self.btn_connect.setObjectName("btn_connect")
        self.horizontalLayout.addWidget(self.btn_connect)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.general)
        self.username = QtWidgets.QWidget()
        self.username.setObjectName("username")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.username)
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_2 = QtWidgets.QWidget(self.username)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_username = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.input_username.setFont(font)
        self.input_username.setInputMask("")
        self.input_username.setText("")
        self.input_username.setMaxLength(32767)
        self.input_username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_username.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_username.setClearButtonEnabled(True)
        self.input_username.setObjectName("input_username")
        self.verticalLayout_2.addWidget(self.input_username)
        self.checkbox_save_me = QtWidgets.QCheckBox(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.checkbox_save_me.setFont(font)
        self.checkbox_save_me.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkbox_save_me.setObjectName("checkbox_save_me")
        self.verticalLayout_2.addWidget(self.checkbox_save_me)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.verticalLayout_6.addWidget(self.widget_2)
        self.stackedWidget.addWidget(self.username)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        Main.setCentralWidget(self.mainwidget)

        self.retranslateUi(Main)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        self.btn_general.setText(_translate("Main", "General"))
        self.btn_username.setText(_translate("Main", "Username"))
        self.input_ip_address.setToolTip(_translate("Main", "enter IP address"))
        self.input_ip_address.setPlaceholderText(_translate("Main", "IP address..."))
        self.input_port.setToolTip(_translate("Main", "enter port number"))
        self.input_port.setPlaceholderText(_translate("Main", "port..."))
        self.input_password.setToolTip(_translate("Main", "enter password"))
        self.input_password.setPlaceholderText(_translate("Main", "password..."))
        self.btn_connect.setText(_translate("Main", "Connect"))
        self.btn_connect.setShortcut(_translate("Main", "Return"))
        self.input_username.setToolTip(_translate("Main", "enter username"))
        self.input_username.setPlaceholderText(_translate("Main", "username..."))
        self.checkbox_save_me.setText(_translate("Main", "Remember me"))
import resources_rc
