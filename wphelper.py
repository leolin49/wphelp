# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wphelper.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 271)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 70, 251, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.comboBox_resolution = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_resolution.setObjectName("comboBox_resolution")
        self.gridLayout.addWidget(self.comboBox_resolution, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_catalog = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_catalog.setObjectName("comboBox_catalog")
        self.gridLayout.addWidget(self.comboBox_catalog, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_number = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.gridLayout.addWidget(self.lineEdit_number, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_source = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_source.setObjectName("comboBox_source")
        self.gridLayout.addWidget(self.comboBox_source, 0, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 200, 255, 43))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DownLoad = QtWidgets.QCommandLinkButton(self.layoutWidget1)
        self.DownLoad.setObjectName("DownLoad")
        self.horizontalLayout.addWidget(self.DownLoad)
        self.About = QtWidgets.QPushButton(self.layoutWidget1)
        self.About.setObjectName("About")
        self.horizontalLayout.addWidget(self.About)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 50, 401, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 20, 311, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "wphelper-v1.0"))
        self.label_1.setText(_translate("Dialog", "来源"))
        self.label_2.setText(_translate("Dialog", "分辨率"))
        self.label_4.setText(_translate("Dialog", "数量"))
        self.label_3.setText(_translate("Dialog", "分类"))
        self.DownLoad.setText(_translate("Dialog", "DownLoad"))
        self.About.setText(_translate("Dialog", "About"))
