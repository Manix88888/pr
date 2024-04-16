# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_files\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 250)
        Dialog.setMinimumSize(QtCore.QSize(300, 250))
        Dialog.setMaximumSize(QtCore.QSize(300, 250))
        Dialog.setStyleSheet("background-color: white;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.obj = QtWidgets.QLabel(Dialog)
        self.obj.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.obj.setFont(font)
        self.obj.setStyleSheet("color: #3AB0FF;")
        self.obj.setAlignment(QtCore.Qt.AlignCenter)
        self.obj.setObjectName("obj")
        self.verticalLayout.addWidget(self.obj)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(-1, 0, 9, 0)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.speed = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.speed.setFont(font)
        self.speed.setStyleSheet("color: #0014FF;")
        self.speed.setAlignment(QtCore.Qt.AlignCenter)
        self.speed.setObjectName("speed")
        self.horizontalLayout.addWidget(self.speed)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.time = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.time.setFont(font)
        self.time.setStyleSheet("color: #0014FF;")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.horizontalLayout_2.addWidget(self.time)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.start = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("color: #0014FF;")
        self.start.setAlignment(QtCore.Qt.AlignCenter)
        self.start.setObjectName("start")
        self.horizontalLayout_3.addWidget(self.start)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.end = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.end.setFont(font)
        self.end.setStyleSheet("color: #0014FF;")
        self.end.setAlignment(QtCore.Qt.AlignCenter)
        self.end.setObjectName("end")
        self.horizontalLayout_4.addWidget(self.end)
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.obj.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "Скорость:"))
        self.speed.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "м/с"))
        self.label_5.setText(_translate("Dialog", "Время:"))
        self.time.setText(_translate("Dialog", "TextLabel"))
        self.label_7.setText(_translate("Dialog", "с"))
        self.label_8.setText(_translate("Dialog", "Начальная\n"
"позиция:"))
        self.start.setText(_translate("Dialog", "TextLabel"))
        self.label_10.setText(_translate("Dialog", "м"))
        self.label_11.setText(_translate("Dialog", "Конечная\n"
"позиция:"))
        self.end.setText(_translate("Dialog", "TextLabel"))
        self.label_13.setText(_translate("Dialog", "м"))
