# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_BipedRig.ui'
#
# Created: Tue Mar 15 20:23:49 2022
#      by: PySide2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(234, 172)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.AutoRigTab = QtWidgets.QTabWidget(Form)
        self.AutoRigTab.setObjectName("AutoRigTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.heightLabel = QtWidgets.QLabel(self.tab)
        self.heightLabel.setMinimumSize(QtCore.QSize(20, 0))
        self.heightLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.heightLabel.setTextFormat(QtCore.Qt.PlainText)
        self.heightLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.heightLabel.setObjectName("heightLabel")
        self.horizontalLayout.addWidget(self.heightLabel)
        self.HeightSpnBox = QtWidgets.QDoubleSpinBox(self.tab)
        self.HeightSpnBox.setMaximum(1000000.0)
        self.HeightSpnBox.setProperty("value", 75.0)
        self.HeightSpnBox.setObjectName("HeightSpnBox")
        self.horizontalLayout.addWidget(self.HeightSpnBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.CreateReferencePointsBtn = QtWidgets.QPushButton(self.tab)
        self.CreateReferencePointsBtn.setObjectName("CreateReferencePointsBtn")
        self.verticalLayout.addWidget(self.CreateReferencePointsBtn)
        self.MirrorSelectionBtn = QtWidgets.QPushButton(self.tab)
        self.MirrorSelectionBtn.setObjectName("MirrorSelectionBtn")
        self.verticalLayout.addWidget(self.MirrorSelectionBtn)
        self.CreateRigBtn = QtWidgets.QPushButton(self.tab)
        self.CreateRigBtn.setObjectName("CreateRigBtn")
        self.verticalLayout.addWidget(self.CreateRigBtn)
        self.AutoRigTab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SkeletonHandsBtn = QtWidgets.QPushButton(self.tab_2)
        self.SkeletonHandsBtn.setObjectName("SkeletonHandsBtn")
        self.verticalLayout_2.addWidget(self.SkeletonHandsBtn)
        self.supportScaleRigBtn = QtWidgets.QPushButton(self.tab_2)
        self.supportScaleRigBtn.setObjectName("supportScaleRigBtn")
        self.verticalLayout_2.addWidget(self.supportScaleRigBtn)
        self.feetOrientationBtn = QtWidgets.QPushButton(self.tab_2)
        self.feetOrientationBtn.setObjectName("feetOrientationBtn")
        self.verticalLayout_2.addWidget(self.feetOrientationBtn)
        self.AutoRigTab.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ClavicleSpaceSwitchBtn = QtWidgets.QPushButton(self.tab_5)
        self.ClavicleSpaceSwitchBtn.setObjectName("ClavicleSpaceSwitchBtn")
        self.verticalLayout_4.addWidget(self.ClavicleSpaceSwitchBtn)
        self.PoleVectorBtn = QtWidgets.QPushButton(self.tab_5)
        self.PoleVectorBtn.setObjectName("PoleVectorBtn")
        self.verticalLayout_4.addWidget(self.PoleVectorBtn)
        self.label = QtWidgets.QLabel(self.tab_5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.AutoRigTab.addTab(self.tab_5, "")
        self.verticalLayout_3.addWidget(self.AutoRigTab)

        self.retranslateUi(Form)
        self.AutoRigTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.heightLabel.setText(QtWidgets.QApplication.translate("Form", "Height", None, -1))
        self.CreateReferencePointsBtn.setText(QtWidgets.QApplication.translate("Form", "Create Reference Points", None, -1))
        self.MirrorSelectionBtn.setText(QtWidgets.QApplication.translate("Form", "Mirror Selection", None, -1))
        self.CreateRigBtn.setText(QtWidgets.QApplication.translate("Form", "CreateRig", None, -1))
        self.AutoRigTab.setTabText(self.AutoRigTab.indexOf(self.tab), QtWidgets.QApplication.translate("Form", "AutoRig", None, -1))
        self.SkeletonHandsBtn.setText(QtWidgets.QApplication.translate("Form", "Skeleton Hands", None, -1))
        self.supportScaleRigBtn.setText(QtWidgets.QApplication.translate("Form", "Support Scale Rig", None, -1))
        self.feetOrientationBtn.setText(QtWidgets.QApplication.translate("Form", "Correct Feet Orientation", None, -1))
        self.AutoRigTab.setTabText(self.AutoRigTab.indexOf(self.tab_2), QtWidgets.QApplication.translate("Form", "Snipets", None, -1))
        self.ClavicleSpaceSwitchBtn.setText(QtWidgets.QApplication.translate("Form", "Clavicle Space Switch", None, -1))
        self.PoleVectorBtn.setText(QtWidgets.QApplication.translate("Form", "Correct P Vector Orient", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "All deprecated snippets are all ready\n"
" included on the autorig default creation", None, -1))
        self.AutoRigTab.setTabText(self.AutoRigTab.indexOf(self.tab_5), QtWidgets.QApplication.translate("Form", "Deprecated", None, -1))

