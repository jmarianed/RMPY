# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_RigTools.ui'
#
# Created: Fri Jul 23 00:15:20 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(703, 419)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.MiscGroupBox = QtWidgets.QGroupBox(self.tab)
        self.MiscGroupBox.setObjectName("MiscGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.MiscGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.RenameTool = QtWidgets.QPushButton(self.MiscGroupBox)
        self.RenameTool.setEnabled(False)
        self.RenameTool.setObjectName("RenameTool")
        self.verticalLayout_4.addWidget(self.RenameTool)
        self.ExtractGeoBtn = QtWidgets.QPushButton(self.MiscGroupBox)
        self.ExtractGeoBtn.setObjectName("ExtractGeoBtn")
        self.verticalLayout_4.addWidget(self.ExtractGeoBtn)
        self.ParentConstraintBtn = QtWidgets.QPushButton(self.MiscGroupBox)
        self.ParentConstraintBtn.setObjectName("ParentConstraintBtn")
        self.verticalLayout_4.addWidget(self.ParentConstraintBtn)
        self.AttributeTransferBtn = QtWidgets.QPushButton(self.MiscGroupBox)
        self.AttributeTransferBtn.setToolTip("")
        self.AttributeTransferBtn.setObjectName("AttributeTransferBtn")
        self.verticalLayout_4.addWidget(self.AttributeTransferBtn)
        self.verticalLayout_17.addWidget(self.MiscGroupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.locator_at_average_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.locator_at_average_btn.setObjectName("locator_at_average_btn")
        self.verticalLayout_14.addWidget(self.locator_at_average_btn)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_14.addWidget(self.pushButton)
        self.create_locators_at_nodes_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.create_locators_at_nodes_btn.setObjectName("create_locators_at_nodes_btn")
        self.verticalLayout_14.addWidget(self.create_locators_at_nodes_btn)
        self.three_points_locators_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.three_points_locators_btn.setObjectName("three_points_locators_btn")
        self.verticalLayout_14.addWidget(self.three_points_locators_btn)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_14.addWidget(self.pushButton_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.points_between_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.points_between_btn.setObjectName("points_between_btn")
        self.horizontalLayout_2.addWidget(self.points_between_btn)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.verticalLayout_14.addLayout(self.horizontalLayout_2)
        self.verticalLayout_17.addWidget(self.groupBox_4)
        self.horizontalLayout.addLayout(self.verticalLayout_17)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.ConstShapeLblBtn = QtWidgets.QPushButton(self.groupBox)
        self.ConstShapeLblBtn.setObjectName("ConstShapeLblBtn")
        self.verticalLayout_9.addWidget(self.ConstShapeLblBtn)
        self.SCCombineButton = QtWidgets.QPushButton(self.groupBox)
        self.SCCombineButton.setObjectName("SCCombineButton")
        self.verticalLayout_9.addWidget(self.SCCombineButton)
        self.CopyCvsPosBtn = QtWidgets.QPushButton(self.groupBox)
        self.CopyCvsPosBtn.setObjectName("CopyCvsPosBtn")
        self.verticalLayout_9.addWidget(self.CopyCvsPosBtn)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_9.addWidget(self.pushButton_2)
        self.verticalLayout_11.addWidget(self.groupBox)
        self.AlignGroupBox = QtWidgets.QGroupBox(self.tab)
        self.AlignGroupBox.setObjectName("AlignGroupBox")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.AlignGroupBox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.AlignPosition = QtWidgets.QPushButton(self.AlignGroupBox)
        self.AlignPosition.setObjectName("AlignPosition")
        self.verticalLayout_10.addWidget(self.AlignPosition)
        self.AlignRotation = QtWidgets.QPushButton(self.AlignGroupBox)
        self.AlignRotation.setObjectName("AlignRotation")
        self.verticalLayout_10.addWidget(self.AlignRotation)
        self.AlignAll = QtWidgets.QPushButton(self.AlignGroupBox)
        self.AlignAll.setObjectName("AlignAll")
        self.verticalLayout_10.addWidget(self.AlignAll)
        self.aim_button_btn = QtWidgets.QPushButton(self.AlignGroupBox)
        self.aim_button_btn.setObjectName("aim_button_btn")
        self.verticalLayout_10.addWidget(self.aim_button_btn)
        self.verticalLayout_11.addWidget(self.AlignGroupBox)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.GroupsGroupBox = QtWidgets.QGroupBox(self.tab)
        self.GroupsGroupBox.setObjectName("GroupsGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.GroupsGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CreateChildGroup = QtWidgets.QPushButton(self.GroupsGroupBox)
        self.CreateChildGroup.setObjectName("CreateChildGroup")
        self.verticalLayout.addWidget(self.CreateChildGroup)
        self.groupBox_2 = QtWidgets.QGroupBox(self.GroupsGroupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.worldRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.worldRadio.setObjectName("worldRadio")
        self.horizontalLayout_8.addWidget(self.worldRadio)
        self.parentRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.parentRadio.setObjectName("parentRadio")
        self.horizontalLayout_8.addWidget(self.parentRadio)
        self.insertedRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.insertedRadio.setChecked(True)
        self.insertedRadio.setObjectName("insertedRadio")
        self.horizontalLayout_8.addWidget(self.insertedRadio)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.CreateParentGroup = QtWidgets.QPushButton(self.groupBox_2)
        self.CreateParentGroup.setObjectName("CreateParentGroup")
        self.verticalLayout_7.addWidget(self.CreateParentGroup)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_6.addWidget(self.GroupsGroupBox)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.mirror_selection_btn = QtWidgets.QPushButton(self.tab)
        self.mirror_selection_btn.setObjectName("mirror_selection_btn")
        self.verticalLayout_5.addWidget(self.mirror_selection_btn)
        self.orient_parents_btn = QtWidgets.QPushButton(self.tab)
        self.orient_parents_btn.setObjectName("orient_parents_btn")
        self.verticalLayout_5.addWidget(self.orient_parents_btn)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_13.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.RigGroupBox = QtWidgets.QGroupBox(self.tab_2)
        self.RigGroupBox.setObjectName("RigGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.RigGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.FKOnSelection = QtWidgets.QPushButton(self.RigGroupBox)
        self.FKOnSelection.setObjectName("FKOnSelection")
        self.verticalLayout_2.addWidget(self.FKOnSelection)
        self.IKOnSelection = QtWidgets.QPushButton(self.RigGroupBox)
        self.IKOnSelection.setObjectName("IKOnSelection")
        self.verticalLayout_2.addWidget(self.IKOnSelection)
        self.GenericJointChainRigBtn = QtWidgets.QPushButton(self.RigGroupBox)
        self.GenericJointChainRigBtn.setObjectName("GenericJointChainRigBtn")
        self.verticalLayout_2.addWidget(self.GenericJointChainRigBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_10.addWidget(self.RigGroupBox)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.SkiningToolslabel = QtWidgets.QLabel(self.tab_2)
        self.SkiningToolslabel.setObjectName("SkiningToolslabel")
        self.verticalLayout_3.addWidget(self.SkiningToolslabel)
        self.ListConnectedJoints = QtWidgets.QPushButton(self.tab_2)
        self.ListConnectedJoints.setObjectName("ListConnectedJoints")
        self.verticalLayout_3.addWidget(self.ListConnectedJoints)
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.SelectJoints = QtWidgets.QPushButton(self.tab_2)
        self.SelectJoints.setObjectName("SelectJoints")
        self.verticalLayout_3.addWidget(self.SelectJoints)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_9.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.MiscGroupBox.setTitle(QtWidgets.QApplication.translate("Form", "Misc", None, -1))
        self.RenameTool.setText(QtWidgets.QApplication.translate("Form", "Rename Tool", None, -1))
        self.ExtractGeoBtn.setText(QtWidgets.QApplication.translate("Form", "ExtractGeometry", None, -1))
        self.ParentConstraintBtn.setText(QtWidgets.QApplication.translate("Form", "Parent Constraint", None, -1))
        self.AttributeTransferBtn.setText(QtWidgets.QApplication.translate("Form", "Move Attributes", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("Form", "Create Locators", None, -1))
        self.locator_at_average_btn.setToolTip(QtWidgets.QApplication.translate("Form", "select some vertex or objects and a locator will be created at the average position", None, -1))
        self.locator_at_average_btn.setText(QtWidgets.QApplication.translate("Form", "Locator at average vtx", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Selection at average vtx", None, -1))
        self.create_locators_at_nodes_btn.setText(QtWidgets.QApplication.translate("Form", "Locator at selection", None, -1))
        self.three_points_locators_btn.setToolTip(QtWidgets.QApplication.translate("Form", "select tree points or vertices a locator will be created over the first element, aiming to the second one, and using the third as up vector.", None, -1))
        self.three_points_locators_btn.setText(QtWidgets.QApplication.translate("Form", "Three point aim locator", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Form", "Pole Vector locator", None, -1))
        self.points_between_btn.setText(QtWidgets.QApplication.translate("Form", "Between points", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Form", "EditShapes", None, -1))
        self.ConstShapeLblBtn.setText(QtWidgets.QApplication.translate("Form", "Const Shape Lbl", None, -1))
        self.SCCombineButton.setText(QtWidgets.QApplication.translate("Form", "Combine", None, -1))
        self.CopyCvsPosBtn.setText(QtWidgets.QApplication.translate("Form", "Copy Cvs Position", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "Mirror Shapes", None, -1))
        self.AlignGroupBox.setTitle(QtWidgets.QApplication.translate("Form", "Align Tools", None, -1))
        self.AlignPosition.setText(QtWidgets.QApplication.translate("Form", "AlignPosition", None, -1))
        self.AlignRotation.setText(QtWidgets.QApplication.translate("Form", "AlignRotation", None, -1))
        self.AlignAll.setText(QtWidgets.QApplication.translate("Form", "Align Pos & Rot", None, -1))
        self.aim_button_btn.setText(QtWidgets.QApplication.translate("Form", "Aim to object", None, -1))
        self.GroupsGroupBox.setTitle(QtWidgets.QApplication.translate("Form", "Group Creation", None, -1))
        self.CreateChildGroup.setText(QtWidgets.QApplication.translate("Form", "Create Child Group", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Form", "Parent Group", None, -1))
        self.worldRadio.setText(QtWidgets.QApplication.translate("Form", "world", None, -1))
        self.parentRadio.setText(QtWidgets.QApplication.translate("Form", "parent", None, -1))
        self.insertedRadio.setText(QtWidgets.QApplication.translate("Form", "inserted", None, -1))
        self.CreateParentGroup.setText(QtWidgets.QApplication.translate("Form", "Create Parent Group", None, -1))
        self.mirror_selection_btn.setText(QtWidgets.QApplication.translate("Form", "Mirror selection", None, -1))
        self.orient_parents_btn.setText(QtWidgets.QApplication.translate("Form", "Orient Parents", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("Form", "hierarchyse", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("Form", "Tab 1", None, -1))
        self.RigGroupBox.setTitle(QtWidgets.QApplication.translate("Form", "Rig", None, -1))
        self.FKOnSelection.setToolTip(QtWidgets.QApplication.translate("Form", "Select some locators in order to create an FK Control", None, -1))
        self.FKOnSelection.setText(QtWidgets.QApplication.translate("Form", "FK on selection", None, -1))
        self.IKOnSelection.setToolTip(QtWidgets.QApplication.translate("Form", "Select some locators in order to create an FK Control", None, -1))
        self.IKOnSelection.setText(QtWidgets.QApplication.translate("Form", "IK on selection", None, -1))
        self.GenericJointChainRigBtn.setText(QtWidgets.QApplication.translate("Form", "Generic Joint Chain Rig", None, -1))
        self.SkiningToolslabel.setText(QtWidgets.QApplication.translate("Form", "SkiningTools", None, -1))
        self.ListConnectedJoints.setText(QtWidgets.QApplication.translate("Form", "List Skined Joints", None, -1))
        self.SelectJoints.setText(QtWidgets.QApplication.translate("Form", "Select Joints", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("Form", "Tab 2", None, -1))

