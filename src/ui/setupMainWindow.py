# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setupMainWindowKNDeWp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.widgets import QClickedLineEdit

class Ui_setupMainWindow(object):
    def setupUi(self, setupMainWindow):
        if not setupMainWindow.objectName():
            setupMainWindow.setObjectName(u"setupMainWindow")
        setupMainWindow.resize(400, 220)
        setupMainWindow.setMinimumSize(QSize(400, 220))
        setupMainWindow.setMaximumSize(QSize(800, 440))
        self.centralwidget = QWidget(setupMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.languageFormLayout = QFormLayout()
        self.languageFormLayout.setObjectName(u"languageFormLayout")
        self.languageLabel = QLabel(self.centralwidget)
        self.languageLabel.setObjectName(u"languageLabel")

        self.languageFormLayout.setWidget(0, QFormLayout.LabelRole, self.languageLabel)

        self.languageComboBox = QComboBox(self.centralwidget)
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.setObjectName(u"languageComboBox")

        self.languageFormLayout.setWidget(0, QFormLayout.FieldRole, self.languageComboBox)


        self.gridLayout.addLayout(self.languageFormLayout, 0, 0, 1, 1)

        self.songsDBModeFormLayout = QFormLayout()
        self.songsDBModeFormLayout.setObjectName(u"songsDBModeFormLayout")
        self.songsDBModeLabel = QLabel(self.centralwidget)
        self.songsDBModeLabel.setObjectName(u"songsDBModeLabel")

        self.songsDBModeFormLayout.setWidget(0, QFormLayout.LabelRole, self.songsDBModeLabel)

        self.songsDBModeComboBox = QComboBox(self.centralwidget)
        self.songsDBModeComboBox.addItem(u"osu!")
        self.songsDBModeComboBox.addItem(u"danser")
        self.songsDBModeComboBox.setObjectName(u"songsDBModeComboBox")

        self.songsDBModeFormLayout.setWidget(0, QFormLayout.FieldRole, self.songsDBModeComboBox)


        self.gridLayout.addLayout(self.songsDBModeFormLayout, 0, 1, 1, 1)

        self.osuRootPathFormLayout = QFormLayout()
        self.osuRootPathFormLayout.setObjectName(u"osuRootPathFormLayout")
        self.osuRootPathLabel = QLabel(self.centralwidget)
        self.osuRootPathLabel.setObjectName(u"osuRootPathLabel")

        self.osuRootPathFormLayout.setWidget(0, QFormLayout.LabelRole, self.osuRootPathLabel)

        self.osuRootPathLineEdit = QClickedLineEdit(self.centralwidget)
        self.osuRootPathLineEdit.setObjectName(u"osuRootPathLineEdit")
        self.osuRootPathLineEdit.setReadOnly(True)

        self.osuRootPathFormLayout.setWidget(0, QFormLayout.FieldRole, self.osuRootPathLineEdit)


        self.gridLayout.addLayout(self.osuRootPathFormLayout, 1, 0, 1, 2)

        self.skinsPathFormLayout = QFormLayout()
        self.skinsPathFormLayout.setObjectName(u"skinsPathFormLayout")
        self.skinsPathLabel = QLabel(self.centralwidget)
        self.skinsPathLabel.setObjectName(u"skinsPathLabel")

        self.skinsPathFormLayout.setWidget(0, QFormLayout.LabelRole, self.skinsPathLabel)

        self.skinsPathLineEdit = QClickedLineEdit(self.centralwidget)
        self.skinsPathLineEdit.setObjectName(u"skinsPathLineEdit")
        self.skinsPathLineEdit.setReadOnly(True)

        self.skinsPathFormLayout.setWidget(0, QFormLayout.FieldRole, self.skinsPathLineEdit)


        self.gridLayout.addLayout(self.skinsPathFormLayout, 2, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 1)

        self.songsPathFormLayout = QFormLayout()
        self.songsPathFormLayout.setObjectName(u"songsPathFormLayout")
        self.songsPathLineEdit = QClickedLineEdit(self.centralwidget)
        self.songsPathLineEdit.setObjectName(u"songsPathLineEdit")
        self.songsPathLineEdit.setReadOnly(True)

        self.songsPathFormLayout.setWidget(0, QFormLayout.FieldRole, self.songsPathLineEdit)

        self.songsPathLabel = QLabel(self.centralwidget)
        self.songsPathLabel.setObjectName(u"songsPathLabel")

        self.songsPathFormLayout.setWidget(0, QFormLayout.LabelRole, self.songsPathLabel)


        self.gridLayout.addLayout(self.songsPathFormLayout, 3, 0, 1, 2)

        self.danserPathFormLayout = QFormLayout()
        self.danserPathFormLayout.setObjectName(u"danserPathFormLayout")
        self.danserPathLabel = QLabel(self.centralwidget)
        self.danserPathLabel.setObjectName(u"danserPathLabel")

        self.danserPathFormLayout.setWidget(0, QFormLayout.LabelRole, self.danserPathLabel)

        self.danserPathLineEdit = QClickedLineEdit(self.centralwidget)
        self.danserPathLineEdit.setObjectName(u"danserPathLineEdit")
        self.danserPathLineEdit.setReadOnly(True)

        self.danserPathFormLayout.setWidget(0, QFormLayout.FieldRole, self.danserPathLineEdit)


        self.gridLayout.addLayout(self.danserPathFormLayout, 4, 0, 1, 2)

        setupMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(setupMainWindow)

        QMetaObject.connectSlotsByName(setupMainWindow)
    # setupUi

    def retranslateUi(self, setupMainWindow):
        setupMainWindow.setWindowTitle(QCoreApplication.translate("setupMainWindow", u"Setup", None))
        self.languageLabel.setText(QCoreApplication.translate("setupMainWindow", u"Language:", None))
        self.languageComboBox.setItemText(0, QCoreApplication.translate("setupMainWindow", u"English", None))
        self.languageComboBox.setItemText(1, QCoreApplication.translate("setupMainWindow", u"Chinese(Simplified)", None))

        self.songsDBModeLabel.setText(QCoreApplication.translate("setupMainWindow", u"Songs DB Mode:", None))

        self.osuRootPathLabel.setText(QCoreApplication.translate("setupMainWindow", u"osu! Root Path:", None))
        self.skinsPathLabel.setText(QCoreApplication.translate("setupMainWindow", u"Skins Path:", None))
        self.songsPathLabel.setText(QCoreApplication.translate("setupMainWindow", u"Songs Path:", None))
        self.danserPathLabel.setText(QCoreApplication.translate("setupMainWindow", u"danser Path:", None))
    # retranslateUi

