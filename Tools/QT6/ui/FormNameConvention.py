# Form implementation generated from reading ui file 'name_convention.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(289, 170)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.side_label = QtWidgets.QLabel(parent=Form)
        self.side_label.setObjectName("side_label")
        self.horizontalLayout_3.addWidget(self.side_label)
        self.side_comboBox = QtWidgets.QComboBox(parent=Form)
        self.side_comboBox.setObjectName("side_comboBox")
        self.horizontalLayout_3.addWidget(self.side_comboBox)
        self.side_push_button = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_push_button.sizePolicy().hasHeightForWidth())
        self.side_push_button.setSizePolicy(sizePolicy)
        self.side_push_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.side_push_button.setObjectName("side_push_button")
        self.horizontalLayout_3.addWidget(self.side_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_label = QtWidgets.QLabel(parent=Form)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout.addWidget(self.name_label)
        self.name_lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.horizontalLayout.addWidget(self.name_lineEdit)
        self.name_button = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_button.sizePolicy().hasHeightForWidth())
        self.name_button.setSizePolicy(sizePolicy)
        self.name_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.name_button.setObjectName("name_button")
        self.horizontalLayout.addWidget(self.name_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.default_system_chkBox = QtWidgets.QCheckBox(parent=Form)
        self.default_system_chkBox.setText("")
        self.default_system_chkBox.setChecked(True)
        self.default_system_chkBox.setObjectName("default_system_chkBox")
        self.horizontalLayout_2.addWidget(self.default_system_chkBox)
        self.system_label = QtWidgets.QLabel(parent=Form)
        self.system_label.setObjectName("system_label")
        self.horizontalLayout_2.addWidget(self.system_label)
        self.system_lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.system_lineEdit.setObjectName("system_lineEdit")
        self.horizontalLayout_2.addWidget(self.system_lineEdit)
        self.system_button = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.system_button.sizePolicy().hasHeightForWidth())
        self.system_button.setSizePolicy(sizePolicy)
        self.system_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.system_button.setObjectName("system_button")
        self.horizontalLayout_2.addWidget(self.system_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.object_type_label = QtWidgets.QLabel(parent=Form)
        self.object_type_label.setObjectName("object_type_label")
        self.horizontalLayout_4.addWidget(self.object_type_label)
        self.objectType_comboBox = QtWidgets.QComboBox(parent=Form)
        self.objectType_comboBox.setObjectName("objectType_comboBox")
        self.horizontalLayout_4.addWidget(self.objectType_comboBox)
        self.object_type_button = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_type_button.sizePolicy().hasHeightForWidth())
        self.object_type_button.setSizePolicy(sizePolicy)
        self.object_type_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.object_type_button.setObjectName("object_type_button")
        self.horizontalLayout_4.addWidget(self.object_type_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.rename_button = QtWidgets.QPushButton(parent=Form)
        self.rename_button.setObjectName("rename_button")
        self.verticalLayout.addWidget(self.rename_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.side_label.setText(_translate("Form", "side:"))
        self.side_push_button.setText(_translate("Form", ">"))
        self.name_label.setText(_translate("Form", " name :"))
        self.name_button.setText(_translate("Form", ">"))
        self.system_label.setText(_translate("Form", "system:"))
        self.system_button.setText(_translate("Form", ">"))
        self.object_type_label.setText(_translate("Form", "object type:"))
        self.object_type_button.setText(_translate("Form", ">"))
        self.rename_button.setText(_translate("Form", "rename"))
