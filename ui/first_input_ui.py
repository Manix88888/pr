# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_files\first_input.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 420)
        Dialog.setStyleSheet("background-color: white;\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_first = QtWidgets.QTabWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_first.setFont(font)
        self.tabWidget_first.setStyleSheet("QTabBar::tab {\n"
"  background-color:#F9F2ED;\n"
"  color: black;\n"
"  padding: 7px 25px;\n"
"margin-top: 5px;\n"
"border-radius: 10px;\n"
"margin-right: 10px;\n"
"margin-left: 70px;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background-color: #3AB0FF;\n"
"color: white;\n"
" }\n"
"QTabWidget::pane { \n"
"   border: none;\n"
"}")
        self.tabWidget_first.setObjectName("tabWidget_first")
        self.tab_rpd = QtWidgets.QWidget()
        self.tab_rpd.setObjectName("tab_rpd")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_rpd)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.tab_rpd)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_speed = QtWidgets.QCheckBox(self.frame)
        self.cb_speed.setMaximumSize(QtCore.QSize(16, 16777215))
        self.cb_speed.setStyleSheet("")
        self.cb_speed.setText("")
        self.cb_speed.setIconSize(QtCore.QSize(10, 10))
        self.cb_speed.setObjectName("cb_speed")
        self.horizontalLayout.addWidget(self.cb_speed)
        self.label_23 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout.addWidget(self.label_23)
        self.label_speed = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_speed.setFont(font)
        self.label_speed.setStyleSheet("QLineEdit {\n"
"  border-radius: 10px;\n"
"  border: 2px solid #F9F2ED;\n"
"  padding: 2px 10px;\n"
"margin-left: 15px;\n"
"margin-right: 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #3AB0FF;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #F9F2ED;\n"
"}")
        self.label_speed.setText("")
        self.label_speed.setReadOnly(True)
        self.label_speed.setObjectName("label_speed")
        self.horizontalLayout.addWidget(self.label_speed)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.tab_rpd)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cb_time = QtWidgets.QCheckBox(self.frame_2)
        self.cb_time.setMaximumSize(QtCore.QSize(16, 16777215))
        self.cb_time.setText("")
        self.cb_time.setIconSize(QtCore.QSize(24, 24))
        self.cb_time.setObjectName("cb_time")
        self.horizontalLayout_2.addWidget(self.cb_time)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_time = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("QLineEdit {\n"
"  border-radius: 10px;\n"
"  border: 2px solid #F9F2ED;\n"
"  padding: 2px 10px;\n"
"margin-left: 45px;\n"
"margin-right: 25px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #3AB0FF;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #F9F2ED;\n"
"}")
        self.label_time.setReadOnly(True)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout_2.addWidget(self.label_time)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.tab_rpd)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cb_start = QtWidgets.QCheckBox(self.frame_3)
        self.cb_start.setMaximumSize(QtCore.QSize(16, 16777215))
        self.cb_start.setText("")
        self.cb_start.setIconSize(QtCore.QSize(16, 16))
        self.cb_start.setObjectName("cb_start")
        self.horizontalLayout_3.addWidget(self.cb_start)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_start = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_start.setFont(font)
        self.label_start.setStyleSheet("QLineEdit {\n"
"  border-radius: 10px;\n"
"  border: 2px solid #F9F2ED;\n"
"  padding: 2px 10px;\n"
"margin-left: 17px;\n"
"margin-right: 23px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #3AB0FF;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #F9F2ED;\n"
"}")
        self.label_start.setReadOnly(True)
        self.label_start.setObjectName("label_start")
        self.horizontalLayout_3.addWidget(self.label_start)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.tab_rpd)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cb_end = QtWidgets.QCheckBox(self.frame_4)
        self.cb_end.setMaximumSize(QtCore.QSize(16, 16777215))
        self.cb_end.setText("")
        self.cb_end.setIconSize(QtCore.QSize(16, 16))
        self.cb_end.setObjectName("cb_end")
        self.horizontalLayout_5.addWidget(self.cb_end)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.label_end = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_end.setFont(font)
        self.label_end.setStyleSheet("QLineEdit {\n"
"  border-radius: 10px;\n"
"  border: 2px solid #F9F2ED;\n"
"  padding: 2px 10px;\n"
"margin-left: 28px;\n"
"margin-right: 23px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #3AB0FF;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #F9F2ED;\n"
"}")
        self.label_end.setReadOnly(True)
        self.label_end.setObjectName("label_end")
        self.horizontalLayout_5.addWidget(self.label_end)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_4.setSpacing(50)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ok_btn = QtWidgets.QPushButton(self.tab_rpd)
        self.ok_btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: #3AB0FF;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #009EFF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #0014FF;\n"
"}")
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout_4.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.tab_rpd)
        self.cancel_btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: #F87474;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f54040;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #f01313;\n"
"}")
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget_first.addTab(self.tab_rpd, "")
        self.tab_rypd = QtWidgets.QWidget()
        self.tab_rypd.setObjectName("tab_rypd")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_rypd)
        self.verticalLayout_12.setContentsMargins(5, 0, 5, 10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_7 = QtWidgets.QFrame(self.tab_rypd)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.cb_speed_start = QtWidgets.QCheckBox(self.frame_7)
        self.cb_speed_start.setMaximumSize(QtCore.QSize(16, 16777215))
        self.cb_speed_start.setText("")
        self.cb_speed_start.setIconSize(QtCore.QSize(16, 16))
        self.cb_speed_start.setObjectName("cb_speed_start")
        self.horizontalLayout_9.addWidget(self.cb_speed_start)
        self.label_14 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.label_speed_start = QtWidgets.QLineEdit(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_speed_start.setFont(font)
        self.label_speed_start.setStyleSheet("QLineEdit {\n"
"  border-radius: 10px;\n"
"  border: 2px solid #F9F2ED;\n"
"  padding: 2px 10px;\n"
"margin-left: 15px;\n"
"margin-right: 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #3AB0FF;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #F9F2ED;\n"
"}")
        self.label_speed_start.setReadOnly(True)
        self.label_speed_start.setObjectName("label_speed_start")
        self.horizontalLayout_9.addWidget(self.label_speed_start)
        self.label_15 = QtWidgets.QLabel(self.frame_7)
        self.label_15.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.verticalLayout_12.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.tab_rypd)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cb_speed_end = QtWidgets.QCheckBox(self.frame_6)
        self.cb_speed_end.setMaximumSize(QtCore.QSize(16, 16777215))
        self.cb_speed_end.setText("")
        self.cb_speed_end.setIconSize(QtCore.QSize(16, 16))
        self.cb_speed_end.setObjectName("cb_speed_end")
        self.horizontalLayout_8.addWidget(self.cb_speed_end)
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.label_speed_end = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_speed_end.setFont(font)
        self.label_speed_end.setStyleSheet("QLineEdit {\n"
"  border-radius: 10px;\n"
"  border: 2px solid #F9F2ED;\n"
"  padding: 2px 10px;\n"
"margin-left: 15px;\n"
"margin-right: 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #3AB0FF;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #F9F2ED;\n"
"}")
        self.label_speed_end.setReadOnly(True)
        self.label_speed_end.setObjectName("label_speed_end")
        self.horizontalLayout_8.addWidget(self.label_speed_end)
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout_12.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.tab_rypd)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.cb_boost = QtWidgets.QCheckBox(self.frame_9)
        self.cb_boost.setMaximumSize(QtCore.QSize(16, 16777215))
        self.cb_boost.setText("")
        self.cb_boost.setIconSize(QtCore.QSize(16, 16))
        self.cb_boost.setObjectName("cb_boost")
        self.horizontalLayout_11.addWidget(self.cb_boost)
        self.label_19 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_11.addWidget(self.label_19)
        self.label_boost = QtWidgets.QLineEdit(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_boost.setFont(font)
        self.label_boost.setStyleSheet("QLineEdit {\n"
"  border-radius: 10px;\n"
"  border: 2px solid #F9F2ED;\n"
"  padding: 2px 10px;\n"
"margin-left: 15px;\n"
"margin-right: 7px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #3AB0FF;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #F9F2ED;\n"
"}")
        self.label_boost.setReadOnly(True)
        self.label_boost.setObjectName("label_boost")
        self.horizontalLayout_11.addWidget(self.label_boost)
        self.label_20 = QtWidgets.QLabel(self.frame_9)
        self.label_20.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_11.addWidget(self.label_20)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.verticalLayout_12.addWidget(self.frame_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.cb_time_2 = QtWidgets.QCheckBox(self.tab_rypd)
        self.cb_time_2.setMaximumSize(QtCore.QSize(16, 16777215))
        self.cb_time_2.setText("")
        self.cb_time_2.setIconSize(QtCore.QSize(16, 16))
        self.cb_time_2.setObjectName("cb_time_2")
        self.horizontalLayout_12.addWidget(self.cb_time_2)
        self.label_21 = QtWidgets.QLabel(self.tab_rypd)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_12.addWidget(self.label_21)
        self.label_time_2 = QtWidgets.QLineEdit(self.tab_rypd)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_2.setFont(font)
        self.label_time_2.setStyleSheet("QLineEdit {\n"
"  border-radius: 10px;\n"
"  border: 2px solid #F9F2ED;\n"
"  padding: 2px 10px;\n"
"margin-left: 45px;\n"
"margin-right: 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #3AB0FF;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #F9F2ED;\n"
"}")
        self.label_time_2.setReadOnly(True)
        self.label_time_2.setObjectName("label_time_2")
        self.horizontalLayout_12.addWidget(self.label_time_2)
        self.label_22 = QtWidgets.QLabel(self.tab_rypd)
        self.label_22.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_12.addWidget(self.label_22)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.frame_5 = QtWidgets.QFrame(self.tab_rypd)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cb_start_2 = QtWidgets.QCheckBox(self.frame_5)
        self.cb_start_2.setMaximumSize(QtCore.QSize(16, 16777215))
        self.cb_start_2.setText("")
        self.cb_start_2.setIconSize(QtCore.QSize(16, 16))
        self.cb_start_2.setObjectName("cb_start_2")
        self.horizontalLayout_6.addWidget(self.cb_start_2)
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.label_start_2 = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_start_2.setFont(font)
        self.label_start_2.setStyleSheet("QLineEdit {\n"
"  border-radius: 10px;\n"
"  border: 2px solid #F9F2ED;\n"
"  padding: 2px 10px;\n"
"margin-left: 15px;\n"
"margin-right: 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #3AB0FF;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #F9F2ED;\n"
"}")
        self.label_start_2.setReadOnly(True)
        self.label_start_2.setObjectName("label_start_2")
        self.horizontalLayout_6.addWidget(self.label_start_2)
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_12.addWidget(self.frame_5)
        self.frame_8 = QtWidgets.QFrame(self.tab_rypd)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.cb_end_2 = QtWidgets.QCheckBox(self.frame_8)
        self.cb_end_2.setMaximumSize(QtCore.QSize(16, 16777215))
        self.cb_end_2.setText("")
        self.cb_end_2.setIconSize(QtCore.QSize(16, 16))
        self.cb_end_2.setObjectName("cb_end_2")
        self.horizontalLayout_10.addWidget(self.cb_end_2)
        self.label_16 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.label_end_2 = QtWidgets.QLineEdit(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_end_2.setFont(font)
        self.label_end_2.setStyleSheet("QLineEdit {\n"
"  border-radius: 10px;\n"
"  border: 2px solid #F9F2ED;\n"
"  padding: 2px 10px;\n"
"margin-left: 25px;\n"
"margin-right: 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #3AB0FF;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #F9F2ED;\n"
"}")
        self.label_end_2.setReadOnly(True)
        self.label_end_2.setObjectName("label_end_2")
        self.horizontalLayout_10.addWidget(self.label_end_2)
        self.label_17 = QtWidgets.QLabel(self.frame_8)
        self.label_17.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.verticalLayout_12.addWidget(self.frame_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_7.setSpacing(50)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ok_btn_2 = QtWidgets.QPushButton(self.tab_rypd)
        self.ok_btn_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ok_btn_2.setFont(font)
        self.ok_btn_2.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: #3AB0FF;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #009EFF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #0014FF;\n"
"}")
        self.ok_btn_2.setObjectName("ok_btn_2")
        self.horizontalLayout_7.addWidget(self.ok_btn_2)
        self.cancel_btn_2 = QtWidgets.QPushButton(self.tab_rypd)
        self.cancel_btn_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn_2.setFont(font)
        self.cancel_btn_2.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: #F87474;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f54040;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #f01313;\n"
"}")
        self.cancel_btn_2.setObjectName("cancel_btn_2")
        self.horizontalLayout_7.addWidget(self.cancel_btn_2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.tabWidget_first.addTab(self.tab_rypd, "")
        self.verticalLayout.addWidget(self.tabWidget_first)

        self.retranslateUi(Dialog)
        self.tabWidget_first.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_23.setText(_translate("Dialog", "Скорость:"))
        self.label_3.setText(_translate("Dialog", "м/с"))
        self.label_4.setText(_translate("Dialog", "Время:"))
        self.label_5.setText(_translate("Dialog", "с"))
        self.label_6.setText(_translate("Dialog", "Начальная\n"
"позиция:"))
        self.label_start.setPlaceholderText(_translate("Dialog", "0"))
        self.label_7.setText(_translate("Dialog", "м"))
        self.label_8.setText(_translate("Dialog", "Конечная\n"
"позиция:"))
        self.label_9.setText(_translate("Dialog", "м"))
        self.ok_btn.setText(_translate("Dialog", "продолжить"))
        self.cancel_btn.setText(_translate("Dialog", "отмена"))
        self.tabWidget_first.setTabText(self.tabWidget_first.indexOf(self.tab_rpd), _translate("Dialog", "РПД"))
        self.label_14.setText(_translate("Dialog", "Начальная\n"
"скорость:"))
        self.label_15.setText(_translate("Dialog", "м/с"))
        self.label_12.setText(_translate("Dialog", "Конечная\n"
"скорость:"))
        self.label_13.setText(_translate("Dialog", "м/с"))
        self.label_19.setText(_translate("Dialog", "Ускорение:"))
        self.label_20.setText(_translate("Dialog", "м/с²"))
        self.label_21.setText(_translate("Dialog", "Время:"))
        self.label_22.setText(_translate("Dialog", "с"))
        self.label_10.setText(_translate("Dialog", "Начальная\n"
"позиция:"))
        self.label_start_2.setPlaceholderText(_translate("Dialog", "0"))
        self.label_11.setText(_translate("Dialog", "м"))
        self.label_16.setText(_translate("Dialog", "Конечная\n"
"позиция:"))
        self.label_17.setText(_translate("Dialog", "м"))
        self.ok_btn_2.setText(_translate("Dialog", "продолжить"))
        self.cancel_btn_2.setText(_translate("Dialog", "отмена"))
        self.tabWidget_first.setTabText(self.tabWidget_first.indexOf(self.tab_rypd), _translate("Dialog", "РУПД"))
