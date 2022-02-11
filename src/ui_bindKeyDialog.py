# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bindKeyDialogAqiLnq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_bindKeyDialog(object):
    def setupUi(self, bindKeyDialog):
        if not bindKeyDialog.objectName():
            bindKeyDialog.setObjectName(u"bindKeyDialog")
        bindKeyDialog.resize(285, 119)
        self.gridLayout = QGridLayout(bindKeyDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bindKeyVerticalLayout = QVBoxLayout()
        self.bindKeyVerticalLayout.setObjectName(u"bindKeyVerticalLayout")
        self.bindKeyVerticalLayout.setContentsMargins(9, 9, 9, 9)
        self.inputKeyInfoLabel = QLabel(bindKeyDialog)
        self.inputKeyInfoLabel.setObjectName(u"inputKeyInfoLabel")
        self.inputKeyInfoLabel.setWordWrap(True)

        self.bindKeyVerticalLayout.addWidget(self.inputKeyInfoLabel)

        self.inputKeyFormLayout = QFormLayout()
        self.inputKeyFormLayout.setObjectName(u"inputKeyFormLayout")
        self.inputKeyLabel = QLabel(bindKeyDialog)
        self.inputKeyLabel.setObjectName(u"inputKeyLabel")

        self.inputKeyFormLayout.setWidget(0, QFormLayout.LabelRole, self.inputKeyLabel)

        self.inputKeyPushButton = QPushButton(bindKeyDialog)
        self.inputKeyPushButton.setObjectName(u"inputKeyPushButton")

        self.inputKeyFormLayout.setWidget(0, QFormLayout.FieldRole, self.inputKeyPushButton)


        self.bindKeyVerticalLayout.addLayout(self.inputKeyFormLayout)

        self.OKCancelButtonBox = QDialogButtonBox(bindKeyDialog)
        self.OKCancelButtonBox.setObjectName(u"OKCancelButtonBox")
        self.OKCancelButtonBox.setOrientation(Qt.Horizontal)
        self.OKCancelButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.OKCancelButtonBox.setCenterButtons(False)

        self.bindKeyVerticalLayout.addWidget(self.OKCancelButtonBox)


        self.gridLayout.addLayout(self.bindKeyVerticalLayout, 0, 0, 1, 1)


        self.retranslateUi(bindKeyDialog)
        self.OKCancelButtonBox.accepted.connect(bindKeyDialog.accept)
        self.OKCancelButtonBox.rejected.connect(bindKeyDialog.reject)

        QMetaObject.connectSlotsByName(bindKeyDialog)
    # setupUi

    def retranslateUi(self, bindKeyDialog):
        bindKeyDialog.setWindowTitle(QCoreApplication.translate("bindKeyDialog", u"bindKeyDialog", None))
        self.inputKeyInfoLabel.setText(QCoreApplication.translate("bindKeyDialog", u"Please press the key you want to bind.", None))
        self.inputKeyLabel.setText(QCoreApplication.translate("bindKeyDialog", u"Your input key is:", None))
        self.inputKeyPushButtonSetDefault()
    # retranslateUi

    def inputKeyPushButtonSetDefault(self):
        self.inputKeyPushButton.setText(QCoreApplication.translate("bindKeyDialog", u"<binding>", None))
        
    def inputKeyPushButtonIsDefault(self):
        return self.inputKeyPushButton.text() == QCoreApplication.translate("bindKeyDialog", u"<binding>", None)

    

