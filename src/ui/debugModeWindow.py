# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DebugModeWindowkSSrRb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import logging

class QTextEditLogger(logging.Handler, QObject):
    appendPlainText = pyqtSignal(str) # Safe for multi Thread
    def __init__(self, parent):
        super().__init__()
        QObject.__init__(self)
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)
        self.appendPlainText.connect(self.widget.appendPlainText)

    def emit(self, record):
        msg = self.format(record)
        if self.widget.blockCount() > 1000:
            self.widget.setPlainText("")
        self.appendPlainText.emit(msg)

class Ui_debugModeWindow(object):
    def setupUi(self, debugModeWindow):
        if not debugModeWindow.objectName():
            debugModeWindow.setObjectName(u"debugModeWindow")
        debugModeWindow.resize(400, 400)
        debugModeWindow.setMinimumSize(QSize(400, 400))
        debugModeWindow.setMaximumSize(QSize(1920, 1080))
        debugModeWindow.setWindowTitle(u"Debug Mode Window")
        self.centralwidget = QWidget(debugModeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.currentDanserExecArgmentsVerticalLayout = QVBoxLayout()
        self.currentDanserExecArgmentsVerticalLayout.setObjectName(u"currentDanserExecArgmentsVerticalLayout")
        self.currentDanserExecArgmentsLabel = QLabel(debugModeWindow)
        self.currentDanserExecArgmentsLabel.setObjectName(u"currentDanserExecArgmentsLabel")
        self.currentDanserExecArgmentsLabel.setText(u"Current Danser Execute Argments:")

        self.currentDanserExecArgmentsVerticalLayout.addWidget(self.currentDanserExecArgmentsLabel)

        self.currentDanserExecArgmentsLineEdit = QLineEdit(debugModeWindow)
        self.currentDanserExecArgmentsLineEdit.setObjectName(u"currentDanserExecArgmentsLineEdit")
        self.currentDanserExecArgmentsLineEdit.setReadOnly(True)

        self.currentDanserExecArgmentsVerticalLayout.addWidget(self.currentDanserExecArgmentsLineEdit)


        self.verticalLayout.addLayout(self.currentDanserExecArgmentsVerticalLayout)

        self.recordingOutputNameVerticalLayout = QVBoxLayout()
        self.recordingOutputNameVerticalLayout.setObjectName(u"recordingOutputNameVerticalLayout")
        self.recordingOutputNameLabel = QLabel(debugModeWindow)
        self.recordingOutputNameLabel.setObjectName(u"recordingOutputNameLabel")
        self.recordingOutputNameLabel.setText(u"Recording Output File Name:")

        self.recordingOutputNameVerticalLayout.addWidget(self.recordingOutputNameLabel)

        self.recordingOutputNameLineEdit = QLineEdit(debugModeWindow)
        self.recordingOutputNameLineEdit.setObjectName(u"recordingOutputNameLineEdit")
        self.recordingOutputNameLineEdit.setReadOnly(True)

        self.recordingOutputNameVerticalLayout.addWidget(self.recordingOutputNameLineEdit)


        self.verticalLayout.addLayout(self.recordingOutputNameVerticalLayout)

        self.fullLogVerticalLayout = QVBoxLayout()
        self.fullLogVerticalLayout.setObjectName(u"fullLogVerticalLayout")
        self.fullLogLabel = QLabel(debugModeWindow)
        self.fullLogLabel.setObjectName(u"fullLogLabel")
        self.fullLogLabel.setText(u"Full Log:")
        self.fullLogVerticalLayout.addWidget(self.fullLogLabel)

        self.fullLogPlainTextEdit = QTextEditLogger(debugModeWindow)
        self.fullLogPlainTextEdit.widget.setObjectName(u"fullLogPlainTextEdit")
        self.fullLogVerticalLayout.addWidget(self.fullLogPlainTextEdit.widget)

        self.verticalLayout.addLayout(self.fullLogVerticalLayout)

        debugModeWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(debugModeWindow)

    # setupUi




