# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RMblendShapeEditor.ui'
#
# Created: Mon Sep 26 14:23:46 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(786, 730)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.BlendShapeRebuilderLabel = QtGui.QLabel(Form)
        self.BlendShapeRebuilderLabel.setObjectName("BlendShapeRebuilderLabel")
        self.verticalLayout_5.addWidget(self.BlendShapeRebuilderLabel)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.CurrentBSlbl = QtGui.QLabel(Form)
        self.CurrentBSlbl.setMaximumSize(QtCore.QSize(108, 16777215))
        self.CurrentBSlbl.setFrameShadow(QtGui.QFrame.Plain)
        self.CurrentBSlbl.setObjectName("CurrentBSlbl")
        self.horizontalLayout_3.addWidget(self.CurrentBSlbl)
        self.BlendShapeNodeNamelbl = QtGui.QLabel(Form)
        self.BlendShapeNodeNamelbl.setFrameShape(QtGui.QFrame.NoFrame)
        self.BlendShapeNodeNamelbl.setObjectName("BlendShapeNodeNamelbl")
        self.horizontalLayout_3.addWidget(self.BlendShapeNodeNamelbl)
        self.GetBlendshapeBtn = QtGui.QPushButton(Form)
        self.GetBlendshapeBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.GetBlendshapeBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.GetBlendshapeBtn.setObjectName("GetBlendshapeBtn")
        self.horizontalLayout_3.addWidget(self.GetBlendshapeBtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RebuildTargetsFromSelectionBtn = QtGui.QPushButton(Form)
        self.RebuildTargetsFromSelectionBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.RebuildTargetsFromSelectionBtn.setObjectName("RebuildTargetsFromSelectionBtn")
        self.horizontalLayout_2.addWidget(self.RebuildTargetsFromSelectionBtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ReplaceBlendShapeInputBtn = QtGui.QPushButton(Form)
        self.ReplaceBlendShapeInputBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.ReplaceBlendShapeInputBtn.setObjectName("ReplaceBlendShapeInputBtn")
        self.verticalLayout.addWidget(self.ReplaceBlendShapeInputBtn)
        self.BlendShapeNodesLbl = QtGui.QLabel(Form)
        self.BlendShapeNodesLbl.setObjectName("BlendShapeNodesLbl")
        self.verticalLayout.addWidget(self.BlendShapeNodesLbl)
        self.BlendShapeNodeTbl = QtGui.QListWidget(Form)
        self.BlendShapeNodeTbl.setObjectName("BlendShapeNodeTbl")
        self.verticalLayout.addWidget(self.BlendShapeNodeTbl)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.RebuildSelectedTargets = QtGui.QPushButton(Form)
        self.RebuildSelectedTargets.setMinimumSize(QtCore.QSize(0, 40))
        self.RebuildSelectedTargets.setObjectName("RebuildSelectedTargets")
        self.verticalLayout_2.addWidget(self.RebuildSelectedTargets)
        self.TargetGroupsLbl = QtGui.QLabel(Form)
        self.TargetGroupsLbl.setObjectName("TargetGroupsLbl")
        self.verticalLayout_2.addWidget(self.TargetGroupsLbl)
        self.InputTargetGroupAlias = QtGui.QListWidget(Form)
        self.InputTargetGroupAlias.setObjectName("InputTargetGroupAlias")
        self.verticalLayout_2.addWidget(self.InputTargetGroupAlias)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ReplaceTargetWithSelBtn = QtGui.QPushButton(Form)
        self.ReplaceTargetWithSelBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.ReplaceTargetWithSelBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ReplaceTargetWithSelBtn.setObjectName("ReplaceTargetWithSelBtn")
        self.verticalLayout_3.addWidget(self.ReplaceTargetWithSelBtn)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.TargetList = QtGui.QListWidget(Form)
        self.TargetList.setObjectName("TargetList")
        self.verticalLayout_3.addWidget(self.TargetList)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.CorrectVtxPosBtn = QtGui.QLabel(Form)
        self.CorrectVtxPosBtn.setFrameShape(QtGui.QFrame.NoFrame)
        self.CorrectVtxPosBtn.setObjectName("CorrectVtxPosBtn")
        self.verticalLayout_4.addWidget(self.CorrectVtxPosBtn)
        self.LoadSelectionBtn = QtGui.QPushButton(Form)
        self.LoadSelectionBtn.setObjectName("LoadSelectionBtn")
        self.verticalLayout_4.addWidget(self.LoadSelectionBtn)
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_4.addWidget(self.listWidget)
        self.CorrectVtxBtn = QtGui.QPushButton(Form)
        self.CorrectVtxBtn.setMinimumSize(QtCore.QSize(100, 30))
        self.CorrectVtxBtn.setObjectName("CorrectVtxBtn")
        self.verticalLayout_4.addWidget(self.CorrectVtxBtn)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.BlendShapeRebuilderLabel.setText(QtGui.QApplication.translate("Form", "Blend Shape Rebuilder", None, QtGui.QApplication.UnicodeUTF8))
        self.CurrentBSlbl.setText(QtGui.QApplication.translate("Form", "Current Blend Shape:", None, QtGui.QApplication.UnicodeUTF8))
        self.BlendShapeNodeNamelbl.setText(QtGui.QApplication.translate("Form", "No Blendshape Node Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.GetBlendshapeBtn.setText(QtGui.QApplication.translate("Form", "Get BlendShape Node\n"
"From Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.RebuildTargetsFromSelectionBtn.setText(QtGui.QApplication.translate("Form", "Rebuild targets from \n"
"selected node", None, QtGui.QApplication.UnicodeUTF8))
        self.ReplaceBlendShapeInputBtn.setText(QtGui.QApplication.translate("Form", "Replace BS Input \n"
" with selection", None, QtGui.QApplication.UnicodeUTF8))
        self.BlendShapeNodesLbl.setText(QtGui.QApplication.translate("Form", "BlendShape Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.RebuildSelectedTargets.setText(QtGui.QApplication.translate("Form", "Rebuild selected targets", None, QtGui.QApplication.UnicodeUTF8))
        self.TargetGroupsLbl.setText(QtGui.QApplication.translate("Form", "Target Groups Alias", None, QtGui.QApplication.UnicodeUTF8))
        self.ReplaceTargetWithSelBtn.setText(QtGui.QApplication.translate("Form", "Replace Selected Target \n"
"With Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "BlendShape Targets", None, QtGui.QApplication.UnicodeUTF8))
        self.CorrectVtxPosBtn.setText(QtGui.QApplication.translate("Form", "Vertex Position Correction", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadSelectionBtn.setToolTip(QtGui.QApplication.translate("Form", "Load Targets you want to correct, then select the vertex on the original shape that you want to transfer to this targets. ", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadSelectionBtn.setText(QtGui.QApplication.translate("Form", "Load Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.CorrectVtxBtn.setText(QtGui.QApplication.translate("Form", "Correct With \n"
"Selected Verices", None, QtGui.QApplication.UnicodeUTF8))

