# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_BlendShapeEditor.ui'
#
# Created: Tue Mar 15 20:23:49 2022
#      by: PySide2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(786, 730)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.BlendShapeRebuilderLabel = QtWidgets.QLabel(Form)
        self.BlendShapeRebuilderLabel.setObjectName("BlendShapeRebuilderLabel")
        self.verticalLayout_5.addWidget(self.BlendShapeRebuilderLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.CurrentBSlbl = QtWidgets.QLabel(Form)
        self.CurrentBSlbl.setMaximumSize(QtCore.QSize(108, 16777215))
        self.CurrentBSlbl.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CurrentBSlbl.setObjectName("CurrentBSlbl")
        self.horizontalLayout_3.addWidget(self.CurrentBSlbl)
        self.BlendShapeNodeNamelbl = QtWidgets.QLabel(Form)
        self.BlendShapeNodeNamelbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BlendShapeNodeNamelbl.setObjectName("BlendShapeNodeNamelbl")
        self.horizontalLayout_3.addWidget(self.BlendShapeNodeNamelbl)
        self.GetBlendshapeBtn = QtWidgets.QPushButton(Form)
        self.GetBlendshapeBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.GetBlendshapeBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.GetBlendshapeBtn.setObjectName("GetBlendshapeBtn")
        self.horizontalLayout_3.addWidget(self.GetBlendshapeBtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RebuildTargetsFromSelectionBtn = QtWidgets.QPushButton(Form)
        self.RebuildTargetsFromSelectionBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.RebuildTargetsFromSelectionBtn.setObjectName("RebuildTargetsFromSelectionBtn")
        self.horizontalLayout_2.addWidget(self.RebuildTargetsFromSelectionBtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ReplaceBlendShapeInputBtn = QtWidgets.QPushButton(Form)
        self.ReplaceBlendShapeInputBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.ReplaceBlendShapeInputBtn.setObjectName("ReplaceBlendShapeInputBtn")
        self.verticalLayout.addWidget(self.ReplaceBlendShapeInputBtn)
        self.BlendShapeNodesLbl = QtWidgets.QLabel(Form)
        self.BlendShapeNodesLbl.setObjectName("BlendShapeNodesLbl")
        self.verticalLayout.addWidget(self.BlendShapeNodesLbl)
        self.BlendShapeNodeTbl = QtWidgets.QListWidget(Form)
        self.BlendShapeNodeTbl.setObjectName("BlendShapeNodeTbl")
        self.verticalLayout.addWidget(self.BlendShapeNodeTbl)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.RebuildSelectedTargets = QtWidgets.QPushButton(Form)
        self.RebuildSelectedTargets.setMinimumSize(QtCore.QSize(0, 40))
        self.RebuildSelectedTargets.setObjectName("RebuildSelectedTargets")
        self.verticalLayout_2.addWidget(self.RebuildSelectedTargets)
        self.TargetGroupsLbl = QtWidgets.QLabel(Form)
        self.TargetGroupsLbl.setObjectName("TargetGroupsLbl")
        self.verticalLayout_2.addWidget(self.TargetGroupsLbl)
        self.InputTargetGroupAlias = QtWidgets.QListWidget(Form)
        self.InputTargetGroupAlias.setObjectName("InputTargetGroupAlias")
        self.verticalLayout_2.addWidget(self.InputTargetGroupAlias)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ReplaceTargetWithSelBtn = QtWidgets.QPushButton(Form)
        self.ReplaceTargetWithSelBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.ReplaceTargetWithSelBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ReplaceTargetWithSelBtn.setObjectName("ReplaceTargetWithSelBtn")
        self.verticalLayout_3.addWidget(self.ReplaceTargetWithSelBtn)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.TargetList = QtWidgets.QListWidget(Form)
        self.TargetList.setObjectName("TargetList")
        self.verticalLayout_3.addWidget(self.TargetList)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.CorrectVtxPosBtn = QtWidgets.QLabel(Form)
        self.CorrectVtxPosBtn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CorrectVtxPosBtn.setObjectName("CorrectVtxPosBtn")
        self.verticalLayout_4.addWidget(self.CorrectVtxPosBtn)
        self.LoadSelectionBtn = QtWidgets.QPushButton(Form)
        self.LoadSelectionBtn.setObjectName("LoadSelectionBtn")
        self.verticalLayout_4.addWidget(self.LoadSelectionBtn)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_4.addWidget(self.listWidget)
        self.CorrectVtxBtn = QtWidgets.QPushButton(Form)
        self.CorrectVtxBtn.setMinimumSize(QtCore.QSize(100, 30))
        self.CorrectVtxBtn.setObjectName("CorrectVtxBtn")
        self.verticalLayout_4.addWidget(self.CorrectVtxBtn)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.BlendShapeRebuilderLabel.setText(QtWidgets.QApplication.translate("Form", "Blend Shape Rebuilder", None, -1))
        self.CurrentBSlbl.setText(QtWidgets.QApplication.translate("Form", "Current Blend Shape:", None, -1))
        self.BlendShapeNodeNamelbl.setText(QtWidgets.QApplication.translate("Form", "No Blendshape Node Selected", None, -1))
        self.GetBlendshapeBtn.setText(QtWidgets.QApplication.translate("Form", "Get BlendShape Node\n"
"From Selection", None, -1))
        self.RebuildTargetsFromSelectionBtn.setText(QtWidgets.QApplication.translate("Form", "Rebuild targets from \n"
"selected node", None, -1))
        self.ReplaceBlendShapeInputBtn.setText(QtWidgets.QApplication.translate("Form", "Replace BS Input \n"
" with selection", None, -1))
        self.BlendShapeNodesLbl.setText(QtWidgets.QApplication.translate("Form", "BlendShape Nodes", None, -1))
        self.RebuildSelectedTargets.setText(QtWidgets.QApplication.translate("Form", "Rebuild selected targets", None, -1))
        self.TargetGroupsLbl.setText(QtWidgets.QApplication.translate("Form", "Target Groups Alias", None, -1))
        self.ReplaceTargetWithSelBtn.setText(QtWidgets.QApplication.translate("Form", "Replace Selected Target \n"
"With Selection", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "BlendShape Targets", None, -1))
        self.CorrectVtxPosBtn.setText(QtWidgets.QApplication.translate("Form", "Vertex Position Correction", None, -1))
        self.LoadSelectionBtn.setToolTip(QtWidgets.QApplication.translate("Form", "Load Targets you want to correct, then select the vertex on the original shape that you want to transfer to this targets. ", None, -1))
        self.LoadSelectionBtn.setText(QtWidgets.QApplication.translate("Form", "Load Selection", None, -1))
        self.CorrectVtxBtn.setText(QtWidgets.QApplication.translate("Form", "Correct With \n"
"Selected Verices", None, -1))

