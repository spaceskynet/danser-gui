# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import QSize, Qt, QCoreApplication, QMetaObject
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import (QWidget, QGridLayout, QTabWidget, QHBoxLayout, QVBoxLayout, QFormLayout, 
                             QLabel, QCheckBox, QPushButton, QGroupBox, QLineEdit, QSlider, QComboBox, QSpinBox, QDoubleSpinBox, QAbstractSpinBox, QRadioButton, QButtonGroup, QSizePolicy)
from ui.widgets import QClickedLineEdit, QClickedLabel
from superqt import QLabeledSlider, QLabeledDoubleSlider, QLabeledRangeSlider, QLabeledDoubleRangeSlider

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(704, 396)
        MainWindow.setMinimumSize(QSize(704, 396))
        MainWindow.setMaximumSize(QSize(2560, 1400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainTabWidget = QTabWidget(self.centralwidget)
        self.mainTabWidget.setObjectName(u"mainTabWidget")
        self.generalTab = QWidget()
        self.generalTab.setObjectName(u"generalTab")
        self.gridLayout_10 = QGridLayout(self.generalTab)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.generalHorizontalLayout = QHBoxLayout()
        self.generalHorizontalLayout.setObjectName(u"generalHorizontalLayout")
        self.startLayout = QGridLayout()
        self.startLayout.setObjectName(u"startLayout")
        self.startLayout.setContentsMargins(10, 10, 10, 10)
        self.startLogo = QClickedLabel(self.generalTab)
        self.startLogo.setObjectName(u"startLogo")
        self.startLogo.setMinimumSize(QSize(275, 275))
        self.startLogo.setAutoFillBackground(False)
        self.startLogo.setStyleSheet(u"background: transparent")

        self.startLayout.addWidget(self.startLogo, 0, 0, 1, 1)


        self.generalHorizontalLayout.addLayout(self.startLayout)

        self.generalSettingVerticalLayout = QVBoxLayout()
        self.generalSettingVerticalLayout.setObjectName(u"generalSettingVerticalLayout")
        self.danserModeAndIsRecordHorizontalLayout = QHBoxLayout()
        self.danserModeAndIsRecordHorizontalLayout.setObjectName(u"danserModeAndIsRecordHorizontalLayout")
        self.danserModeFormLayout = QFormLayout()
        self.danserModeFormLayout.setObjectName(u"danserModeFormLayout")
        self.danserModeLabel = QLabel(self.generalTab)
        self.danserModeLabel.setObjectName(u"danserModeLabel")

        self.danserModeFormLayout.setWidget(0, QFormLayout.LabelRole, self.danserModeLabel)

        self.danserModeComboBox = QComboBox(self.generalTab)
        self.danserModeComboBox.addItem(u"danser")
        self.danserModeComboBox.addItem(u"knockout")
        self.danserModeComboBox.addItem(u"play")
        self.danserModeComboBox.addItem(u"replay")
        self.danserModeComboBox.setObjectName(u"danserModeComboBox")

        self.danserModeFormLayout.setWidget(0, QFormLayout.FieldRole, self.danserModeComboBox)


        self.danserModeAndIsRecordHorizontalLayout.addLayout(self.danserModeFormLayout)

        self.isRecordCheckBox = QCheckBox(self.generalTab)
        self.isRecordCheckBox.setObjectName(u"isRecordCheckBox")

        self.danserModeAndIsRecordHorizontalLayout.addWidget(self.isRecordCheckBox)

        self.openRecordingOutputFolderPushButton = QPushButton(self.generalTab)
        self.openRecordingOutputFolderPushButton.setObjectName(u"openRecordingOutputFolderPushButton")

        self.danserModeAndIsRecordHorizontalLayout.addWidget(self.openRecordingOutputFolderPushButton)


        self.generalSettingVerticalLayout.addLayout(self.danserModeAndIsRecordHorizontalLayout)

        self.osrSelectButton = QPushButton(self.generalTab)
        self.osrSelectButton.setObjectName(u"osrSelectButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.osrSelectButton.sizePolicy().hasHeightForWidth())
        self.osrSelectButton.setSizePolicy(sizePolicy)

        self.generalSettingVerticalLayout.addWidget(self.osrSelectButton)

        self.osuSelectButton = QPushButton(self.generalTab)
        self.osuSelectButton.setObjectName(u"osuSelectButton")
        sizePolicy.setHeightForWidth(self.osuSelectButton.sizePolicy().hasHeightForWidth())
        self.osuSelectButton.setSizePolicy(sizePolicy)

        self.generalSettingVerticalLayout.addWidget(self.osuSelectButton)

        self.replayPathVerticalLayout = QVBoxLayout()
        self.replayPathVerticalLayout.setObjectName(u"replayPathVerticalLayout")
        self.osrPathLabel = QLabel(self.generalTab)
        self.osrPathLabel.setObjectName(u"osrPathLabel")

        self.replayPathVerticalLayout.addWidget(self.osrPathLabel)

        self.osrPathLineEdit = QClickedLineEdit(self.generalTab)
        self.osrPathLineEdit.setObjectName(u"osrPathLineEdit")
        self.osrPathLineEdit.setReadOnly(True)

        self.replayPathVerticalLayout.addWidget(self.osrPathLineEdit)

        self.replayPathVerticalLayout.setStretch(0, 1)
        self.replayPathVerticalLayout.setStretch(1, 1)

        self.generalSettingVerticalLayout.addLayout(self.replayPathVerticalLayout)

        self.beatmapPathVerticalLayout = QVBoxLayout()
        self.beatmapPathVerticalLayout.setObjectName(u"beatmapPathVerticalLayout")
        self.osuPathLabel = QLabel(self.generalTab)
        self.osuPathLabel.setObjectName(u"osuPathLabel")

        self.beatmapPathVerticalLayout.addWidget(self.osuPathLabel)

        self.osuPathLineEdit = QClickedLineEdit(self.generalTab)
        self.osuPathLineEdit.setObjectName(u"osuPathLineEdit")
        self.osuPathLineEdit.setReadOnly(True)

        self.beatmapPathVerticalLayout.addWidget(self.osuPathLineEdit)

        self.beatmapPathVerticalLayout.setStretch(0, 1)
        self.beatmapPathVerticalLayout.setStretch(1, 1)

        self.generalSettingVerticalLayout.addLayout(self.beatmapPathVerticalLayout)

        self.skinsComboBox = QComboBox(self.generalTab)
        self.skinsComboBox.setObjectName(u"skinsComboBox")

        self.generalSettingVerticalLayout.addWidget(self.skinsComboBox)


        self.generalHorizontalLayout.addLayout(self.generalSettingVerticalLayout)

        self.generalHorizontalLayout.setStretch(0, 1)
        self.generalHorizontalLayout.setStretch(1, 1)

        self.gridLayout_10.addLayout(self.generalHorizontalLayout, 0, 0, 1, 1)

        self.mainTabWidget.addTab(self.generalTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.settingsTab.setEnabled(True)
        self.horizontalLayout_3 = QHBoxLayout(self.settingsTab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.settingsHorizontalLayout = QHBoxLayout()
        self.settingsHorizontalLayout.setObjectName(u"settingsHorizontalLayout")
        self.settingsTabWidget = QTabWidget(self.settingsTab)
        self.settingsTabWidget.setObjectName(u"settingsTabWidget")
        self.generalSettings = QWidget()
        self.generalSettings.setObjectName(u"generalSettings")
        self.gridLayout_3 = QGridLayout(self.generalSettings)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.generalSettingsGridLayout = QGridLayout()
        self.generalSettingsGridLayout.setObjectName(u"generalSettingsGridLayout")
        self.generalSettingsGridLayout.setVerticalSpacing(0)
        self.basicGroupBox = QGroupBox(self.generalSettings)
        self.basicGroupBox.setObjectName(u"basicGroupBox")
        self.gridLayout_6 = QGridLayout(self.basicGroupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.empty_widget_8 = QWidget(self.basicGroupBox)
        self.empty_widget_8.setObjectName(u"empty_widget_8")

        self.gridLayout_6.addWidget(self.empty_widget_8, 1, 0, 1, 1)

        self.basicGridLayout = QGridLayout()
        self.basicGridLayout.setObjectName(u"basicGridLayout")
        self.basicGridLayout.setHorizontalSpacing(6)
        self.songsDBGridLayout = QGridLayout()
        self.songsDBGridLayout.setObjectName(u"songsDBGridLayout")
        self.songsDBModeLabel = QLabel(self.basicGroupBox)
        self.songsDBModeLabel.setObjectName(u"songsDBModeLabel")

        self.songsDBGridLayout.addWidget(self.songsDBModeLabel, 0, 0, 1, 2)

        self.songsDBModeComboBox = QComboBox(self.basicGroupBox)
        self.songsDBModeComboBox.addItem(u"osu!")
        self.songsDBModeComboBox.addItem(u"danser")
        self.songsDBModeComboBox.setObjectName(u"songsDBModeComboBox")

        self.songsDBGridLayout.addWidget(self.songsDBModeComboBox, 1, 0, 1, 1)

        self.songsDBUpdatePushButton = QPushButton(self.basicGroupBox)
        self.songsDBUpdatePushButton.setObjectName(u"songsDBUpdatePushButton")

        self.songsDBGridLayout.addWidget(self.songsDBUpdatePushButton, 1, 1, 1, 1)


        self.basicGridLayout.addLayout(self.songsDBGridLayout, 0, 1, 1, 1)

        self.songsPathFormLayout = QFormLayout()
        self.songsPathFormLayout.setObjectName(u"songsPathFormLayout")
        self.songsPathLabel = QLabel(self.basicGroupBox)
        self.songsPathLabel.setObjectName(u"songsPathLabel")

        self.songsPathFormLayout.setWidget(0, QFormLayout.LabelRole, self.songsPathLabel)

        self.songsPathLineEdit = QClickedLineEdit(self.basicGroupBox)
        self.songsPathLineEdit.setObjectName(u"songsPathLineEdit")
        self.songsPathLineEdit.setReadOnly(True)

        self.songsPathFormLayout.setWidget(0, QFormLayout.FieldRole, self.songsPathLineEdit)


        self.basicGridLayout.addLayout(self.songsPathFormLayout, 2, 0, 1, 2)

        self.danserPathFormLayout = QFormLayout()
        self.danserPathFormLayout.setObjectName(u"danserPathFormLayout")
        self.danserPathLabel = QLabel(self.basicGroupBox)
        self.danserPathLabel.setObjectName(u"danserPathLabel")

        self.danserPathFormLayout.setWidget(0, QFormLayout.LabelRole, self.danserPathLabel)

        self.danserPathLineEdit = QClickedLineEdit(self.basicGroupBox)
        self.danserPathLineEdit.setObjectName(u"danserPathLineEdit")
        self.danserPathLineEdit.setReadOnly(True)

        self.danserPathFormLayout.setWidget(0, QFormLayout.FieldRole, self.danserPathLineEdit)


        self.basicGridLayout.addLayout(self.danserPathFormLayout, 4, 0, 1, 2)

        self.languageFormLayout = QFormLayout()
        self.languageFormLayout.setObjectName(u"languageFormLayout")
        self.languageLabel = QLabel(self.basicGroupBox)
        self.languageLabel.setObjectName(u"languageLabel")

        self.languageFormLayout.setWidget(0, QFormLayout.LabelRole, self.languageLabel)

        self.languageComboBox = QComboBox(self.basicGroupBox)
        self.languageComboBox.setObjectName(u"languageComboBox")

        self.languageFormLayout.setWidget(0, QFormLayout.FieldRole, self.languageComboBox)


        self.basicGridLayout.addLayout(self.languageFormLayout, 6, 0, 1, 2)

        self.skinsPathFormLayout = QFormLayout()
        self.skinsPathFormLayout.setObjectName(u"skinsPathFormLayout")
        self.skinsPathLabel = QLabel(self.basicGroupBox)
        self.skinsPathLabel.setObjectName(u"skinsPathLabel")

        self.skinsPathFormLayout.setWidget(0, QFormLayout.LabelRole, self.skinsPathLabel)

        self.skinsPathLineEdit = QClickedLineEdit(self.basicGroupBox)
        self.skinsPathLineEdit.setObjectName(u"skinsPathLineEdit")
        self.skinsPathLineEdit.setReadOnly(True)

        self.skinsPathFormLayout.setWidget(0, QFormLayout.FieldRole, self.skinsPathLineEdit)


        self.basicGridLayout.addLayout(self.skinsPathFormLayout, 3, 0, 1, 2)

        self.osuApiFormLayout = QFormLayout()
        self.osuApiFormLayout.setObjectName(u"osuApiFormLayout")
        self.osuApiPathLabel = QLabel(self.basicGroupBox)
        self.osuApiPathLabel.setObjectName(u"osuApiPathLabel")

        self.osuApiFormLayout.setWidget(0, QFormLayout.LabelRole, self.osuApiPathLabel)

        self.osuApiLineEdit = QLineEdit(self.basicGroupBox)
        self.osuApiLineEdit.setObjectName(u"osuApiLineEdit")
        self.osuApiLineEdit.setEchoMode(QLineEdit.Password)

        self.osuApiFormLayout.setWidget(0, QFormLayout.FieldRole, self.osuApiLineEdit)


        self.basicGridLayout.addLayout(self.osuApiFormLayout, 5, 0, 1, 2)

        self.usernameVerticalLayout = QVBoxLayout()
        self.usernameVerticalLayout.setObjectName(u"usernameVerticalLayout")
        self.usernameLabel = QLabel(self.basicGroupBox)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.usernameVerticalLayout.addWidget(self.usernameLabel)

        self.usernameLineEdit = QLineEdit(self.basicGroupBox)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.usernameVerticalLayout.addWidget(self.usernameLineEdit)


        self.basicGridLayout.addLayout(self.usernameVerticalLayout, 0, 0, 1, 1)

        self.osuRootPathFormLayout = QFormLayout()
        self.osuRootPathFormLayout.setObjectName(u"osuRootPathFormLayout")
        self.osuRootPathLabel = QLabel(self.basicGroupBox)
        self.osuRootPathLabel.setObjectName(u"osuRootPathLabel")

        self.osuRootPathFormLayout.setWidget(0, QFormLayout.LabelRole, self.osuRootPathLabel)

        self.osuRootPathLineEdit = QClickedLineEdit(self.basicGroupBox)
        self.osuRootPathLineEdit.setObjectName(u"osuRootPathLineEdit")
        self.osuRootPathLineEdit.setReadOnly(True)

        self.osuRootPathFormLayout.setWidget(0, QFormLayout.FieldRole, self.osuRootPathLineEdit)


        self.basicGridLayout.addLayout(self.osuRootPathFormLayout, 1, 0, 1, 2)


        self.gridLayout_6.addLayout(self.basicGridLayout, 0, 0, 1, 1)


        self.generalSettingsGridLayout.addWidget(self.basicGroupBox, 0, 0, 2, 1)

        self.volumeGroupBox = QGroupBox(self.generalSettings)
        self.volumeGroupBox.setObjectName(u"volumeGroupBox")
        self.verticalLayout_6 = QVBoxLayout(self.volumeGroupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.volumeVerticalLayout = QVBoxLayout()
        self.volumeVerticalLayout.setObjectName(u"volumeVerticalLayout")
        self.globalVolumeFormLayout = QFormLayout()
        self.globalVolumeFormLayout.setObjectName(u"globalVolumeFormLayout")
        self.globalVolumeLabel = QLabel(self.volumeGroupBox)
        self.globalVolumeLabel.setObjectName(u"globalVolumeLabel")

        self.globalVolumeFormLayout.setWidget(0, QFormLayout.LabelRole, self.globalVolumeLabel)

        self.globalVolumeSlider = QLabeledSlider(self.volumeGroupBox)
        self.globalVolumeSlider.setObjectName(u"globalVolumeSlider")
        self.globalVolumeSlider.setCursor(QCursor(Qt.SizeHorCursor))
        self.globalVolumeSlider.setMouseTracking(False)
        self.globalVolumeSlider.setLayoutDirection(Qt.LeftToRight)
        self.globalVolumeSlider.setAutoFillBackground(False)
        self.globalVolumeSlider.setInputMethodHints(Qt.ImhNone)
        self.globalVolumeSlider.setMaximum(100)
        self.globalVolumeSlider.setValue(100)
        self.globalVolumeSlider.setTracking(False)
        self.globalVolumeSlider.setOrientation(Qt.Horizontal)
        self.globalVolumeSlider.setInvertedAppearance(False)
        self.globalVolumeSlider.setInvertedControls(False)
        self.globalVolumeSlider.setTickPosition(QSlider.NoTicks)

        self.globalVolumeFormLayout.setWidget(0, QFormLayout.FieldRole, self.globalVolumeSlider)


        self.volumeVerticalLayout.addLayout(self.globalVolumeFormLayout)

        self.musicVolumeFormLayout = QFormLayout()
        self.musicVolumeFormLayout.setObjectName(u"musicVolumeFormLayout")
        self.musicVolumeLabel = QLabel(self.volumeGroupBox)
        self.musicVolumeLabel.setObjectName(u"musicVolumeLabel")

        self.musicVolumeFormLayout.setWidget(0, QFormLayout.LabelRole, self.musicVolumeLabel)

        self.musicVolumeSlider = QLabeledSlider(self.volumeGroupBox)
        self.musicVolumeSlider.setObjectName(u"musicVolumeSlider")
        self.musicVolumeSlider.setCursor(QCursor(Qt.SizeHorCursor))
        self.musicVolumeSlider.setMaximum(100)
        self.musicVolumeSlider.setValue(100)
        self.musicVolumeSlider.setOrientation(Qt.Horizontal)

        self.musicVolumeFormLayout.setWidget(0, QFormLayout.FieldRole, self.musicVolumeSlider)


        self.volumeVerticalLayout.addLayout(self.musicVolumeFormLayout)

        self.hitSoundVolumeFormLayout = QFormLayout()
        self.hitSoundVolumeFormLayout.setObjectName(u"hitSoundVolumeFormLayout")
        self.hitSoundVolumeLabel = QLabel(self.volumeGroupBox)
        self.hitSoundVolumeLabel.setObjectName(u"hitSoundVolumeLabel")

        self.hitSoundVolumeFormLayout.setWidget(0, QFormLayout.LabelRole, self.hitSoundVolumeLabel)

        self.hitSoundVolumeSlider = QLabeledSlider(self.volumeGroupBox)
        self.hitSoundVolumeSlider.setObjectName(u"hitSoundVolumeSlider")
        self.hitSoundVolumeSlider.setCursor(QCursor(Qt.SizeHorCursor))
        self.hitSoundVolumeSlider.setMaximum(100)
        self.hitSoundVolumeSlider.setValue(100)
        self.hitSoundVolumeSlider.setOrientation(Qt.Horizontal)
        self.hitSoundVolumeSlider.setInvertedAppearance(False)
        self.hitSoundVolumeSlider.setInvertedControls(False)
        self.hitSoundVolumeSlider.setTickPosition(QSlider.NoTicks)

        self.hitSoundVolumeFormLayout.setWidget(0, QFormLayout.FieldRole, self.hitSoundVolumeSlider)


        self.volumeVerticalLayout.addLayout(self.hitSoundVolumeFormLayout)


        self.verticalLayout_6.addLayout(self.volumeVerticalLayout)


        self.generalSettingsGridLayout.addWidget(self.volumeGroupBox, 1, 1, 1, 1)

        self.graphicsGroupBox = QGroupBox(self.generalSettings)
        self.graphicsGroupBox.setObjectName(u"graphicsGroupBox")
        self.gridLayout_5 = QGridLayout(self.graphicsGroupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsVerticalLayout = QVBoxLayout()
        self.graphicsVerticalLayout.setObjectName(u"graphicsVerticalLayout")
        self.graphicsResolutionHorizontalLayout = QHBoxLayout()
        self.graphicsResolutionHorizontalLayout.setSpacing(6)
        self.graphicsResolutionHorizontalLayout.setObjectName(u"graphicsResolutionHorizontalLayout")
        self.resolutionLabel = QLabel(self.graphicsGroupBox)
        self.resolutionLabel.setObjectName(u"resolutionLabel")

        self.graphicsResolutionHorizontalLayout.addWidget(self.resolutionLabel)

        self.graphicsWidth = QLineEdit(self.graphicsGroupBox)
        self.graphicsWidth.setObjectName(u"graphicsWidth")

        self.graphicsResolutionHorizontalLayout.addWidget(self.graphicsWidth)

        self.resolutionMiddleX = QLabel(self.graphicsGroupBox)
        self.resolutionMiddleX.setObjectName(u"resolutionMiddleX")
        self.resolutionMiddleX.setText(u"x")

        self.graphicsResolutionHorizontalLayout.addWidget(self.resolutionMiddleX)

        self.graphicsHeight = QLineEdit(self.graphicsGroupBox)
        self.graphicsHeight.setObjectName(u"graphicsHeight")

        self.graphicsResolutionHorizontalLayout.addWidget(self.graphicsHeight)


        self.graphicsVerticalLayout.addLayout(self.graphicsResolutionHorizontalLayout)

        self.graphicsOtherFormLayout = QFormLayout()
        self.graphicsOtherFormLayout.setObjectName(u"graphicsOtherFormLayout")
        self.graphicsOtherCheckBoxVerticalLayout = QVBoxLayout()
        self.graphicsOtherCheckBoxVerticalLayout.setObjectName(u"graphicsOtherCheckBoxVerticalLayout")
        self.fullScreenCheckBox = QCheckBox(self.graphicsGroupBox)
        self.fullScreenCheckBox.setObjectName(u"fullScreenCheckBox")

        self.graphicsOtherCheckBoxVerticalLayout.addWidget(self.fullScreenCheckBox)

        self.vsyncCheckBox = QCheckBox(self.graphicsGroupBox)
        self.vsyncCheckBox.setObjectName(u"vsyncCheckBox")

        self.graphicsOtherCheckBoxVerticalLayout.addWidget(self.vsyncCheckBox)

        self.showFPSCheckBox = QCheckBox(self.graphicsGroupBox)
        self.showFPSCheckBox.setObjectName(u"showFPSCheckBox")

        self.graphicsOtherCheckBoxVerticalLayout.addWidget(self.showFPSCheckBox)


        self.graphicsOtherFormLayout.setLayout(0, QFormLayout.LabelRole, self.graphicsOtherCheckBoxVerticalLayout)

        self.graphicsOtherSpinBoxVerticalLayout = QVBoxLayout()
        self.graphicsOtherSpinBoxVerticalLayout.setObjectName(u"graphicsOtherSpinBoxVerticalLayout")
        self.MSAAFormLayout = QFormLayout()
        self.MSAAFormLayout.setObjectName(u"MSAAFormLayout")
        self.MSAALabel = QLabel(self.graphicsGroupBox)
        self.MSAALabel.setObjectName(u"MSAALabel")

        self.MSAAFormLayout.setWidget(0, QFormLayout.LabelRole, self.MSAALabel)

        self.MSAASpinBox = QSpinBox(self.graphicsGroupBox)
        self.MSAASpinBox.setObjectName(u"MSAASpinBox")
        self.MSAASpinBox.setMinimum(0)
        self.MSAASpinBox.setMaximum(16)

        self.MSAAFormLayout.setWidget(0, QFormLayout.FieldRole, self.MSAASpinBox)


        self.graphicsOtherSpinBoxVerticalLayout.addLayout(self.MSAAFormLayout)

        self.FPSCapFormLayout = QFormLayout()
        self.FPSCapFormLayout.setObjectName(u"FPSCapFormLayout")
        self.FPSCapLabel = QLabel(self.graphicsGroupBox)
        self.FPSCapLabel.setObjectName(u"FPSCapLabel")

        self.FPSCapFormLayout.setWidget(0, QFormLayout.LabelRole, self.FPSCapLabel)

        self.FPSCapSpinBox = QSpinBox(self.graphicsGroupBox)
        self.FPSCapSpinBox.setObjectName(u"FPSCapSpinBox")
        self.FPSCapSpinBox.setMinimum(0)
        self.FPSCapSpinBox.setMaximum(10000)

        self.FPSCapFormLayout.setWidget(0, QFormLayout.FieldRole, self.FPSCapSpinBox)


        self.graphicsOtherSpinBoxVerticalLayout.addLayout(self.FPSCapFormLayout)


        self.graphicsOtherFormLayout.setLayout(0, QFormLayout.FieldRole, self.graphicsOtherSpinBoxVerticalLayout)


        self.graphicsVerticalLayout.addLayout(self.graphicsOtherFormLayout)

        self.graphicsVerticalLayout.setStretch(0, 2)
        self.graphicsVerticalLayout.setStretch(1, 2)

        self.gridLayout_5.addLayout(self.graphicsVerticalLayout, 0, 0, 1, 1)


        self.generalSettingsGridLayout.addWidget(self.graphicsGroupBox, 0, 1, 1, 1)

        self.generalSettingsGridLayout.setRowStretch(0, 3)
        self.generalSettingsGridLayout.setRowStretch(1, 2)
        self.generalSettingsGridLayout.setColumnStretch(0, 3)
        self.generalSettingsGridLayout.setColumnStretch(1, 2)

        self.gridLayout_3.addLayout(self.generalSettingsGridLayout, 0, 0, 1, 1)

        self.settingsTabWidget.addTab(self.generalSettings, "")
        self.beatmapSettings = QWidget()
        self.beatmapSettings.setObjectName(u"beatmapSettings")
        self.verticalLayout_5 = QVBoxLayout(self.beatmapSettings)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.beatmapBasicGroupBox = QGroupBox(self.beatmapSettings)
        self.beatmapBasicGroupBox.setObjectName(u"beatmapBasicGroupBox")
        self.gridLayout_31 = QGridLayout(self.beatmapBasicGroupBox)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.beatmapBasicGridLayout = QGridLayout()
        self.beatmapBasicGridLayout.setObjectName(u"beatmapBasicGridLayout")
        self.timingRangeGridLayout = QGridLayout()
        self.timingRangeGridLayout.setObjectName(u"timingRangeGridLayout")
        self.timingRangeLabel = QLabel(self.beatmapBasicGroupBox)
        self.timingRangeLabel.setObjectName(u"timingRangeLabel")

        self.timingRangeGridLayout.addWidget(self.timingRangeLabel, 1, 0, 1, 1)

        self.timingRangeSlider = QLabeledRangeSlider(self.beatmapBasicGroupBox)
        self.timingRangeSlider.setObjectName(u"timingRangeSlider")
        self.timingRangeSlider.setOrientation(Qt.Horizontal)

        self.timingRangeGridLayout.addWidget(self.timingRangeSlider, 0, 1, 2, 1)

        self.timingRangeGridLayout.setRowStretch(0, 1)
        self.timingRangeGridLayout.setRowStretch(1, 1)

        self.beatmapBasicGridLayout.addLayout(self.timingRangeGridLayout, 0, 0, 1, 1)

        self.beatmapSpeedPitchHorizontalLayout = QHBoxLayout()
        self.beatmapSpeedPitchHorizontalLayout.setObjectName(u"beatmapSpeedPitchHorizontalLayout")
        self.beatmapSpeedFormLayout = QFormLayout()
        self.beatmapSpeedFormLayout.setObjectName(u"beatmapSpeedFormLayout")
        self.beatmapSpeedLabel = QLabel(self.beatmapBasicGroupBox)
        self.beatmapSpeedLabel.setObjectName(u"beatmapSpeedLabel")

        self.beatmapSpeedFormLayout.setWidget(0, QFormLayout.LabelRole, self.beatmapSpeedLabel)

        self.beatmapSpeedDoubleSpinBox = QDoubleSpinBox(self.beatmapBasicGroupBox)
        self.beatmapSpeedDoubleSpinBox.setObjectName(u"beatmapSpeedDoubleSpinBox")
        self.beatmapSpeedDoubleSpinBox.setDecimals(1)
        self.beatmapSpeedDoubleSpinBox.setMinimum(1.000000000000000)
        self.beatmapSpeedDoubleSpinBox.setMaximum(10.000000000000000)
        self.beatmapSpeedDoubleSpinBox.setSingleStep(0.100000000000000)

        self.beatmapSpeedFormLayout.setWidget(0, QFormLayout.FieldRole, self.beatmapSpeedDoubleSpinBox)


        self.beatmapSpeedPitchHorizontalLayout.addLayout(self.beatmapSpeedFormLayout)

        self.beatmapPitchFormLayout = QFormLayout()
        self.beatmapPitchFormLayout.setObjectName(u"beatmapPitchFormLayout")
        self.beatmapPitchDoubleSpinBox = QDoubleSpinBox(self.beatmapBasicGroupBox)
        self.beatmapPitchDoubleSpinBox.setObjectName(u"beatmapPitchDoubleSpinBox")
        self.beatmapPitchDoubleSpinBox.setDecimals(1)
        self.beatmapPitchDoubleSpinBox.setMinimum(0.000000000000000)
        self.beatmapPitchDoubleSpinBox.setMaximum(5.900000000000000)
        self.beatmapPitchDoubleSpinBox.setSingleStep(0.100000000000000)
        self.beatmapPitchDoubleSpinBox.setStepType(QAbstractSpinBox.DefaultStepType)

        self.beatmapPitchFormLayout.setWidget(0, QFormLayout.FieldRole, self.beatmapPitchDoubleSpinBox)

        self.beatmapPitchLabel = QLabel(self.beatmapBasicGroupBox)
        self.beatmapPitchLabel.setObjectName(u"beatmapPitchLabel")

        self.beatmapPitchFormLayout.setWidget(0, QFormLayout.LabelRole, self.beatmapPitchLabel)


        self.beatmapSpeedPitchHorizontalLayout.addLayout(self.beatmapPitchFormLayout)


        self.beatmapBasicGridLayout.addLayout(self.beatmapSpeedPitchHorizontalLayout, 1, 0, 1, 1)


        self.gridLayout_31.addLayout(self.beatmapBasicGridLayout, 0, 0, 1, 1)

        self.specialGroupBox = QGroupBox(self.beatmapBasicGroupBox)
        self.specialGroupBox.setObjectName(u"specialGroupBox")
        self.gridLayout_30 = QGridLayout(self.specialGroupBox)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.cursorsInMirrorCollageFormLayout = QFormLayout()
        self.cursorsInMirrorCollageFormLayout.setObjectName(u"cursorsInMirrorCollageFormLayout")
        self.cursorsInMirrorCollageCheckBox = QCheckBox(self.specialGroupBox)
        self.cursorsInMirrorCollageCheckBox.setObjectName(u"cursorsInMirrorCollageCheckBox")

        self.cursorsInMirrorCollageFormLayout.setWidget(0, QFormLayout.LabelRole, self.cursorsInMirrorCollageCheckBox)

        self.cursorsInMirrorCollageSpinBox = QSpinBox(self.specialGroupBox)
        self.cursorsInMirrorCollageSpinBox.setObjectName(u"cursorsInMirrorCollageSpinBox")
        self.cursorsInMirrorCollageSpinBox.setEnabled(False)
        self.cursorsInMirrorCollageSpinBox.setMinimum(1)
        self.cursorsInMirrorCollageSpinBox.setMaximum(1000)

        self.cursorsInMirrorCollageFormLayout.setWidget(0, QFormLayout.FieldRole, self.cursorsInMirrorCollageSpinBox)


        self.gridLayout_30.addLayout(self.cursorsInMirrorCollageFormLayout, 0, 0, 1, 1)

        self.cursorsInTagModeFormLayout = QFormLayout()
        self.cursorsInTagModeFormLayout.setObjectName(u"cursorsInTagModeFormLayout")
        self.cursorsInTagModeCheckBox = QCheckBox(self.specialGroupBox)
        self.cursorsInTagModeCheckBox.setObjectName(u"cursorsInTagModeCheckBox")

        self.cursorsInTagModeFormLayout.setWidget(0, QFormLayout.LabelRole, self.cursorsInTagModeCheckBox)

        self.cursorsInTagModeSpinBox = QSpinBox(self.specialGroupBox)
        self.cursorsInTagModeSpinBox.setObjectName(u"cursorsInTagModeSpinBox")
        self.cursorsInTagModeSpinBox.setEnabled(False)
        self.cursorsInTagModeSpinBox.setMinimum(1)

        self.cursorsInTagModeFormLayout.setWidget(0, QFormLayout.FieldRole, self.cursorsInTagModeSpinBox)


        self.gridLayout_30.addLayout(self.cursorsInTagModeFormLayout, 1, 0, 1, 1)


        self.gridLayout_31.addWidget(self.specialGroupBox, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.beatmapBasicGroupBox)

        self.beatmapCustomizeGroupBox = QGroupBox(self.beatmapSettings)
        self.beatmapCustomizeGroupBox.setObjectName(u"beatmapCustomizeGroupBox")
        self.gridLayout_27 = QGridLayout(self.beatmapCustomizeGroupBox)
        self.gridLayout_27.setSpacing(6)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(-1, 4, -1, 4)
        self.beatmapCustomizeGridLayout = QGridLayout()
        self.beatmapCustomizeGridLayout.setObjectName(u"beatmapCustomizeGridLayout")
        self.customizeBeatmapAttributesCheckBox = QCheckBox(self.beatmapCustomizeGroupBox)
        self.customizeBeatmapAttributesCheckBox.setObjectName(u"customizeBeatmapAttributesCheckBox")

        self.beatmapCustomizeGridLayout.addWidget(self.customizeBeatmapAttributesCheckBox, 0, 0, 1, 1)

        self.beatmapAttributesGroupBox = QGroupBox(self.beatmapCustomizeGroupBox)
        self.beatmapAttributesGroupBox.setObjectName(u"beatmapAttributesGroupBox")
        self.beatmapAttributesGroupBox.setEnabled(False)
        self.verticalLayout_4 = QVBoxLayout(self.beatmapAttributesGroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.beatmapAttributesVerticalLayout = QVBoxLayout()
        self.beatmapAttributesVerticalLayout.setObjectName(u"beatmapAttributesVerticalLayout")
        self.CSFormLayout = QFormLayout()
        self.CSFormLayout.setObjectName(u"CSFormLayout")
        self.CSLabel = QLabel(self.beatmapAttributesGroupBox)
        self.CSLabel.setObjectName(u"CSLabel")

        self.CSFormLayout.setWidget(0, QFormLayout.LabelRole, self.CSLabel)

        self.CSHorizontalSlider = QLabeledDoubleSlider(self.beatmapAttributesGroupBox)
        self.CSHorizontalSlider.setObjectName(u"CSHorizontalSlider")
        self.CSHorizontalSlider.setMaximum(12)
        self.CSHorizontalSlider.setOrientation(Qt.Horizontal)

        self.CSFormLayout.setWidget(0, QFormLayout.FieldRole, self.CSHorizontalSlider)


        self.beatmapAttributesVerticalLayout.addLayout(self.CSFormLayout)

        self.ARFormLayout = QFormLayout()
        self.ARFormLayout.setObjectName(u"ARFormLayout")
        self.ARLabel = QLabel(self.beatmapAttributesGroupBox)
        self.ARLabel.setObjectName(u"ARLabel")

        self.ARFormLayout.setWidget(0, QFormLayout.LabelRole, self.ARLabel)

        self.ARHorizontalSlider = QLabeledDoubleSlider(self.beatmapAttributesGroupBox)
        self.ARHorizontalSlider.setObjectName(u"ARHorizontalSlider")
        self.ARHorizontalSlider.setMaximum(12)
        self.ARHorizontalSlider.setOrientation(Qt.Horizontal)

        self.ARFormLayout.setWidget(0, QFormLayout.FieldRole, self.ARHorizontalSlider)


        self.beatmapAttributesVerticalLayout.addLayout(self.ARFormLayout)

        self.ODFormLayout = QFormLayout()
        self.ODFormLayout.setObjectName(u"ODFormLayout")
        self.ODLabel = QLabel(self.beatmapAttributesGroupBox)
        self.ODLabel.setObjectName(u"ODLabel")

        self.ODFormLayout.setWidget(0, QFormLayout.LabelRole, self.ODLabel)

        self.ODHorizontalSlider = QLabeledDoubleSlider(self.beatmapAttributesGroupBox)
        self.ODHorizontalSlider.setObjectName(u"ODHorizontalSlider")
        self.ODHorizontalSlider.setMaximum(12)
        self.ODHorizontalSlider.setOrientation(Qt.Horizontal)

        self.ODFormLayout.setWidget(0, QFormLayout.FieldRole, self.ODHorizontalSlider)


        self.beatmapAttributesVerticalLayout.addLayout(self.ODFormLayout)

        self.HPFormLayout = QFormLayout()
        self.HPFormLayout.setObjectName(u"HPFormLayout")
        self.HPLabel = QLabel(self.beatmapAttributesGroupBox)
        self.HPLabel.setObjectName(u"HPLabel")

        self.HPFormLayout.setWidget(0, QFormLayout.LabelRole, self.HPLabel)

        self.HPHorizontalSlider = QLabeledDoubleSlider(self.beatmapAttributesGroupBox)
        self.HPHorizontalSlider.setObjectName(u"HPHorizontalSlider")
        self.HPHorizontalSlider.setMaximum(12)
        self.HPHorizontalSlider.setOrientation(Qt.Horizontal)

        self.HPFormLayout.setWidget(0, QFormLayout.FieldRole, self.HPHorizontalSlider)


        self.beatmapAttributesVerticalLayout.addLayout(self.HPFormLayout)


        self.verticalLayout_4.addLayout(self.beatmapAttributesVerticalLayout)


        self.beatmapCustomizeGridLayout.addWidget(self.beatmapAttributesGroupBox, 0, 1, 2, 1)

        self.beatmapModsGroupBox = QGroupBox(self.beatmapCustomizeGroupBox)
        self.beatmapModsGroupBox.setObjectName(u"beatmapModsGroupBox")
        self.gridLayout_29 = QGridLayout(self.beatmapModsGroupBox)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.beatmapModsGridLayout = QGridLayout()
        self.beatmapModsGridLayout.setObjectName(u"beatmapModsGridLayout")
        self.SDPFCheckBox = QCheckBox(self.beatmapModsGroupBox)
        self.SDPFCheckBox.setObjectName(u"SDPFCheckBox")
        self.SDPFCheckBox.setText(u"SD/PF")
        self.SDPFCheckBox.setChecked(False)
        self.SDPFCheckBox.setTristate(True)

        self.beatmapModsGridLayout.addWidget(self.SDPFCheckBox, 0, 0, 1, 1)

        self.NFCheckBox = QCheckBox(self.beatmapModsGroupBox)
        self.NFCheckBox.setObjectName(u"NFCheckBox")
        self.NFCheckBox.setText(u"NF")
        self.NFCheckBox.setChecked(False)
        self.NFCheckBox.setTristate(False)

        self.beatmapModsGridLayout.addWidget(self.NFCheckBox, 0, 1, 1, 1)

        self.HDCheckBox = QCheckBox(self.beatmapModsGroupBox)
        self.HDCheckBox.setObjectName(u"HDCheckBox")
        self.HDCheckBox.setText(u"HD")
        self.HDCheckBox.setChecked(False)
        self.HDCheckBox.setTristate(False)

        self.beatmapModsGridLayout.addWidget(self.HDCheckBox, 1, 0, 1, 1)

        self.FLCheckBox = QCheckBox(self.beatmapModsGroupBox)
        self.FLCheckBox.setObjectName(u"FLCheckBox")
        self.FLCheckBox.setText(u"FL")
        self.FLCheckBox.setChecked(False)
        self.FLCheckBox.setTristate(False)

        self.beatmapModsGridLayout.addWidget(self.FLCheckBox, 1, 1, 1, 1)

        self.DTNCCheckBox = QCheckBox(self.beatmapModsGroupBox)
        self.DTNCCheckBox.setObjectName(u"DTNCCheckBox")
        self.DTNCCheckBox.setText(u"DT/NC")
        self.DTNCCheckBox.setChecked(False)
        self.DTNCCheckBox.setTristate(True)

        self.beatmapModsGridLayout.addWidget(self.DTNCCheckBox, 2, 0, 1, 1)

        self.HTCheckBox = QCheckBox(self.beatmapModsGroupBox)
        self.HTCheckBox.setObjectName(u"HTCheckBox")
        self.HTCheckBox.setText(u"HT")
        self.HTCheckBox.setChecked(False)
        self.HTCheckBox.setTristate(False)

        self.beatmapModsGridLayout.addWidget(self.HTCheckBox, 2, 1, 1, 1)

        self.EZHRCheckBox = QCheckBox(self.beatmapModsGroupBox)
        self.EZHRCheckBox.setObjectName(u"EZHRCheckBox")
        self.EZHRCheckBox.setText(u"EZ/HR")
        self.EZHRCheckBox.setChecked(False)
        self.EZHRCheckBox.setTristate(True)

        self.beatmapModsGridLayout.addWidget(self.EZHRCheckBox, 3, 0, 1, 1)


        self.gridLayout_29.addLayout(self.beatmapModsGridLayout, 0, 0, 1, 1)


        self.beatmapCustomizeGridLayout.addWidget(self.beatmapModsGroupBox, 1, 0, 1, 1)


        self.gridLayout_27.addLayout(self.beatmapCustomizeGridLayout, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.beatmapCustomizeGroupBox)

        self.settingsTabWidget.addTab(self.beatmapSettings, "")
        self.knockoutSettings = QWidget()
        self.knockoutSettings.setObjectName(u"knockoutSettings")
        self.gridLayout_34 = QGridLayout(self.knockoutSettings)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.knockoutGeneralGroupBox = QGroupBox(self.knockoutSettings)
        self.knockoutGeneralGroupBox.setObjectName(u"knockoutGeneralGroupBox")
        self.gridLayout_35 = QGridLayout(self.knockoutGeneralGroupBox)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.knockoutModeFormLayout = QFormLayout()
        self.knockoutModeFormLayout.setObjectName(u"knockoutModeFormLayout")
        self.knockoutModeLabel = QLabel(self.knockoutGeneralGroupBox)
        self.knockoutModeLabel.setObjectName(u"knockoutModeLabel")

        self.knockoutModeFormLayout.setWidget(0, QFormLayout.LabelRole, self.knockoutModeLabel)

        self.knockoutModeComboBox = QComboBox(self.knockoutGeneralGroupBox)
        self.knockoutModeComboBox.addItem("")
        self.knockoutModeComboBox.addItem("")
        self.knockoutModeComboBox.addItem("")
        self.knockoutModeComboBox.addItem("")
        self.knockoutModeComboBox.addItem("")
        self.knockoutModeComboBox.setObjectName(u"knockoutModeComboBox")

        self.knockoutModeFormLayout.setWidget(0, QFormLayout.FieldRole, self.knockoutModeComboBox)


        self.gridLayout_35.addLayout(self.knockoutModeFormLayout, 0, 0, 1, 2)

        self.sortHorizontalLayout = QHBoxLayout()
        self.sortHorizontalLayout.setObjectName(u"sortHorizontalLayout")
        self.sortByFormLayout = QFormLayout()
        self.sortByFormLayout.setObjectName(u"sortByFormLayout")
        self.sortByLabel = QLabel(self.knockoutGeneralGroupBox)
        self.sortByLabel.setObjectName(u"sortByLabel")

        self.sortByFormLayout.setWidget(0, QFormLayout.LabelRole, self.sortByLabel)

        self.sortByComboBox = QComboBox(self.knockoutGeneralGroupBox)
        self.sortByComboBox.addItem(u"Score")
        self.sortByComboBox.addItem(u"PP")
        self.sortByComboBox.setObjectName(u"sortByComboBox")

        self.sortByFormLayout.setWidget(0, QFormLayout.FieldRole, self.sortByComboBox)


        self.sortHorizontalLayout.addLayout(self.sortByFormLayout)

        self.liveSortCheckBox = QCheckBox(self.knockoutGeneralGroupBox)
        self.liveSortCheckBox.setObjectName(u"liveSortCheckBox")

        self.sortHorizontalLayout.addWidget(self.liveSortCheckBox)


        self.gridLayout_35.addLayout(self.sortHorizontalLayout, 2, 0, 1, 2)

        self.knockoutCursorSizeGridLayout = QGridLayout()
        self.knockoutCursorSizeGridLayout.setObjectName(u"knockoutCursorSizeGridLayout")
        self.knockoutCursorSizeLabel = QLabel(self.knockoutGeneralGroupBox)
        self.knockoutCursorSizeLabel.setObjectName(u"knockoutCursorSizeLabel")

        self.knockoutCursorSizeGridLayout.addWidget(self.knockoutCursorSizeLabel, 1, 1, 1, 1)

        self.knockoutCursorSizeSlider = QLabeledDoubleRangeSlider(self.knockoutGeneralGroupBox)
        self.knockoutCursorSizeSlider.setObjectName(u"knockoutCursorSizeSlider")
        self.knockoutCursorSizeSlider.setOrientation(Qt.Horizontal)

        self.knockoutCursorSizeGridLayout.addWidget(self.knockoutCursorSizeSlider, 0, 2, 2, 1)


        self.gridLayout_35.addLayout(self.knockoutCursorSizeGridLayout, 3, 0, 1, 2)

        self.checkBoxHorizontalLayout = QHBoxLayout()
        self.checkBoxHorizontalLayout.setObjectName(u"checkBoxHorizontalLayout")
        self.revivePlayersAtEndCheckBox = QCheckBox(self.knockoutGeneralGroupBox)
        self.revivePlayersAtEndCheckBox.setObjectName(u"revivePlayersAtEndCheckBox")

        self.checkBoxHorizontalLayout.addWidget(self.revivePlayersAtEndCheckBox)

        self.HideOverlayOnBreaksCheckBox = QCheckBox(self.knockoutGeneralGroupBox)
        self.HideOverlayOnBreaksCheckBox.setObjectName(u"HideOverlayOnBreaksCheckBox")

        self.checkBoxHorizontalLayout.addWidget(self.HideOverlayOnBreaksCheckBox)


        self.gridLayout_35.addLayout(self.checkBoxHorizontalLayout, 4, 0, 1, 2)

        self.maxPlayersFormLayout = QFormLayout()
        self.maxPlayersFormLayout.setObjectName(u"maxPlayersFormLayout")
        self.maxPlayersLabel = QLabel(self.knockoutGeneralGroupBox)
        self.maxPlayersLabel.setObjectName(u"maxPlayersLabel")

        self.maxPlayersFormLayout.setWidget(0, QFormLayout.LabelRole, self.maxPlayersLabel)

        self.maxPlayersSpinBox = QSpinBox(self.knockoutGeneralGroupBox)
        self.maxPlayersSpinBox.setObjectName(u"maxPlayersSpinBox")
        self.maxPlayersSpinBox.setMinimum(1)
        self.maxPlayersSpinBox.setMaximum(50)
        self.maxPlayersSpinBox.setSingleStep(1)
        self.maxPlayersSpinBox.setValue(50)

        self.maxPlayersFormLayout.setWidget(0, QFormLayout.FieldRole, self.maxPlayersSpinBox)


        self.gridLayout_35.addLayout(self.maxPlayersFormLayout, 5, 0, 1, 1)

        self.danserNameFormLayout = QFormLayout()
        self.danserNameFormLayout.setObjectName(u"danserNameFormLayout")
        self.addDanserCheckBox = QCheckBox(self.knockoutGeneralGroupBox)
        self.addDanserCheckBox.setObjectName(u"addDanserCheckBox")

        self.danserNameFormLayout.setWidget(0, QFormLayout.LabelRole, self.addDanserCheckBox)

        self.danserNameLineEdit = QLineEdit(self.knockoutGeneralGroupBox)
        self.danserNameLineEdit.setObjectName(u"danserNameLineEdit")

        self.danserNameFormLayout.setWidget(0, QFormLayout.FieldRole, self.danserNameLineEdit)


        self.gridLayout_35.addLayout(self.danserNameFormLayout, 6, 0, 1, 2)

        self.openKnockoutReplaysFolderPushButton = QPushButton(self.knockoutGeneralGroupBox)
        self.openKnockoutReplaysFolderPushButton.setObjectName(u"openKnockoutReplaysFolderPushButton")

        self.gridLayout_35.addWidget(self.openKnockoutReplaysFolderPushButton, 7, 0, 1, 2)

        self.spinBoxHorizontalLayout = QHBoxLayout()
        self.spinBoxHorizontalLayout.setObjectName(u"spinBoxHorizontalLayout")
        self.graceEndTimeHorizontalLayout = QHBoxLayout()
        self.graceEndTimeHorizontalLayout.setObjectName(u"graceEndTimeHorizontalLayout")
        self.graceEndTimeLabel = QLabel(self.knockoutGeneralGroupBox)
        self.graceEndTimeLabel.setObjectName(u"graceEndTimeLabel")

        self.graceEndTimeHorizontalLayout.addWidget(self.graceEndTimeLabel)

        self.graceEndTimeDoubleSpinBox = QDoubleSpinBox(self.knockoutGeneralGroupBox)
        self.graceEndTimeDoubleSpinBox.setObjectName(u"graceEndTimeDoubleSpinBox")
        self.graceEndTimeDoubleSpinBox.setDecimals(1)
        self.graceEndTimeDoubleSpinBox.setMinimum(-100.000000000000000)
        self.graceEndTimeDoubleSpinBox.setSingleStep(1.000000000000000)
        self.graceEndTimeDoubleSpinBox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.graceEndTimeDoubleSpinBox.setValue(-10.000000000000000)

        self.graceEndTimeHorizontalLayout.addWidget(self.graceEndTimeDoubleSpinBox)


        self.spinBoxHorizontalLayout.addLayout(self.graceEndTimeHorizontalLayout)

        self.bubbleMinimumComboHorizontalLayout = QHBoxLayout()
        self.bubbleMinimumComboHorizontalLayout.setObjectName(u"bubbleMinimumComboHorizontalLayout")
        self.bubbleMinimumComboLabel = QLabel(self.knockoutGeneralGroupBox)
        self.bubbleMinimumComboLabel.setObjectName(u"bubbleMinimumComboLabel")

        self.bubbleMinimumComboHorizontalLayout.addWidget(self.bubbleMinimumComboLabel)

        self.bubbleMinimumComboSpinBox = QSpinBox(self.knockoutGeneralGroupBox)
        self.bubbleMinimumComboSpinBox.setObjectName(u"bubbleMinimumComboSpinBox")
        self.bubbleMinimumComboSpinBox.setMaximum(10000)

        self.bubbleMinimumComboHorizontalLayout.addWidget(self.bubbleMinimumComboSpinBox)


        self.spinBoxHorizontalLayout.addLayout(self.bubbleMinimumComboHorizontalLayout)


        self.gridLayout_35.addLayout(self.spinBoxHorizontalLayout, 1, 0, 1, 2)


        self.gridLayout_34.addWidget(self.knockoutGeneralGroupBox, 0, 0, 2, 1)

        self.excludeModsGroupBox = QGroupBox(self.knockoutSettings)
        self.excludeModsGroupBox.setObjectName(u"excludeModsGroupBox")
        self.gridLayout_33 = QGridLayout(self.excludeModsGroupBox)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.excludeModsGridLayout = QGridLayout()
        self.excludeModsGridLayout.setObjectName(u"excludeModsGridLayout")
        self.excludeModsHDCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsHDCheckBox.setObjectName(u"excludeModsHDCheckBox")
        self.excludeModsHDCheckBox.setText(u"HD")
        self.excludeModsHDCheckBox.setChecked(False)
        self.excludeModsHDCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsHDCheckBox, 1, 0, 1, 1)

        self.excludeModsEZCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsEZCheckBox.setObjectName(u"excludeModsEZCheckBox")
        self.excludeModsEZCheckBox.setText(u"EZ")
        self.excludeModsEZCheckBox.setChecked(False)
        self.excludeModsEZCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsEZCheckBox, 3, 0, 1, 1)

        self.excludeModsV2CheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsV2CheckBox.setObjectName(u"excludeModsV2CheckBox")
        self.excludeModsV2CheckBox.setText(u"V2")
        self.excludeModsV2CheckBox.setChecked(False)
        self.excludeModsV2CheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsV2CheckBox, 3, 2, 1, 1)

        self.excludeModsHTCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsHTCheckBox.setObjectName(u"excludeModsHTCheckBox")
        self.excludeModsHTCheckBox.setText(u"HT")
        self.excludeModsHTCheckBox.setChecked(False)
        self.excludeModsHTCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsHTCheckBox, 2, 2, 1, 1)

        self.excludeModsPFCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsPFCheckBox.setObjectName(u"excludeModsPFCheckBox")
        self.excludeModsPFCheckBox.setText(u"PF")
        self.excludeModsPFCheckBox.setChecked(False)
        self.excludeModsPFCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsPFCheckBox, 0, 1, 1, 1)

        self.excludeModsNCCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsNCCheckBox.setObjectName(u"excludeModsNCCheckBox")
        self.excludeModsNCCheckBox.setText(u"NC")
        self.excludeModsNCCheckBox.setChecked(False)
        self.excludeModsNCCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsNCCheckBox, 2, 1, 1, 1)

        self.excludeModsRXCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsRXCheckBox.setObjectName(u"excludeModsRXCheckBox")
        self.excludeModsRXCheckBox.setText(u"RX")
        self.excludeModsRXCheckBox.setChecked(False)
        self.excludeModsRXCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsRXCheckBox, 4, 1, 1, 1)

        self.excludeModsSDCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsSDCheckBox.setObjectName(u"excludeModsSDCheckBox")
        self.excludeModsSDCheckBox.setText(u"SD")
        self.excludeModsSDCheckBox.setChecked(False)
        self.excludeModsSDCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsSDCheckBox, 0, 0, 1, 1)

        self.excludeModsDTCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsDTCheckBox.setObjectName(u"excludeModsDTCheckBox")
        self.excludeModsDTCheckBox.setText(u"DT")
        self.excludeModsDTCheckBox.setChecked(False)
        self.excludeModsDTCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsDTCheckBox, 2, 0, 1, 1)

        self.excludeModsATCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsATCheckBox.setObjectName(u"excludeModsATCheckBox")
        self.excludeModsATCheckBox.setText(u"AT")
        self.excludeModsATCheckBox.setChecked(False)
        self.excludeModsATCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsATCheckBox, 4, 0, 1, 1)

        self.excludeModsFLCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsFLCheckBox.setObjectName(u"excludeModsFLCheckBox")
        self.excludeModsFLCheckBox.setText(u"FL")
        self.excludeModsFLCheckBox.setChecked(False)
        self.excludeModsFLCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsFLCheckBox, 1, 1, 1, 1)

        self.excludeModsHRCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsHRCheckBox.setObjectName(u"excludeModsHRCheckBox")
        self.excludeModsHRCheckBox.setText(u"HR")
        self.excludeModsHRCheckBox.setChecked(False)
        self.excludeModsHRCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsHRCheckBox, 3, 1, 1, 1)

        self.excludeModsAPCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsAPCheckBox.setObjectName(u"excludeModsAPCheckBox")
        self.excludeModsAPCheckBox.setText(u"AP")
        self.excludeModsAPCheckBox.setChecked(False)
        self.excludeModsAPCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsAPCheckBox, 4, 2, 1, 1)

        self.excludeModsNFCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsNFCheckBox.setObjectName(u"excludeModsNFCheckBox")
        self.excludeModsNFCheckBox.setText(u"NF")
        self.excludeModsNFCheckBox.setChecked(False)
        self.excludeModsNFCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsNFCheckBox, 0, 2, 1, 1)

        self.excludeModsTDCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsTDCheckBox.setObjectName(u"excludeModsTDCheckBox")
        self.excludeModsTDCheckBox.setText(u"TD")
        self.excludeModsTDCheckBox.setChecked(False)
        self.excludeModsTDCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsTDCheckBox, 5, 0, 1, 1)

        self.excludeModsSOCheckBox = QCheckBox(self.excludeModsGroupBox)
        self.excludeModsSOCheckBox.setObjectName(u"excludeModsSOCheckBox")
        self.excludeModsSOCheckBox.setText(u"SO")
        self.excludeModsSOCheckBox.setChecked(False)
        self.excludeModsSOCheckBox.setTristate(False)

        self.excludeModsGridLayout.addWidget(self.excludeModsSOCheckBox, 5, 1, 1, 1)


        self.gridLayout_33.addLayout(self.excludeModsGridLayout, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.excludeModsGroupBox, 0, 1, 1, 1)

        self.hideModsGroupBox = QGroupBox(self.knockoutSettings)
        self.hideModsGroupBox.setObjectName(u"hideModsGroupBox")
        self.gridLayout_32 = QGridLayout(self.hideModsGroupBox)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.hideModsGridLayout = QGridLayout()
        self.hideModsGridLayout.setObjectName(u"hideModsGridLayout")
        self.hideModsHDCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsHDCheckBox.setObjectName(u"hideModsHDCheckBox")
        self.hideModsHDCheckBox.setText(u"HD")
        self.hideModsHDCheckBox.setChecked(False)
        self.hideModsHDCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsHDCheckBox, 1, 0, 1, 1)

        self.hideModsEZCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsEZCheckBox.setObjectName(u"hideModsEZCheckBox")
        self.hideModsEZCheckBox.setText(u"EZ")
        self.hideModsEZCheckBox.setChecked(False)
        self.hideModsEZCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsEZCheckBox, 3, 0, 1, 1)

        self.hideModsV2CheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsV2CheckBox.setObjectName(u"hideModsV2CheckBox")
        self.hideModsV2CheckBox.setText(u"V2")
        self.hideModsV2CheckBox.setChecked(False)
        self.hideModsV2CheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsV2CheckBox, 3, 2, 1, 1)

        self.hideModsHTCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsHTCheckBox.setObjectName(u"hideModsHTCheckBox")
        self.hideModsHTCheckBox.setText(u"HT")
        self.hideModsHTCheckBox.setChecked(False)
        self.hideModsHTCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsHTCheckBox, 2, 2, 1, 1)

        self.hideModsPFCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsPFCheckBox.setObjectName(u"hideModsPFCheckBox")
        self.hideModsPFCheckBox.setText(u"PF")
        self.hideModsPFCheckBox.setChecked(False)
        self.hideModsPFCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsPFCheckBox, 0, 1, 1, 1)

        self.hideModsNCCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsNCCheckBox.setObjectName(u"hideModsNCCheckBox")
        self.hideModsNCCheckBox.setText(u"NC")
        self.hideModsNCCheckBox.setChecked(False)
        self.hideModsNCCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsNCCheckBox, 2, 1, 1, 1)

        self.hideModsRXCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsRXCheckBox.setObjectName(u"hideModsRXCheckBox")
        self.hideModsRXCheckBox.setText(u"RX")
        self.hideModsRXCheckBox.setChecked(False)
        self.hideModsRXCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsRXCheckBox, 4, 1, 1, 1)

        self.hideModsSDCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsSDCheckBox.setObjectName(u"hideModsSDCheckBox")
        self.hideModsSDCheckBox.setText(u"SD")
        self.hideModsSDCheckBox.setChecked(False)
        self.hideModsSDCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsSDCheckBox, 0, 0, 1, 1)

        self.hideModsDTCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsDTCheckBox.setObjectName(u"hideModsDTCheckBox")
        self.hideModsDTCheckBox.setText(u"DT")
        self.hideModsDTCheckBox.setChecked(False)
        self.hideModsDTCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsDTCheckBox, 2, 0, 1, 1)

        self.hideModsATCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsATCheckBox.setObjectName(u"hideModsATCheckBox")
        self.hideModsATCheckBox.setText(u"AT")
        self.hideModsATCheckBox.setChecked(False)
        self.hideModsATCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsATCheckBox, 4, 0, 1, 1)

        self.hideModsFLCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsFLCheckBox.setObjectName(u"hideModsFLCheckBox")
        self.hideModsFLCheckBox.setText(u"FL")
        self.hideModsFLCheckBox.setChecked(False)
        self.hideModsFLCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsFLCheckBox, 1, 1, 1, 1)

        self.hideModsHRCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsHRCheckBox.setObjectName(u"hideModsHRCheckBox")
        self.hideModsHRCheckBox.setText(u"HR")
        self.hideModsHRCheckBox.setChecked(False)
        self.hideModsHRCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsHRCheckBox, 3, 1, 1, 1)

        self.hideModsAPCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsAPCheckBox.setObjectName(u"hideModsAPCheckBox")
        self.hideModsAPCheckBox.setText(u"AP")
        self.hideModsAPCheckBox.setChecked(False)
        self.hideModsAPCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsAPCheckBox, 4, 2, 1, 1)

        self.hideModsNFCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsNFCheckBox.setObjectName(u"hideModsNFCheckBox")
        self.hideModsNFCheckBox.setText(u"NF")
        self.hideModsNFCheckBox.setChecked(False)
        self.hideModsNFCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsNFCheckBox, 0, 2, 1, 1)

        self.hideModsTDCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsTDCheckBox.setObjectName(u"hideModsTDCheckBox")
        self.hideModsTDCheckBox.setText(u"TD")
        self.hideModsTDCheckBox.setChecked(False)
        self.hideModsTDCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsTDCheckBox, 5, 0, 1, 1)

        self.hideModsSOCheckBox = QCheckBox(self.hideModsGroupBox)
        self.hideModsSOCheckBox.setObjectName(u"hideModsSOCheckBox")
        self.hideModsSOCheckBox.setText(u"SO")
        self.hideModsSOCheckBox.setChecked(False)
        self.hideModsSOCheckBox.setTristate(False)

        self.hideModsGridLayout.addWidget(self.hideModsSOCheckBox, 5, 1, 1, 1)


        self.gridLayout_32.addLayout(self.hideModsGridLayout, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.hideModsGroupBox, 0, 2, 1, 1)

        self.experimentalFeaturesGroupBox = QGroupBox(self.knockoutSettings)
        self.experimentalFeaturesGroupBox.setObjectName(u"experimentalFeaturesGroupBox")
        self.verticalLayout_7 = QVBoxLayout(self.experimentalFeaturesGroupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.modifyOsrMD5CheckBox = QCheckBox(self.experimentalFeaturesGroupBox)
        self.modifyOsrMD5CheckBox.setObjectName(u"modifyOsrMD5CheckBox")

        self.verticalLayout_7.addWidget(self.modifyOsrMD5CheckBox)

        self.addDateAfterPlayerNamecheckBox = QCheckBox(self.experimentalFeaturesGroupBox)
        self.addDateAfterPlayerNamecheckBox.setObjectName(u"addDateAfterPlayerNamecheckBox")

        self.verticalLayout_7.addWidget(self.addDateAfterPlayerNamecheckBox)

        self.dateFormatFormLayout = QFormLayout()
        self.dateFormatFormLayout.setObjectName(u"dateFormatFormLayout")
        self.dateFormatLabel = QLabel(self.experimentalFeaturesGroupBox)
        self.dateFormatLabel.setObjectName(u"dateFormatLabel")

        self.dateFormatFormLayout.setWidget(0, QFormLayout.LabelRole, self.dateFormatLabel)

        self.dateFormatComboBox = QComboBox(self.experimentalFeaturesGroupBox)
        self.dateFormatComboBox.addItem("")
        self.dateFormatComboBox.addItem("")
        self.dateFormatComboBox.addItem("")
        self.dateFormatComboBox.setObjectName(u"dateFormatComboBox")

        self.dateFormatFormLayout.setWidget(0, QFormLayout.FieldRole, self.dateFormatComboBox)


        self.verticalLayout_7.addLayout(self.dateFormatFormLayout)


        self.gridLayout_34.addWidget(self.experimentalFeaturesGroupBox, 1, 1, 1, 2)

        self.settingsTabWidget.addTab(self.knockoutSettings, "")
        self.recordingSettings = QWidget()
        self.recordingSettings.setObjectName(u"recordingSettings")
        self.gridLayout_9 = QGridLayout(self.recordingSettings)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.recordingGroupBox = QGroupBox(self.recordingSettings)
        self.recordingGroupBox.setObjectName(u"recordingGroupBox")
        self.gridLayout_8 = QGridLayout(self.recordingGroupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.recordingGridLayout = QGridLayout()
        self.recordingGridLayout.setObjectName(u"recordingGridLayout")
        self.recordingGeneralVerticalLayout = QVBoxLayout()
        self.recordingGeneralVerticalLayout.setObjectName(u"recordingGeneralVerticalLayout")
        self.recordingResolutionHorizontalLayout = QHBoxLayout()
        self.recordingResolutionHorizontalLayout.setSpacing(6)
        self.recordingResolutionHorizontalLayout.setObjectName(u"recordingResolutionHorizontalLayout")
        self.recordingResolutionLabel = QLabel(self.recordingGroupBox)
        self.recordingResolutionLabel.setObjectName(u"recordingResolutionLabel")

        self.recordingResolutionHorizontalLayout.addWidget(self.recordingResolutionLabel)

        self.recordingWidth = QLineEdit(self.recordingGroupBox)
        self.recordingWidth.setObjectName(u"recordingWidth")

        self.recordingResolutionHorizontalLayout.addWidget(self.recordingWidth)

        self.recordingResolutionMiddleX = QLabel(self.recordingGroupBox)
        self.recordingResolutionMiddleX.setObjectName(u"recordingResolutionMiddleX")
        self.recordingResolutionMiddleX.setText(u"x")

        self.recordingResolutionHorizontalLayout.addWidget(self.recordingResolutionMiddleX)

        self.recordingHeight = QLineEdit(self.recordingGroupBox)
        self.recordingHeight.setObjectName(u"recordingHeight")

        self.recordingResolutionHorizontalLayout.addWidget(self.recordingHeight)


        self.recordingGeneralVerticalLayout.addLayout(self.recordingResolutionHorizontalLayout)

        self.recordingFPSHorizontalLayout = QHBoxLayout()
        self.recordingFPSHorizontalLayout.setObjectName(u"recordingFPSHorizontalLayout")
        self.recordingFPSFormLayout = QFormLayout()
        self.recordingFPSFormLayout.setObjectName(u"recordingFPSFormLayout")
        self.recordingFPSLabel = QLabel(self.recordingGroupBox)
        self.recordingFPSLabel.setObjectName(u"recordingFPSLabel")

        self.recordingFPSFormLayout.setWidget(0, QFormLayout.LabelRole, self.recordingFPSLabel)

        self.recordingFPSSpinBox = QSpinBox(self.recordingGroupBox)
        self.recordingFPSSpinBox.setObjectName(u"recordingFPSSpinBox")
        self.recordingFPSSpinBox.setMinimum(0)
        self.recordingFPSSpinBox.setMaximum(10000)

        self.recordingFPSFormLayout.setWidget(0, QFormLayout.FieldRole, self.recordingFPSSpinBox)


        self.recordingFPSHorizontalLayout.addLayout(self.recordingFPSFormLayout)

        self.motionBlurcheckBox = QCheckBox(self.recordingGroupBox)
        self.motionBlurcheckBox.setObjectName(u"motionBlurcheckBox")

        self.recordingFPSHorizontalLayout.addWidget(self.motionBlurcheckBox)


        self.recordingGeneralVerticalLayout.addLayout(self.recordingFPSHorizontalLayout)

        self.recordingEncoderFormLayout = QFormLayout()
        self.recordingEncoderFormLayout.setObjectName(u"recordingEncoderFormLayout")
        self.recordingEncoderLabel = QLabel(self.recordingGroupBox)
        self.recordingEncoderLabel.setObjectName(u"recordingEncoderLabel")

        self.recordingEncoderFormLayout.setWidget(0, QFormLayout.LabelRole, self.recordingEncoderLabel)

        self.recordingEncoderComboBox = QComboBox(self.recordingGroupBox)
        self.recordingEncoderComboBox.addItem("")
        self.recordingEncoderComboBox.addItem("")
        self.recordingEncoderComboBox.addItem("")
        self.recordingEncoderComboBox.addItem("")
        self.recordingEncoderComboBox.addItem("")
        self.recordingEncoderComboBox.setObjectName(u"recordingEncoderComboBox")

        self.recordingEncoderFormLayout.setWidget(0, QFormLayout.FieldRole, self.recordingEncoderComboBox)


        self.recordingGeneralVerticalLayout.addLayout(self.recordingEncoderFormLayout)

        self.outputPathVerticalLayout = QVBoxLayout()
        self.outputPathVerticalLayout.setObjectName(u"outputPathVerticalLayout")
        self.outputPathLabel = QLabel(self.recordingGroupBox)
        self.outputPathLabel.setObjectName(u"outputPathLabel")

        self.outputPathVerticalLayout.addWidget(self.outputPathLabel)

        self.outputPathLineEdit = QClickedLineEdit(self.recordingGroupBox)
        self.outputPathLineEdit.setObjectName(u"outputPathLineEdit")
        self.outputPathLineEdit.setReadOnly(True)

        self.outputPathVerticalLayout.addWidget(self.outputPathLineEdit)


        self.recordingGeneralVerticalLayout.addLayout(self.outputPathVerticalLayout)

        self.outputNameVerticalLayout = QVBoxLayout()
        self.outputNameVerticalLayout.setObjectName(u"outputNameVerticalLayout")
        self.outputNameLabel = QLabel(self.recordingGroupBox)
        self.outputNameLabel.setObjectName(u"outputNameLabel")

        self.outputNameVerticalLayout.addWidget(self.outputNameLabel)

        self.outputNameLineEdit = QLineEdit(self.recordingGroupBox)
        self.outputNameLineEdit.setObjectName(u"outputNameLineEdit")

        self.outputNameVerticalLayout.addWidget(self.outputNameLineEdit)


        self.recordingGeneralVerticalLayout.addLayout(self.outputNameVerticalLayout)

        self.localAudioOffsetVerticalLayout = QVBoxLayout()
        self.localAudioOffsetVerticalLayout.setObjectName(u"localAudioOffsetVerticalLayout")
        self.localAudioOffsetLabel = QLabel(self.recordingGroupBox)
        self.localAudioOffsetLabel.setObjectName(u"localAudioOffsetLabel")

        self.localAudioOffsetVerticalLayout.addWidget(self.localAudioOffsetLabel)

        self.localAudioOffsetSlider = QLabeledSlider(self.recordingGroupBox)
        self.localAudioOffsetSlider.setObjectName(u"localAudioOffsetSlider")
        self.localAudioOffsetSlider.setMinimum(-100)
        self.localAudioOffsetSlider.setMaximum(100)
        self.localAudioOffsetSlider.setOrientation(Qt.Horizontal)

        self.localAudioOffsetVerticalLayout.addWidget(self.localAudioOffsetSlider)


        self.recordingGeneralVerticalLayout.addLayout(self.localAudioOffsetVerticalLayout)


        self.recordingGridLayout.addLayout(self.recordingGeneralVerticalLayout, 0, 0, 1, 1)

        self.empty_widget_1 = QWidget(self.recordingGroupBox)
        self.empty_widget_1.setObjectName(u"empty_widget_1")

        self.recordingGridLayout.addWidget(self.empty_widget_1, 1, 0, 1, 1)

        self.encoderConfigGroupBox = QGroupBox(self.recordingGroupBox)
        self.encoderConfigGroupBox.setObjectName(u"encoderConfigGroupBox")
        self.formLayout_17 = QFormLayout(self.encoderConfigGroupBox)
        self.formLayout_17.setObjectName(u"formLayout_17")
        self.encoderConfigVerticalLayout = QVBoxLayout()
        self.encoderConfigVerticalLayout.setObjectName(u"encoderConfigVerticalLayout")
        self.videoCodecCustomizeFormLayout = QFormLayout()
        self.videoCodecCustomizeFormLayout.setObjectName(u"videoCodecCustomizeFormLayout")
        self.videoCodecCustomizeLabel = QLabel(self.encoderConfigGroupBox)
        self.videoCodecCustomizeLabel.setObjectName(u"videoCodecCustomizeLabel")

        self.videoCodecCustomizeFormLayout.setWidget(0, QFormLayout.LabelRole, self.videoCodecCustomizeLabel)

        self.videoCodecCustomizeLineEdit = QLineEdit(self.encoderConfigGroupBox)
        self.videoCodecCustomizeLineEdit.setObjectName(u"videoCodecCustomizeLineEdit")
        self.videoCodecCustomizeLineEdit.setEchoMode(QLineEdit.Normal)
        self.videoCodecCustomizeLineEdit.setClearButtonEnabled(False)

        self.videoCodecCustomizeFormLayout.setWidget(0, QFormLayout.FieldRole, self.videoCodecCustomizeLineEdit)


        self.encoderConfigVerticalLayout.addLayout(self.videoCodecCustomizeFormLayout)

        self.encoderOptionCustomizeVerticalLayout = QVBoxLayout()
        self.encoderOptionCustomizeVerticalLayout.setObjectName(u"encoderOptionCustomizeVerticalLayout")
        self.encoderOptionCustomizeLabel = QLabel(self.encoderConfigGroupBox)
        self.encoderOptionCustomizeLabel.setObjectName(u"encoderOptionCustomizeLabel")

        self.encoderOptionCustomizeVerticalLayout.addWidget(self.encoderOptionCustomizeLabel)

        self.encoderOptionCustomizeLineEdit = QLineEdit(self.encoderConfigGroupBox)
        self.encoderOptionCustomizeLineEdit.setObjectName(u"encoderOptionCustomizeLineEdit")

        self.encoderOptionCustomizeVerticalLayout.addWidget(self.encoderOptionCustomizeLineEdit)


        self.encoderConfigVerticalLayout.addLayout(self.encoderOptionCustomizeVerticalLayout)

        self.presetCustomizeFormLayout = QFormLayout()
        self.presetCustomizeFormLayout.setObjectName(u"presetCustomizeFormLayout")
        self.presetCustomizeLabel = QLabel(self.encoderConfigGroupBox)
        self.presetCustomizeLabel.setObjectName(u"presetCustomizeLabel")

        self.presetCustomizeFormLayout.setWidget(0, QFormLayout.LabelRole, self.presetCustomizeLabel)

        self.presetCustomizeLineEdit = QLineEdit(self.encoderConfigGroupBox)
        self.presetCustomizeLineEdit.setObjectName(u"presetCustomizeLineEdit")

        self.presetCustomizeFormLayout.setWidget(0, QFormLayout.FieldRole, self.presetCustomizeLineEdit)


        self.encoderConfigVerticalLayout.addLayout(self.presetCustomizeFormLayout)

        self.audioCodecFormLayout = QFormLayout()
        self.audioCodecFormLayout.setObjectName(u"audioCodecFormLayout")
        self.audioCodecCustomizeLabel = QLabel(self.encoderConfigGroupBox)
        self.audioCodecCustomizeLabel.setObjectName(u"audioCodecCustomizeLabel")

        self.audioCodecFormLayout.setWidget(0, QFormLayout.LabelRole, self.audioCodecCustomizeLabel)

        self.audioCodecCustomizeLineEdit = QLineEdit(self.encoderConfigGroupBox)
        self.audioCodecCustomizeLineEdit.setObjectName(u"audioCodecCustomizeLineEdit")

        self.audioCodecFormLayout.setWidget(0, QFormLayout.FieldRole, self.audioCodecCustomizeLineEdit)


        self.encoderConfigVerticalLayout.addLayout(self.audioCodecFormLayout)

        self.audioOptionCustomizeVerticalLayout = QVBoxLayout()
        self.audioOptionCustomizeVerticalLayout.setObjectName(u"audioOptionCustomizeVerticalLayout")
        self.audioOptionCustomizeLabel = QLabel(self.encoderConfigGroupBox)
        self.audioOptionCustomizeLabel.setObjectName(u"audioOptionCustomizeLabel")

        self.audioOptionCustomizeVerticalLayout.addWidget(self.audioOptionCustomizeLabel)

        self.audioOptionCustomizeLineEdit = QLineEdit(self.encoderConfigGroupBox)
        self.audioOptionCustomizeLineEdit.setObjectName(u"audioOptionCustomizeLineEdit")

        self.audioOptionCustomizeVerticalLayout.addWidget(self.audioOptionCustomizeLineEdit)


        self.encoderConfigVerticalLayout.addLayout(self.audioOptionCustomizeVerticalLayout)


        self.formLayout_17.setLayout(0, QFormLayout.SpanningRole, self.encoderConfigVerticalLayout)


        self.recordingGridLayout.addWidget(self.encoderConfigGroupBox, 0, 1, 2, 1)

        self.recordingGridLayout.setColumnStretch(0, 1)
        self.recordingGridLayout.setColumnStretch(1, 1)

        self.gridLayout_8.addLayout(self.recordingGridLayout, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.recordingGroupBox, 0, 0, 1, 1)

        self.settingsTabWidget.addTab(self.recordingSettings, "")
        self.gameplaySettings = QWidget()
        self.gameplaySettings.setObjectName(u"gameplaySettings")
        self.gridLayout_12 = QGridLayout(self.gameplaySettings)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gameplaySettingsVerticalLayout = QVBoxLayout()
        self.gameplaySettingsVerticalLayout.setObjectName(u"gameplaySettingsVerticalLayout")
        self.gameplaySettingsGridLayout = QGridLayout()
        self.gameplaySettingsGridLayout.setSpacing(6)
        self.gameplaySettingsGridLayout.setObjectName(u"gameplaySettingsGridLayout")
        self.boundariesGroupBox = QGroupBox(self.gameplaySettings)
        self.boundariesGroupBox.setObjectName(u"boundariesGroupBox")
        self.gridLayout_23 = QGridLayout(self.boundariesGroupBox)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(-1, 4, -1, 0)
        self.boundariesShowCheckBox = QCheckBox(self.boundariesGroupBox)
        self.boundariesShowCheckBox.setObjectName(u"boundariesShowCheckBox")

        self.gridLayout_23.addWidget(self.boundariesShowCheckBox, 0, 0, 1, 1)


        self.gameplaySettingsGridLayout.addWidget(self.boundariesGroupBox, 0, 0, 1, 1)

        self.scoreGroupBox = QGroupBox(self.gameplaySettings)
        self.scoreGroupBox.setObjectName(u"scoreGroupBox")
        self.gridLayout_11 = QGridLayout(self.scoreGroupBox)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 4, -1, 0)
        self.scoreShowCheckBox = QCheckBox(self.scoreGroupBox)
        self.scoreShowCheckBox.setObjectName(u"scoreShowCheckBox")

        self.gridLayout_11.addWidget(self.scoreShowCheckBox, 0, 0, 1, 1)


        self.gameplaySettingsGridLayout.addWidget(self.scoreGroupBox, 0, 1, 1, 1)

        self.hpBarGroupBox = QGroupBox(self.gameplaySettings)
        self.hpBarGroupBox.setObjectName(u"hpBarGroupBox")
        self.gridLayout_13 = QGridLayout(self.hpBarGroupBox)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, 4, -1, 0)
        self.hpBarShowCheckBox = QCheckBox(self.hpBarGroupBox)
        self.hpBarShowCheckBox.setObjectName(u"hpBarShowCheckBox")

        self.gridLayout_13.addWidget(self.hpBarShowCheckBox, 0, 0, 1, 1)


        self.gameplaySettingsGridLayout.addWidget(self.hpBarGroupBox, 0, 2, 1, 1)

        self.comboCounterGroupBox = QGroupBox(self.gameplaySettings)
        self.comboCounterGroupBox.setObjectName(u"comboCounterGroupBox")
        self.gridLayout_17 = QGridLayout(self.comboCounterGroupBox)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(-1, 4, -1, 0)
        self.comboCounterShowCheckBox = QCheckBox(self.comboCounterGroupBox)
        self.comboCounterShowCheckBox.setObjectName(u"comboCounterShowCheckBox")

        self.gridLayout_17.addWidget(self.comboCounterShowCheckBox, 0, 0, 1, 1)


        self.gameplaySettingsGridLayout.addWidget(self.comboCounterGroupBox, 0, 3, 1, 1)

        self.hitCounterGroupBox = QGroupBox(self.gameplaySettings)
        self.hitCounterGroupBox.setObjectName(u"hitCounterGroupBox")
        self.gridLayout_24 = QGridLayout(self.hitCounterGroupBox)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(9, 4, -1, 0)
        self.hitCounterShowCheckBox = QCheckBox(self.hitCounterGroupBox)
        self.hitCounterShowCheckBox.setObjectName(u"hitCounterShowCheckBox")

        self.gridLayout_24.addWidget(self.hitCounterShowCheckBox, 0, 0, 1, 1)


        self.gameplaySettingsGridLayout.addWidget(self.hitCounterGroupBox, 1, 0, 1, 1)

        self.aimErrorMeterGroupBox = QGroupBox(self.gameplaySettings)
        self.aimErrorMeterGroupBox.setObjectName(u"aimErrorMeterGroupBox")
        self.gridLayout_18 = QGridLayout(self.aimErrorMeterGroupBox)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(-1, 4, -1, 0)
        self.aimErrorMeterShowCheckBox = QCheckBox(self.aimErrorMeterGroupBox)
        self.aimErrorMeterShowCheckBox.setObjectName(u"aimErrorMeterShowCheckBox")

        self.gridLayout_18.addWidget(self.aimErrorMeterShowCheckBox, 0, 0, 1, 1)


        self.gameplaySettingsGridLayout.addWidget(self.aimErrorMeterGroupBox, 1, 1, 1, 1)

        self.keyOverlayGroupBox = QGroupBox(self.gameplaySettings)
        self.keyOverlayGroupBox.setObjectName(u"keyOverlayGroupBox")
        self.gridLayout_20 = QGridLayout(self.keyOverlayGroupBox)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(-1, 4, -1, 0)
        self.keyOverlayShowCheckBox = QCheckBox(self.keyOverlayGroupBox)
        self.keyOverlayShowCheckBox.setObjectName(u"keyOverlayShowCheckBox")

        self.gridLayout_20.addWidget(self.keyOverlayShowCheckBox, 0, 0, 1, 1)


        self.gameplaySettingsGridLayout.addWidget(self.keyOverlayGroupBox, 1, 2, 1, 1)

        self.strainGraphGroupBox = QGroupBox(self.gameplaySettings)
        self.strainGraphGroupBox.setObjectName(u"strainGraphGroupBox")
        self.gridLayout_26 = QGridLayout(self.strainGraphGroupBox)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(-1, 4, -1, 0)
        self.strainGraphShowCheckBox = QCheckBox(self.strainGraphGroupBox)
        self.strainGraphShowCheckBox.setObjectName(u"strainGraphShowCheckBox")

        self.gridLayout_26.addWidget(self.strainGraphShowCheckBox, 0, 0, 1, 1)


        self.gameplaySettingsGridLayout.addWidget(self.strainGraphGroupBox, 1, 3, 1, 1)


        self.gameplaySettingsVerticalLayout.addLayout(self.gameplaySettingsGridLayout)

        self.gameplaySettingsHorizontalLayout = QHBoxLayout()
        self.gameplaySettingsHorizontalLayout.setObjectName(u"gameplaySettingsHorizontalLayout")
        self.resultsScreenGroupBox = QGroupBox(self.gameplaySettings)
        self.resultsScreenGroupBox.setObjectName(u"resultsScreenGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.resultsScreenGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 4, 9, 0)
        self.resultsScreenVerticalLayout = QVBoxLayout()
        self.resultsScreenVerticalLayout.setObjectName(u"resultsScreenVerticalLayout")
        self.resultsScreenShowCheckBox = QCheckBox(self.resultsScreenGroupBox)
        self.resultsScreenShowCheckBox.setObjectName(u"resultsScreenShowCheckBox")

        self.resultsScreenVerticalLayout.addWidget(self.resultsScreenShowCheckBox)

        self.resultsScreenUseLocalTimeZoneCheckBox = QCheckBox(self.resultsScreenGroupBox)
        self.resultsScreenUseLocalTimeZoneCheckBox.setObjectName(u"resultsScreenUseLocalTimeZoneCheckBox")
        self.resultsScreenUseLocalTimeZoneCheckBox.setEnabled(False)

        self.resultsScreenVerticalLayout.addWidget(self.resultsScreenUseLocalTimeZoneCheckBox)

        self.resultsScreenTimeFormLayout = QFormLayout()
        self.resultsScreenTimeFormLayout.setObjectName(u"resultsScreenTimeFormLayout")
        self.resultsScreenTimeLabel = QLabel(self.resultsScreenGroupBox)
        self.resultsScreenTimeLabel.setObjectName(u"resultsScreenTimeLabel")

        self.resultsScreenTimeFormLayout.setWidget(0, QFormLayout.LabelRole, self.resultsScreenTimeLabel)

        self.resultsScreenTimeSpinBox = QSpinBox(self.resultsScreenGroupBox)
        self.resultsScreenTimeSpinBox.setObjectName(u"resultsScreenTimeSpinBox")
        self.resultsScreenTimeSpinBox.setEnabled(False)

        self.resultsScreenTimeFormLayout.setWidget(0, QFormLayout.FieldRole, self.resultsScreenTimeSpinBox)


        self.resultsScreenVerticalLayout.addLayout(self.resultsScreenTimeFormLayout)


        self.verticalLayout_2.addLayout(self.resultsScreenVerticalLayout)


        self.gameplaySettingsHorizontalLayout.addWidget(self.resultsScreenGroupBox)

        self.modsGroupBox = QGroupBox(self.gameplaySettings)
        self.modsGroupBox.setObjectName(u"modsGroupBox")
        self.verticalLayout = QVBoxLayout(self.modsGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.modsVerticalLayout = QVBoxLayout()
        self.modsVerticalLayout.setObjectName(u"modsVerticalLayout")
        self.modsShowCheckBox = QCheckBox(self.modsGroupBox)
        self.modsShowCheckBox.setObjectName(u"modsShowCheckBox")

        self.modsVerticalLayout.addWidget(self.modsShowCheckBox)

        self.modsHideInReplaysCheckBox = QCheckBox(self.modsGroupBox)
        self.modsHideInReplaysCheckBox.setObjectName(u"modsHideInReplaysCheckBox")
        self.modsHideInReplaysCheckBox.setEnabled(False)

        self.modsVerticalLayout.addWidget(self.modsHideInReplaysCheckBox)

        self.modsFoldInReplaysCheckBox = QCheckBox(self.modsGroupBox)
        self.modsFoldInReplaysCheckBox.setObjectName(u"modsFoldInReplaysCheckBox")
        self.modsFoldInReplaysCheckBox.setEnabled(False)

        self.modsVerticalLayout.addWidget(self.modsFoldInReplaysCheckBox)


        self.verticalLayout.addLayout(self.modsVerticalLayout)


        self.gameplaySettingsHorizontalLayout.addWidget(self.modsGroupBox)

        self.scoreBoardGroupBox = QGroupBox(self.gameplaySettings)
        self.scoreBoardGroupBox.setObjectName(u"scoreBoardGroupBox")
        self.gridLayout_4 = QGridLayout(self.scoreBoardGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scoreBoardVerticalLayout = QVBoxLayout()
        self.scoreBoardVerticalLayout.setObjectName(u"scoreBoardVerticalLayout")
        self.scoreBoardShowCheckBox = QCheckBox(self.scoreBoardGroupBox)
        self.scoreBoardShowCheckBox.setObjectName(u"scoreBoardShowCheckBox")

        self.scoreBoardVerticalLayout.addWidget(self.scoreBoardShowCheckBox)

        self.scoreBoardHideOthersCheckBox = QCheckBox(self.scoreBoardGroupBox)
        self.scoreBoardHideOthersCheckBox.setObjectName(u"scoreBoardHideOthersCheckBox")
        self.scoreBoardHideOthersCheckBox.setEnabled(False)

        self.scoreBoardVerticalLayout.addWidget(self.scoreBoardHideOthersCheckBox)

        self.scoreBoardShowAvatarsCheckBox = QCheckBox(self.scoreBoardGroupBox)
        self.scoreBoardShowAvatarsCheckBox.setObjectName(u"scoreBoardShowAvatarsCheckBox")
        self.scoreBoardShowAvatarsCheckBox.setEnabled(False)

        self.scoreBoardVerticalLayout.addWidget(self.scoreBoardShowAvatarsCheckBox)


        self.gridLayout_4.addLayout(self.scoreBoardVerticalLayout, 0, 0, 1, 1)


        self.gameplaySettingsHorizontalLayout.addWidget(self.scoreBoardGroupBox)

        self.ppCounterGroupBox = QGroupBox(self.gameplaySettings)
        self.ppCounterGroupBox.setObjectName(u"ppCounterGroupBox")
        self.gridLayout_2 = QGridLayout(self.ppCounterGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ppCounterVerticalLayout = QVBoxLayout()
        self.ppCounterVerticalLayout.setObjectName(u"ppCounterVerticalLayout")
        self.ppCounterShowCheckBox = QCheckBox(self.ppCounterGroupBox)
        self.ppCounterShowCheckBox.setObjectName(u"ppCounterShowCheckBox")

        self.ppCounterVerticalLayout.addWidget(self.ppCounterShowCheckBox)

        self.ppCounterUseLazerPPCheckBox = QCheckBox(self.ppCounterGroupBox)
        self.ppCounterUseLazerPPCheckBox.setObjectName(u"ppCounterUseLazerPPCheckBox")

        self.ppCounterVerticalLayout.addWidget(self.ppCounterUseLazerPPCheckBox)


        self.gridLayout_2.addLayout(self.ppCounterVerticalLayout, 0, 0, 1, 1)


        self.gameplaySettingsHorizontalLayout.addWidget(self.ppCounterGroupBox)


        self.gameplaySettingsVerticalLayout.addLayout(self.gameplaySettingsHorizontalLayout)

        self.gameplaySettingsGridLayout_2 = QHBoxLayout()
        self.gameplaySettingsGridLayout_2.setObjectName(u"gameplaySettingsGridLayout_2")
        self.inputGroupBox = QGroupBox(self.gameplaySettings)
        self.inputGroupBox.setObjectName(u"inputGroupBox")
        self.gridLayout_22 = QGridLayout(self.inputGroupBox)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(-1, 4, -1, 0)
        self.inputGridLayout = QGridLayout()
        self.inputGridLayout.setObjectName(u"inputGridLayout")
        self.inputGridLayout.setHorizontalSpacing(20)
        self.mouseButtonsDisabledCheckBox = QCheckBox(self.inputGroupBox)
        self.mouseButtonsDisabledCheckBox.setObjectName(u"mouseButtonsDisabledCheckBox")

        self.inputGridLayout.addWidget(self.mouseButtonsDisabledCheckBox, 0, 1, 1, 1)

        self.empty_widget_2 = QWidget(self.inputGroupBox)
        self.empty_widget_2.setObjectName(u"empty_widget_2")

        self.inputGridLayout.addWidget(self.empty_widget_2, 1, 1, 1, 1)

        self.inputKeyGridLayout = QGridLayout()
        self.inputKeyGridLayout.setObjectName(u"inputKeyGridLayout")
        self.inputKeyGridLayout.setHorizontalSpacing(10)
        self.leftKeyHorizontalLayout = QHBoxLayout()
        self.leftKeyHorizontalLayout.setObjectName(u"leftKeyHorizontalLayout")
        self.leftKeyLabel = QLabel(self.inputGroupBox)
        self.leftKeyLabel.setObjectName(u"leftKeyLabel")

        self.leftKeyHorizontalLayout.addWidget(self.leftKeyLabel)

        self.leftKeyPushButton = QPushButton(self.inputGroupBox)
        self.leftKeyPushButton.setObjectName(u"leftKeyPushButton")
        self.leftKeyPushButton.setText(u"")

        self.leftKeyHorizontalLayout.addWidget(self.leftKeyPushButton)

        self.leftKeyHorizontalLayout.setStretch(0, 1)
        self.leftKeyHorizontalLayout.setStretch(1, 1)

        self.inputKeyGridLayout.addLayout(self.leftKeyHorizontalLayout, 0, 0, 1, 1)

        self.restartKeyHorizontalLayout = QHBoxLayout()
        self.restartKeyHorizontalLayout.setObjectName(u"restartKeyHorizontalLayout")
        self.restartKeyLabel = QLabel(self.inputGroupBox)
        self.restartKeyLabel.setObjectName(u"restartKeyLabel")

        self.restartKeyHorizontalLayout.addWidget(self.restartKeyLabel)

        self.restartKeyPushButton = QPushButton(self.inputGroupBox)
        self.restartKeyPushButton.setObjectName(u"restartKeyPushButton")
        self.restartKeyPushButton.setText(u"")

        self.restartKeyHorizontalLayout.addWidget(self.restartKeyPushButton)

        self.restartKeyHorizontalLayout.setStretch(0, 1)
        self.restartKeyHorizontalLayout.setStretch(1, 1)

        self.inputKeyGridLayout.addLayout(self.restartKeyHorizontalLayout, 0, 1, 1, 1)

        self.rightKeyHorizontalLayout = QHBoxLayout()
        self.rightKeyHorizontalLayout.setObjectName(u"rightKeyHorizontalLayout")
        self.rightKeyLabel = QLabel(self.inputGroupBox)
        self.rightKeyLabel.setObjectName(u"rightKeyLabel")

        self.rightKeyHorizontalLayout.addWidget(self.rightKeyLabel)

        self.rightKeyPushButton = QPushButton(self.inputGroupBox)
        self.rightKeyPushButton.setObjectName(u"rightKeyPushButton")
        self.rightKeyPushButton.setText(u"")

        self.rightKeyHorizontalLayout.addWidget(self.rightKeyPushButton)

        self.rightKeyHorizontalLayout.setStretch(0, 1)
        self.rightKeyHorizontalLayout.setStretch(1, 1)

        self.inputKeyGridLayout.addLayout(self.rightKeyHorizontalLayout, 1, 0, 1, 1)

        self.smokeKeyHorizontalLayout = QHBoxLayout()
        self.smokeKeyHorizontalLayout.setObjectName(u"smokeKeyHorizontalLayout")
        self.smokeKeyLabel = QLabel(self.inputGroupBox)
        self.smokeKeyLabel.setObjectName(u"smokeKeyLabel")

        self.smokeKeyHorizontalLayout.addWidget(self.smokeKeyLabel)

        self.smokeKeyPushButton = QPushButton(self.inputGroupBox)
        self.smokeKeyPushButton.setObjectName(u"smokeKeyPushButton")
        self.smokeKeyPushButton.setText(u"")

        self.smokeKeyHorizontalLayout.addWidget(self.smokeKeyPushButton)

        self.smokeKeyHorizontalLayout.setStretch(0, 1)
        self.smokeKeyHorizontalLayout.setStretch(1, 1)

        self.inputKeyGridLayout.addLayout(self.smokeKeyHorizontalLayout, 1, 1, 1, 1)


        self.inputGridLayout.addLayout(self.inputKeyGridLayout, 0, 0, 2, 1)


        self.gridLayout_22.addLayout(self.inputGridLayout, 0, 0, 1, 1)


        self.gameplaySettingsGridLayout_2.addWidget(self.inputGroupBox)

        self.hitErrorMeterGroupBox = QGroupBox(self.gameplaySettings)
        self.hitErrorMeterGroupBox.setObjectName(u"hitErrorMeterGroupBox")
        self.gridLayout_7 = QGridLayout(self.hitErrorMeterGroupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.hitErrorMeterVerticalLayout = QVBoxLayout()
        self.hitErrorMeterVerticalLayout.setObjectName(u"hitErrorMeterVerticalLayout")
        self.hitErrorMeterShowCheckBox = QCheckBox(self.hitErrorMeterGroupBox)
        self.hitErrorMeterShowCheckBox.setObjectName(u"hitErrorMeterShowCheckBox")

        self.hitErrorMeterVerticalLayout.addWidget(self.hitErrorMeterShowCheckBox)

        self.hitErrorMeterShowUnstableRateCheckBox = QCheckBox(self.hitErrorMeterGroupBox)
        self.hitErrorMeterShowUnstableRateCheckBox.setObjectName(u"hitErrorMeterShowUnstableRateCheckBox")
        self.hitErrorMeterShowUnstableRateCheckBox.setEnabled(False)

        self.hitErrorMeterVerticalLayout.addWidget(self.hitErrorMeterShowUnstableRateCheckBox)


        self.gridLayout_7.addLayout(self.hitErrorMeterVerticalLayout, 0, 0, 1, 1)


        self.gameplaySettingsGridLayout_2.addWidget(self.hitErrorMeterGroupBox)

        self.gameplaySettingsGridLayout_2.setStretch(0, 4)
        self.gameplaySettingsGridLayout_2.setStretch(1, 1)

        self.gameplaySettingsVerticalLayout.addLayout(self.gameplaySettingsGridLayout_2)


        self.gridLayout_12.addLayout(self.gameplaySettingsVerticalLayout, 0, 0, 1, 1)

        self.settingsTabWidget.addTab(self.gameplaySettings, "")
        self.skinSettings = QWidget()
        self.skinSettings.setObjectName(u"skinSettings")
        self.gridLayout_19 = QGridLayout(self.skinSettings)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.skinSettingsGridLayout = QGridLayout()
        self.skinSettingsGridLayout.setObjectName(u"skinSettingsGridLayout")
        self.skinGeneralGroupBox = QGroupBox(self.skinSettings)
        self.skinGeneralGroupBox.setObjectName(u"skinGeneralGroupBox")
        self.gridLayout_16 = QGridLayout(self.skinGeneralGroupBox)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.skinGeneralVerticalLayout = QVBoxLayout()
        self.skinGeneralVerticalLayout.setObjectName(u"skinGeneralVerticalLayout")
        self.useSkinColorsRadioButton = QRadioButton(self.skinGeneralGroupBox)
        self.useSkinOrBeatmapColorsButtonGroup = QButtonGroup(MainWindow)
        self.useSkinOrBeatmapColorsButtonGroup.setObjectName(u"useSkinOrBeatmapColorsButtonGroup")
        self.useSkinOrBeatmapColorsButtonGroup.addButton(self.useSkinColorsRadioButton)
        self.useSkinColorsRadioButton.setObjectName(u"useSkinColorsRadioButton")
        self.useSkinColorsRadioButton.setChecked(True)

        self.skinGeneralVerticalLayout.addWidget(self.useSkinColorsRadioButton)

        self.useBeatmapColorsRadioButton = QRadioButton(self.skinGeneralGroupBox)
        self.useSkinOrBeatmapColorsButtonGroup.addButton(self.useBeatmapColorsRadioButton)
        self.useBeatmapColorsRadioButton.setObjectName(u"useBeatmapColorsRadioButton")

        self.skinGeneralVerticalLayout.addWidget(self.useBeatmapColorsRadioButton)

        self.useSkinCursorCheckBox = QCheckBox(self.skinGeneralGroupBox)
        self.useSkinCursorCheckBox.setObjectName(u"useSkinCursorCheckBox")

        self.skinGeneralVerticalLayout.addWidget(self.useSkinCursorCheckBox)

        self.useSkinHitsoundsCheckBox = QCheckBox(self.skinGeneralGroupBox)
        self.useSkinHitsoundsCheckBox.setObjectName(u"useSkinHitsoundsCheckBox")

        self.skinGeneralVerticalLayout.addWidget(self.useSkinHitsoundsCheckBox)


        self.gridLayout_16.addLayout(self.skinGeneralVerticalLayout, 0, 0, 1, 1)


        self.skinSettingsGridLayout.addWidget(self.skinGeneralGroupBox, 0, 0, 1, 1)

        self.cursorGroupBox = QGroupBox(self.skinSettings)
        self.cursorGroupBox.setObjectName(u"cursorGroupBox")
        self.gridLayout_15 = QGridLayout(self.cursorGroupBox)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.cursorVerticalLayout = QVBoxLayout()
        self.cursorVerticalLayout.setObjectName(u"cursorVerticalLayout")
        self.scaleToCSCheckBox = QCheckBox(self.cursorGroupBox)
        self.scaleToCSCheckBox.setObjectName(u"scaleToCSCheckBox")

        self.cursorVerticalLayout.addWidget(self.scaleToCSCheckBox)

        self.cursorRipplesCheckBox = QCheckBox(self.cursorGroupBox)
        self.cursorRipplesCheckBox.setObjectName(u"cursorRipplesCheckBox")

        self.cursorVerticalLayout.addWidget(self.cursorRipplesCheckBox)

        self.cursorSizeGridLayout = QGridLayout()
        self.cursorSizeGridLayout.setObjectName(u"cursorSizeGridLayout")
        self.cursorSizeSlider = QLabeledDoubleSlider(self.cursorGroupBox)
        self.cursorSizeSlider.setObjectName(u"cursorSizeSlider")
        self.cursorSizeSlider.setMinimum(50)
        self.cursorSizeSlider.setMaximum(200)
        self.cursorSizeSlider.setPageStep(50)
        self.cursorSizeSlider.setValue(100)
        self.cursorSizeSlider.setOrientation(Qt.Horizontal)
        self.cursorSizeSlider.setTickPosition(QSlider.TicksAbove)
        self.cursorSizeSlider.setTickInterval(50)

        self.cursorSizeGridLayout.addWidget(self.cursorSizeSlider, 0, 1, 1, 1)

        self.cursorSizeLabel = QLabel(self.cursorGroupBox)
        self.cursorSizeLabel.setObjectName(u"cursorSizeLabel")

        self.cursorSizeGridLayout.addWidget(self.cursorSizeLabel, 0, 0, 1, 1)


        self.cursorVerticalLayout.addLayout(self.cursorSizeGridLayout)

        self.forceLongTrailVerticalLayout = QVBoxLayout()
        self.forceLongTrailVerticalLayout.setObjectName(u"forceLongTrailVerticalLayout")
        self.forceLongTrailCheckBox = QCheckBox(self.cursorGroupBox)
        self.forceLongTrailCheckBox.setObjectName(u"forceLongTrailCheckBox")

        self.forceLongTrailVerticalLayout.addWidget(self.forceLongTrailCheckBox)

        self.longTrailDensityFormLayout = QFormLayout()
        self.longTrailDensityFormLayout.setObjectName(u"longTrailDensityFormLayout")
        self.longTrailDensityLabel = QLabel(self.cursorGroupBox)
        self.longTrailDensityLabel.setObjectName(u"longTrailDensityLabel")

        self.longTrailDensityFormLayout.setWidget(0, QFormLayout.LabelRole, self.longTrailDensityLabel)

        self.longTrailDensitySpinBox = QSpinBox(self.cursorGroupBox)
        self.longTrailDensitySpinBox.setObjectName(u"longTrailDensitySpinBox")
        self.longTrailDensitySpinBox.setEnabled(False)
        self.longTrailDensitySpinBox.setMinimum(0)
        self.longTrailDensitySpinBox.setMaximum(10000)

        self.longTrailDensityFormLayout.setWidget(0, QFormLayout.FieldRole, self.longTrailDensitySpinBox)


        self.forceLongTrailVerticalLayout.addLayout(self.longTrailDensityFormLayout)

        self.longTrailLengthFormLayout = QFormLayout()
        self.longTrailLengthFormLayout.setObjectName(u"longTrailLengthFormLayout")
        self.longTrailLengthLabel = QLabel(self.cursorGroupBox)
        self.longTrailLengthLabel.setObjectName(u"longTrailLengthLabel")

        self.longTrailLengthFormLayout.setWidget(0, QFormLayout.LabelRole, self.longTrailLengthLabel)

        self.longTrailLengthSpinBox = QSpinBox(self.cursorGroupBox)
        self.longTrailLengthSpinBox.setObjectName(u"longTrailLengthSpinBox")
        self.longTrailLengthSpinBox.setEnabled(False)
        self.longTrailLengthSpinBox.setMinimum(0)
        self.longTrailLengthSpinBox.setMaximum(10000)

        self.longTrailLengthFormLayout.setWidget(0, QFormLayout.FieldRole, self.longTrailLengthSpinBox)


        self.forceLongTrailVerticalLayout.addLayout(self.longTrailLengthFormLayout)


        self.cursorVerticalLayout.addLayout(self.forceLongTrailVerticalLayout)

        self.cursorRainbowCheckBox = QCheckBox(self.cursorGroupBox)
        self.cursorRainbowCheckBox.setObjectName(u"cursorRainbowCheckBox")

        self.cursorVerticalLayout.addWidget(self.cursorRainbowCheckBox)

        self.cursorTrailGlowCheckBox = QCheckBox(self.cursorGroupBox)
        self.cursorTrailGlowCheckBox.setObjectName(u"cursorTrailGlowCheckBox")

        self.cursorVerticalLayout.addWidget(self.cursorTrailGlowCheckBox)


        self.gridLayout_15.addLayout(self.cursorVerticalLayout, 0, 0, 1, 1)


        self.skinSettingsGridLayout.addWidget(self.cursorGroupBox, 0, 1, 2, 1)

        self.empty_widget_3 = QWidget(self.skinSettings)
        self.empty_widget_3.setObjectName(u"empty_widget_3")

        self.skinSettingsGridLayout.addWidget(self.empty_widget_3, 1, 0, 2, 1)

        self.objectsGroupBox = QGroupBox(self.skinSettings)
        self.objectsGroupBox.setObjectName(u"objectsGroupBox")
        self.gridLayout_14 = QGridLayout(self.objectsGroupBox)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.objectsVerticalLayout = QVBoxLayout()
        self.objectsVerticalLayout.setObjectName(u"objectsVerticalLayout")
        self.drawFollowPointsCheckBox = QCheckBox(self.objectsGroupBox)
        self.drawFollowPointsCheckBox.setObjectName(u"drawFollowPointsCheckBox")

        self.objectsVerticalLayout.addWidget(self.drawFollowPointsCheckBox)

        self.drawComboNumbersCheckBox = QCheckBox(self.objectsGroupBox)
        self.drawComboNumbersCheckBox.setObjectName(u"drawComboNumbersCheckBox")

        self.objectsVerticalLayout.addWidget(self.drawComboNumbersCheckBox)

        self.scaleToTheBeatCheckBox = QCheckBox(self.objectsGroupBox)
        self.scaleToTheBeatCheckBox.setObjectName(u"scaleToTheBeatCheckBox")

        self.objectsVerticalLayout.addWidget(self.scaleToTheBeatCheckBox)

        self.sliderMergeCheckBox = QCheckBox(self.objectsGroupBox)
        self.sliderMergeCheckBox.setObjectName(u"sliderMergeCheckBox")

        self.objectsVerticalLayout.addWidget(self.sliderMergeCheckBox)

        self.objectsRainbowCheckBox = QCheckBox(self.objectsGroupBox)
        self.objectsRainbowCheckBox.setObjectName(u"objectsRainbowCheckBox")

        self.objectsVerticalLayout.addWidget(self.objectsRainbowCheckBox)

        self.flashToTheBeatCheckBox = QCheckBox(self.objectsGroupBox)
        self.flashToTheBeatCheckBox.setObjectName(u"flashToTheBeatCheckBox")

        self.objectsVerticalLayout.addWidget(self.flashToTheBeatCheckBox)

        self.useHitCircleColorCheckBox = QCheckBox(self.objectsGroupBox)
        self.useHitCircleColorCheckBox.setObjectName(u"useHitCircleColorCheckBox")

        self.objectsVerticalLayout.addWidget(self.useHitCircleColorCheckBox)

        self.sliderSnakingInCheckBox = QCheckBox(self.objectsGroupBox)
        self.sliderSnakingInCheckBox.setObjectName(u"sliderSnakingInCheckBox")

        self.objectsVerticalLayout.addWidget(self.sliderSnakingInCheckBox)

        self.sliderSnakingOutCheckBox = QCheckBox(self.objectsGroupBox)
        self.sliderSnakingOutCheckBox.setObjectName(u"sliderSnakingOutCheckBox")

        self.objectsVerticalLayout.addWidget(self.sliderSnakingOutCheckBox)


        self.gridLayout_14.addLayout(self.objectsVerticalLayout, 0, 0, 1, 1)


        self.skinSettingsGridLayout.addWidget(self.objectsGroupBox, 0, 2, 2, 1)


        self.gridLayout_19.addLayout(self.skinSettingsGridLayout, 0, 0, 1, 1)

        self.settingsTabWidget.addTab(self.skinSettings, "")
        self.otherSettings = QWidget()
        self.otherSettings.setObjectName(u"otherSettings")
        self.gridLayout_21 = QGridLayout(self.otherSettings)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.playfieldGroupBox = QGroupBox(self.otherSettings)
        self.playfieldGroupBox.setObjectName(u"playfieldGroupBox")
        self.gridLayout_25 = QGridLayout(self.playfieldGroupBox)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.playfieldGridLayout = QGridLayout()
        self.playfieldGridLayout.setObjectName(u"playfieldGridLayout")
        self.playfieldCheckBoxVerticalLayout = QVBoxLayout()
        self.playfieldCheckBoxVerticalLayout.setObjectName(u"playfieldCheckBoxVerticalLayout")
        self.seizureWarningCheckBox = QCheckBox(self.playfieldGroupBox)
        self.seizureWarningCheckBox.setObjectName(u"seizureWarningCheckBox")

        self.playfieldCheckBoxVerticalLayout.addWidget(self.seizureWarningCheckBox)

        self.loadStoryboardCheckBox = QCheckBox(self.playfieldGroupBox)
        self.loadStoryboardCheckBox.setObjectName(u"loadStoryboardCheckBox")

        self.playfieldCheckBoxVerticalLayout.addWidget(self.loadStoryboardCheckBox)

        self.loadVideoCheckBox = QCheckBox(self.playfieldGroupBox)
        self.loadVideoCheckBox.setObjectName(u"loadVideoCheckBox")

        self.playfieldCheckBoxVerticalLayout.addWidget(self.loadVideoCheckBox)

        self.bgParallaxCheckBox = QCheckBox(self.playfieldGroupBox)
        self.bgParallaxCheckBox.setObjectName(u"bgParallaxCheckBox")

        self.playfieldCheckBoxVerticalLayout.addWidget(self.bgParallaxCheckBox)

        self.showDanserLogoCheckBox = QCheckBox(self.playfieldGroupBox)
        self.showDanserLogoCheckBox.setObjectName(u"showDanserLogoCheckBox")

        self.playfieldCheckBoxVerticalLayout.addWidget(self.showDanserLogoCheckBox)

        self.skipIntroCheckBox = QCheckBox(self.playfieldGroupBox)
        self.skipIntroCheckBox.setObjectName(u"skipIntroCheckBox")

        self.playfieldCheckBoxVerticalLayout.addWidget(self.skipIntroCheckBox)

        self.quickStartCheckBox = QCheckBox(self.playfieldGroupBox)
        self.quickStartCheckBox.setObjectName(u"quickStartCheckBox")

        self.playfieldCheckBoxVerticalLayout.addWidget(self.quickStartCheckBox)


        self.playfieldGridLayout.addLayout(self.playfieldCheckBoxVerticalLayout, 0, 0, 1, 1)

        self.backgroundDimGroupBox = QGroupBox(self.playfieldGroupBox)
        self.backgroundDimGroupBox.setObjectName(u"backgroundDimGroupBox")
        self.backgroundDimGroupBox.setMaximumSize(QSize(16777215, 140))
        self.verticalLayout_14 = QVBoxLayout(self.backgroundDimGroupBox)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.backgroundDimVerticalLayout = QVBoxLayout()
        self.backgroundDimVerticalLayout.setObjectName(u"backgroundDimVerticalLayout")
        self.introBGDimFormLayout = QFormLayout()
        self.introBGDimFormLayout.setObjectName(u"introBGDimFormLayout")
        self.introBGDimLabel = QLabel(self.backgroundDimGroupBox)
        self.introBGDimLabel.setObjectName(u"introBGDimLabel")

        self.introBGDimFormLayout.setWidget(0, QFormLayout.LabelRole, self.introBGDimLabel)

        self.introBGDimSlider = QLabeledSlider(self.backgroundDimGroupBox)
        self.introBGDimSlider.setObjectName(u"introBGDimSlider")
        self.introBGDimSlider.setCursor(QCursor(Qt.SizeHorCursor))
        self.introBGDimSlider.setMouseTracking(False)
        self.introBGDimSlider.setLayoutDirection(Qt.LeftToRight)
        self.introBGDimSlider.setAutoFillBackground(False)
        self.introBGDimSlider.setInputMethodHints(Qt.ImhNone)
        self.introBGDimSlider.setMaximum(100)
        self.introBGDimSlider.setValue(100)
        self.introBGDimSlider.setTracking(False)
        self.introBGDimSlider.setOrientation(Qt.Horizontal)
        self.introBGDimSlider.setInvertedAppearance(False)
        self.introBGDimSlider.setInvertedControls(False)
        self.introBGDimSlider.setTickPosition(QSlider.NoTicks)

        self.introBGDimFormLayout.setWidget(0, QFormLayout.FieldRole, self.introBGDimSlider)


        self.backgroundDimVerticalLayout.addLayout(self.introBGDimFormLayout)

        self.inGameBGDimFormLayout = QFormLayout()
        self.inGameBGDimFormLayout.setObjectName(u"inGameBGDimFormLayout")
        self.inGameBGDimLabel = QLabel(self.backgroundDimGroupBox)
        self.inGameBGDimLabel.setObjectName(u"inGameBGDimLabel")

        self.inGameBGDimFormLayout.setWidget(0, QFormLayout.LabelRole, self.inGameBGDimLabel)

        self.inGameBGDimSlider = QLabeledSlider(self.backgroundDimGroupBox)
        self.inGameBGDimSlider.setObjectName(u"inGameBGDimSlider")
        self.inGameBGDimSlider.setCursor(QCursor(Qt.SizeHorCursor))
        self.inGameBGDimSlider.setMaximum(100)
        self.inGameBGDimSlider.setValue(100)
        self.inGameBGDimSlider.setOrientation(Qt.Horizontal)

        self.inGameBGDimFormLayout.setWidget(0, QFormLayout.FieldRole, self.inGameBGDimSlider)


        self.backgroundDimVerticalLayout.addLayout(self.inGameBGDimFormLayout)

        self.breakBGDimFormLayout = QFormLayout()
        self.breakBGDimFormLayout.setObjectName(u"breakBGDimFormLayout")
        self.breakBGDimLabel = QLabel(self.backgroundDimGroupBox)
        self.breakBGDimLabel.setObjectName(u"breakBGDimLabel")

        self.breakBGDimFormLayout.setWidget(0, QFormLayout.LabelRole, self.breakBGDimLabel)

        self.breakBGDimSlider = QLabeledSlider(self.backgroundDimGroupBox)
        self.breakBGDimSlider.setObjectName(u"breakBGDimSlider")
        self.breakBGDimSlider.setCursor(QCursor(Qt.SizeHorCursor))
        self.breakBGDimSlider.setMaximum(100)
        self.breakBGDimSlider.setValue(100)
        self.breakBGDimSlider.setOrientation(Qt.Horizontal)
        self.breakBGDimSlider.setInvertedAppearance(False)
        self.breakBGDimSlider.setInvertedControls(False)
        self.breakBGDimSlider.setTickPosition(QSlider.NoTicks)

        self.breakBGDimFormLayout.setWidget(0, QFormLayout.FieldRole, self.breakBGDimSlider)


        self.backgroundDimVerticalLayout.addLayout(self.breakBGDimFormLayout)


        self.verticalLayout_14.addLayout(self.backgroundDimVerticalLayout)


        self.playfieldGridLayout.addWidget(self.backgroundDimGroupBox, 0, 1, 1, 1)


        self.gridLayout_25.addLayout(self.playfieldGridLayout, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.playfieldGroupBox, 0, 0, 1, 1)

        self.empty_widget_6 = QWidget(self.otherSettings)
        self.empty_widget_6.setObjectName(u"empty_widget_6")
        self.empty_widget_6.setMinimumSize(QSize(150, 0))

        self.gridLayout_21.addWidget(self.empty_widget_6, 0, 1, 1, 1)

        self.empty_widget_7 = QWidget(self.otherSettings)
        self.empty_widget_7.setObjectName(u"empty_widget_7")
        self.empty_widget_7.setMinimumSize(QSize(0, 80))

        self.gridLayout_21.addWidget(self.empty_widget_7, 1, 0, 1, 2)

        self.settingsTabWidget.addTab(self.otherSettings, "")
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.gridLayout_28 = QGridLayout(self.aboutPage)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.aboutPageGridLayout = QGridLayout()
        self.aboutPageGridLayout.setObjectName(u"aboutPageGridLayout")
        self.empty_widget_5 = QWidget(self.aboutPage)
        self.empty_widget_5.setObjectName(u"empty_widget_5")

        self.aboutPageGridLayout.addWidget(self.empty_widget_5, 0, 0, 1, 1)

        self.danserGuiHorizontalLayout = QHBoxLayout()
        self.danserGuiHorizontalLayout.setObjectName(u"danserGuiHorizontalLayout")
        self.danserGuiLogo = QLabel(self.aboutPage)
        self.danserGuiLogo.setObjectName(u"danserGuiLogo")
        self.danserGuiLogo.setMinimumSize(QSize(60, 60))
        self.danserGuiLogo.setMaximumSize(QSize(60, 60))
        self.danserGuiLogo.setStyleSheet(u"")
        self.danserGuiLogo.setText(u"")
        self.danserGuiLogo.setTextFormat(Qt.AutoText)

        self.danserGuiHorizontalLayout.addWidget(self.danserGuiLogo)

        self.danserGuiDescriptionLabel = QLabel(self.aboutPage)
        self.danserGuiDescriptionLabel.setObjectName(u"danserGuiDescriptionLabel")
        self.danserGuiDescriptionLabel.setTextFormat(Qt.MarkdownText)
        self.danserGuiDescriptionLabel.setOpenExternalLinks(True)

        self.danserGuiHorizontalLayout.addWidget(self.danserGuiDescriptionLabel)


        self.aboutPageGridLayout.addLayout(self.danserGuiHorizontalLayout, 0, 1, 1, 1)

        self.empty_widget_4 = QWidget(self.aboutPage)
        self.empty_widget_4.setObjectName(u"empty_widget_4")

        self.aboutPageGridLayout.addWidget(self.empty_widget_4, 0, 2, 1, 1)

        self.aboutMainMarkdownLabel = QLabel(self.aboutPage)
        self.aboutMainMarkdownLabel.setObjectName(u"aboutMainMarkdownLabel")
        self.aboutMainMarkdownLabel.setTextFormat(Qt.MarkdownText)
        self.aboutMainMarkdownLabel.setWordWrap(True)
        self.aboutMainMarkdownLabel.setOpenExternalLinks(True)

        self.aboutPageGridLayout.addWidget(self.aboutMainMarkdownLabel, 1, 0, 1, 3)


        self.gridLayout_28.addLayout(self.aboutPageGridLayout, 0, 0, 1, 1)

        self.settingsTabWidget.addTab(self.aboutPage, "")

        self.settingsHorizontalLayout.addWidget(self.settingsTabWidget)


        self.horizontalLayout_3.addLayout(self.settingsHorizontalLayout)

        self.mainTabWidget.addTab(self.settingsTab, "")

        self.gridLayout.addWidget(self.mainTabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.mainTabWidget, self.danserModeComboBox)
        QWidget.setTabOrder(self.danserModeComboBox, self.osuSelectButton)
        QWidget.setTabOrder(self.osuSelectButton, self.osrPathLineEdit)
        QWidget.setTabOrder(self.osrPathLineEdit, self.osuPathLineEdit)
        QWidget.setTabOrder(self.osuPathLineEdit, self.skinsComboBox)
        QWidget.setTabOrder(self.skinsComboBox, self.osrSelectButton)

        self.retranslateUi(MainWindow)
        self.forceLongTrailCheckBox.clicked.connect(self.longTrailDensitySpinBox.setEnabled)
        self.forceLongTrailCheckBox.clicked.connect(self.longTrailLengthSpinBox.setEnabled)
        self.resultsScreenShowCheckBox.clicked.connect(self.resultsScreenUseLocalTimeZoneCheckBox.setEnabled)
        self.resultsScreenShowCheckBox.clicked.connect(self.resultsScreenTimeSpinBox.setEnabled)
        self.modsShowCheckBox.clicked.connect(self.modsHideInReplaysCheckBox.setEnabled)
        self.modsShowCheckBox.clicked.connect(self.modsFoldInReplaysCheckBox.setEnabled)
        self.scoreBoardShowCheckBox.clicked.connect(self.scoreBoardHideOthersCheckBox.setEnabled)
        self.scoreBoardShowCheckBox.clicked.connect(self.scoreBoardShowAvatarsCheckBox.setEnabled)
        self.hitErrorMeterShowCheckBox.clicked.connect(self.hitErrorMeterShowUnstableRateCheckBox.setEnabled)
        self.DTNCCheckBox.clicked.connect(self.HTCheckBox.setDisabled)
        self.HTCheckBox.clicked.connect(self.DTNCCheckBox.setDisabled)
        self.SDPFCheckBox.clicked.connect(self.NFCheckBox.setDisabled)
        self.NFCheckBox.clicked.connect(self.SDPFCheckBox.setDisabled)
        self.customizeBeatmapAttributesCheckBox.clicked.connect(self.beatmapAttributesGroupBox.setEnabled)
        self.cursorsInMirrorCollageCheckBox.clicked.connect(self.cursorsInMirrorCollageSpinBox.setEnabled)
        self.cursorsInTagModeCheckBox.clicked.connect(self.cursorsInTagModeSpinBox.setEnabled)
        self.quickStartCheckBox.clicked.connect(self.skipIntroCheckBox.setChecked)
        self.addDanserCheckBox.clicked.connect(self.danserNameLineEdit.setEnabled)
        self.addDateAfterPlayerNamecheckBox.clicked.connect(self.dateFormatComboBox.setEnabled)

        self.mainTabWidget.setCurrentIndex(0)
        self.settingsTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.generalTab.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.startLogo.setToolTip(QCoreApplication.translate("MainWindow", u"Click it and start task!", None))
#endif // QT_CONFIG(tooltip)
        self.startLogo.setText("")
        self.danserModeLabel.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))

#if QT_CONFIG(tooltip)
        self.isRecordCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"realtime preview or generate recording", None))
#endif // QT_CONFIG(tooltip)
        self.isRecordCheckBox.setText(QCoreApplication.translate("MainWindow", u"Record Mode", None))
        self.openRecordingOutputFolderPushButton.setText(QCoreApplication.translate("MainWindow", u"Open Output Folder", None))
        self.osrSelectButton.setText(QCoreApplication.translate("MainWindow", u"SELECT REPLAY(.OSR)", None))
        self.osuSelectButton.setText(QCoreApplication.translate("MainWindow", u"SELECT BEATMAP(.OSU)", None))
        self.osrPathLabel.setText(QCoreApplication.translate("MainWindow", u"Replay(.osr) path:", None))
        self.osuPathLabel.setText(QCoreApplication.translate("MainWindow", u"Beatmap(.osu) path:", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.generalTab), QCoreApplication.translate("MainWindow", u"General", None))
        self.basicGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Basic", None))
        self.songsDBModeLabel.setText(QCoreApplication.translate("MainWindow", u"Songs DB Mode:", None))

        self.songsDBUpdatePushButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.songsPathLabel.setText(QCoreApplication.translate("MainWindow", u"Songs Path:", None))
        self.danserPathLabel.setText(QCoreApplication.translate("MainWindow", u"danser Path:", None))
        self.languageLabel.setText(QCoreApplication.translate("MainWindow", u"Language:", None))
        self.skinsPathLabel.setText(QCoreApplication.translate("MainWindow", u"Skins Path:", None))
        self.osuApiPathLabel.setText(QCoreApplication.translate("MainWindow", u"osu! api:", None))
#if QT_CONFIG(tooltip)
        self.osuApiLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"get it from https://osu.ppy.sh/api/", None))
#endif // QT_CONFIG(tooltip)
        self.osuApiLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Don't tell this to anyone!", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
#if QT_CONFIG(tooltip)
        self.usernameLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Your username (not the username of the replay)", None))
#endif // QT_CONFIG(tooltip)
        self.osuRootPathLabel.setText(QCoreApplication.translate("MainWindow", u"osu! Root Path:", None))
        self.volumeGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.globalVolumeLabel.setText(QCoreApplication.translate("MainWindow", u"Global:", None))
        self.musicVolumeLabel.setText(QCoreApplication.translate("MainWindow", u"Music:", None))
        self.hitSoundVolumeLabel.setText(QCoreApplication.translate("MainWindow", u"HitSound:", None))
        self.graphicsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Graphics", None))
        self.resolutionLabel.setText(QCoreApplication.translate("MainWindow", u"Resolution:", None))
        self.fullScreenCheckBox.setText(QCoreApplication.translate("MainWindow", u"Full Screen", None))
        self.vsyncCheckBox.setText(QCoreApplication.translate("MainWindow", u"Vsync", None))
        self.showFPSCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show FPS", None))
        self.MSAALabel.setText(QCoreApplication.translate("MainWindow", u"MSAA:", None))
        self.FPSCapLabel.setText(QCoreApplication.translate("MainWindow", u"FPS Cap:", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.generalSettings), QCoreApplication.translate("MainWindow", u"General", None))
        self.beatmapBasicGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Basic", None))
        self.timingRangeLabel.setText(QCoreApplication.translate("MainWindow", u"Timing:", None))
        self.beatmapSpeedLabel.setText(QCoreApplication.translate("MainWindow", u"Beatmap Speed:", None))
#if QT_CONFIG(tooltip)
        self.beatmapPitchDoubleSpinBox.setToolTip(QCoreApplication.translate("MainWindow", u"If you set beatmap pitch less than 1, it may be fun.", None))
#endif // QT_CONFIG(tooltip)
        self.beatmapPitchLabel.setText(QCoreApplication.translate("MainWindow", u"Beatmap Pitch:", None))
        self.specialGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Special", None))
        self.cursorsInMirrorCollageCheckBox.setText(QCoreApplication.translate("MainWindow", u"Cursors in Mirror Collage", None))
        self.cursorsInTagModeCheckBox.setText(QCoreApplication.translate("MainWindow", u"Cursors in TAG mode", None))
        self.beatmapCustomizeGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Customize", None))
        self.customizeBeatmapAttributesCheckBox.setText(QCoreApplication.translate("MainWindow", u"Customize Beatmap Attributes", None))
        self.beatmapAttributesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Beatmap Attributes", None))
        self.CSLabel.setText(QCoreApplication.translate("MainWindow", u"CS:", None))
        self.ARLabel.setText(QCoreApplication.translate("MainWindow", u"AR:", None))
        self.ODLabel.setText(QCoreApplication.translate("MainWindow", u"OD:", None))
        self.HPLabel.setText(QCoreApplication.translate("MainWindow", u"HP:", None))
#if QT_CONFIG(tooltip)
        self.beatmapModsGroupBox.setToolTip(QCoreApplication.translate("MainWindow", u"Displays the map with given mods. This is ignored in replay mode!", None))
#endif // QT_CONFIG(tooltip)
        self.beatmapModsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mods", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.beatmapSettings), QCoreApplication.translate("MainWindow", u"Beatmap", None))
        self.knockoutGeneralGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"General", None))
        self.knockoutModeLabel.setText(QCoreApplication.translate("MainWindow", u"Knockout Mode:", None))
        self.knockoutModeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ComboBreak", None))
        self.knockoutModeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"MaxCombo", None))
        self.knockoutModeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"XReplays", None))
        self.knockoutModeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"OneVsOne", None))
        self.knockoutModeComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"SSOrQuit", None))

#if QT_CONFIG(tooltip)
        self.knockoutModeComboBox.setToolTip(QCoreApplication.translate("MainWindow", u"Knockout mode. More info.", None))
#endif // QT_CONFIG(tooltip)
        self.sortByLabel.setText(QCoreApplication.translate("MainWindow", u"Sort By:", None))

        self.liveSortCheckBox.setText(QCoreApplication.translate("MainWindow", u"Live Sort", None))
#if QT_CONFIG(tooltip)
        self.knockoutCursorSizeLabel.setToolTip(QCoreApplication.translate("MainWindow", u"Minimum cursor size (when all players are alive)\n"
"Maximum cursor size (when there is only 1 player left)", None))
#endif // QT_CONFIG(tooltip)
        self.knockoutCursorSizeLabel.setText(QCoreApplication.translate("MainWindow", u"Cursor Size:", None))
#if QT_CONFIG(tooltip)
        self.revivePlayersAtEndCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Whether knocked out players should appear on map end.", None))
#endif // QT_CONFIG(tooltip)
        self.revivePlayersAtEndCheckBox.setText(QCoreApplication.translate("MainWindow", u"Revive Players At End", None))
        self.HideOverlayOnBreaksCheckBox.setText(QCoreApplication.translate("MainWindow", u"Hide Overlay On Breaks", None))
        self.maxPlayersLabel.setText(QCoreApplication.translate("MainWindow", u"Max Players:", None))
        self.addDanserCheckBox.setText(QCoreApplication.translate("MainWindow", u"Add Danser", None))
        self.danserNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Danser Name", None))
        self.openKnockoutReplaysFolderPushButton.setText(QCoreApplication.translate("MainWindow", u"open knockout replays folder", None))
#if QT_CONFIG(tooltip)
        self.graceEndTimeLabel.setToolTip(QCoreApplication.translate("MainWindow", u"In ComboBreak mode, players won't get knocked out if they break combo before this value (in seconds)", None))
#endif // QT_CONFIG(tooltip)
        self.graceEndTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Grace End Time:", None))
#if QT_CONFIG(tooltip)
        self.bubbleMinimumComboLabel.setToolTip(QCoreApplication.translate("MainWindow", u"Minimum combo before combo break to show a bubble in XReplays mode", None))
#endif // QT_CONFIG(tooltip)
        self.bubbleMinimumComboLabel.setText(QCoreApplication.translate("MainWindow", u"Bubble Minimum Combo:", None))
#if QT_CONFIG(tooltip)
        self.excludeModsGroupBox.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude plays which contain one of the mods set here", None))
#endif // QT_CONFIG(tooltip)
        self.excludeModsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Exclude Mods", None))
#if QT_CONFIG(tooltip)
        self.hideModsGroupBox.setToolTip(QCoreApplication.translate("MainWindow", u"Hide specific mods from being displayed in overlay (like NF)", None))
#endif // QT_CONFIG(tooltip)
        self.hideModsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Hide Mods", None))
        self.experimentalFeaturesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Experimental Features", None))
#if QT_CONFIG(tooltip)
        self.modifyOsrMD5CheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Change the Beatmap MD5 of the *.osr file in the replays folder to the MD5 of the currently selected beatmap, which is convenient for making a comparison video of the same song with different difficulties.", None))
#endif // QT_CONFIG(tooltip)
        self.modifyOsrMD5CheckBox.setText(QCoreApplication.translate("MainWindow", u"Modify the Beatmap MD5 of *.osr Files", None))
#if QT_CONFIG(tooltip)
        self.addDateAfterPlayerNamecheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"add the date after the player's username, which is convenient for making comparison videos of players in different periods.", None))
#endif // QT_CONFIG(tooltip)
        self.addDateAfterPlayerNamecheckBox.setText(QCoreApplication.translate("MainWindow", u"Add Date After Player Name", None))
        self.dateFormatLabel.setText(QCoreApplication.translate("MainWindow", u"Date Format:", None))
        self.dateFormatComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"YYYY-mm-dd", None))
        self.dateFormatComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"mm-dd-YYYY", None))
        self.dateFormatComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"dd-mm-YYYY", None))

        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.knockoutSettings), QCoreApplication.translate("MainWindow", u"Knockout", None))
        self.recordingGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Recording", None))
        self.recordingResolutionLabel.setText(QCoreApplication.translate("MainWindow", u"Resolution:", None))
        self.recordingFPSLabel.setText(QCoreApplication.translate("MainWindow", u"FPS:", None))
#if QT_CONFIG(tooltip)
        self.motionBlurcheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Forced to be disabled if star rating of the map is less than 5 stars.", None))
#endif // QT_CONFIG(tooltip)
        self.motionBlurcheckBox.setText(QCoreApplication.translate("MainWindow", u"Motion Blur", None))
        self.recordingEncoderLabel.setText(QCoreApplication.translate("MainWindow", u"Encoder:", None))
        self.recordingEncoderComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CPU", None))
        self.recordingEncoderComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"NVIDIA GPU (NVENC)", None))
        self.recordingEncoderComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"AMD GPU (VCE)", None))
        self.recordingEncoderComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Intel GPU (QSV)", None))
        self.recordingEncoderComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Customize", None))

        self.outputPathLabel.setText(QCoreApplication.translate("MainWindow", u"Output Path:", None))
        self.outputNameLabel.setText(QCoreApplication.translate("MainWindow", u"Output Name:", None))
#if QT_CONFIG(tooltip)
        self.outputNameLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"output name template tooltips", None))
#endif // QT_CONFIG(tooltip)
        self.localAudioOffsetLabel.setText(QCoreApplication.translate("MainWindow", u"Local Audio Offset:", None))
        self.encoderConfigGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Encoder Config Customize", None))
        self.videoCodecCustomizeLabel.setText(QCoreApplication.translate("MainWindow", u"Video Codec:", None))
        self.encoderOptionCustomizeLabel.setText(QCoreApplication.translate("MainWindow", u"Encoder Option:", None))
        self.presetCustomizeLabel.setText(QCoreApplication.translate("MainWindow", u"Preset:", None))
        self.audioCodecCustomizeLabel.setText(QCoreApplication.translate("MainWindow", u"Audio Codec:", None))
        self.audioOptionCustomizeLabel.setText(QCoreApplication.translate("MainWindow", u"Audio Option:", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.recordingSettings), QCoreApplication.translate("MainWindow", u"Recording", None))
        self.boundariesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Boundaries", None))
        self.boundariesShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.scoreGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Score", None))
        self.scoreShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.hpBarGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Hp Bar", None))
        self.hpBarShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.comboCounterGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Combo Counter", None))
        self.comboCounterShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.hitCounterGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Hit Counter", None))
        self.hitCounterShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.aimErrorMeterGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Aim Error Meter", None))
        self.aimErrorMeterShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.keyOverlayGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Key Overlay", None))
        self.keyOverlayShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.strainGraphGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Strain Graph", None))
        self.strainGraphShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.resultsScreenGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Results Screen", None))
        self.resultsScreenShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.resultsScreenUseLocalTimeZoneCheckBox.setText(QCoreApplication.translate("MainWindow", u"Use LocalTimeZone", None))
        self.resultsScreenTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.modsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mods", None))
        self.modsShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.modsHideInReplaysCheckBox.setText(QCoreApplication.translate("MainWindow", u"Hide In Replays", None))
        self.modsFoldInReplaysCheckBox.setText(QCoreApplication.translate("MainWindow", u"Fold In Replays", None))
        self.scoreBoardGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Score Board", None))
        self.scoreBoardShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.scoreBoardHideOthersCheckBox.setText(QCoreApplication.translate("MainWindow", u"Hide Others", None))
        self.scoreBoardShowAvatarsCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show Avatars", None))
        self.ppCounterGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"PP Counter", None))
        self.ppCounterShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.ppCounterUseLazerPPCheckBox.setText(QCoreApplication.translate("MainWindow", u"Use Lazer PP", None))
        self.inputGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.mouseButtonsDisabledCheckBox.setText(QCoreApplication.translate("MainWindow", u" Disable Mouse Buttons", None))
        self.leftKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Left:", None))
        self.restartKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Restart:", None))
        self.rightKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Right:", None))
        self.smokeKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Smoke:", None))
        self.hitErrorMeterGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Hit Error Meter", None))
        self.hitErrorMeterShowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
#if QT_CONFIG(tooltip)
        self.hitErrorMeterShowUnstableRateCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Only shows if hit error meter is enabled.", None))
#endif // QT_CONFIG(tooltip)
        self.hitErrorMeterShowUnstableRateCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show UR", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.gameplaySettings), QCoreApplication.translate("MainWindow", u"Gameplay", None))
        self.skinGeneralGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"General", None))
        self.useSkinColorsRadioButton.setText(QCoreApplication.translate("MainWindow", u"Use Skin Colors", None))
        self.useBeatmapColorsRadioButton.setText(QCoreApplication.translate("MainWindow", u"Use Beatmap Colors", None))
#if QT_CONFIG(tooltip)
        self.useSkinCursorCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"If disabled, Danser cursor will be used.", None))
#endif // QT_CONFIG(tooltip)
        self.useSkinCursorCheckBox.setText(QCoreApplication.translate("MainWindow", u"Use Skin Cursor", None))
        self.useSkinHitsoundsCheckBox.setText(QCoreApplication.translate("MainWindow", u"Use Skin Hitsounds", None))
        self.cursorGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Cursor", None))
        self.scaleToCSCheckBox.setText(QCoreApplication.translate("MainWindow", u"Scale To CS", None))
#if QT_CONFIG(tooltip)
        self.cursorRipplesCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Waves will appear below where the player clicked", None))
#endif // QT_CONFIG(tooltip)
        self.cursorRipplesCheckBox.setText(QCoreApplication.translate("MainWindow", u"Cursor Ripples", None))
        self.cursorSizeLabel.setText(QCoreApplication.translate("MainWindow", u"Cursor Size:", None))
        self.forceLongTrailCheckBox.setText(QCoreApplication.translate("MainWindow", u"Force Long Trail", None))
        self.longTrailDensityLabel.setText(QCoreApplication.translate("MainWindow", u"Long Trail Density:", None))
        self.longTrailLengthLabel.setText(QCoreApplication.translate("MainWindow", u"Long Trail Length:", None))
        self.cursorRainbowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Cursor Rainbow", None))
        self.cursorTrailGlowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Cursor Trail Glow", None))
        self.objectsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Objects", None))
#if QT_CONFIG(tooltip)
        self.drawFollowPointsCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"The lines between circles, basically", None))
#endif // QT_CONFIG(tooltip)
        self.drawFollowPointsCheckBox.setText(QCoreApplication.translate("MainWindow", u"Draw Follow Points", None))
#if QT_CONFIG(tooltip)
        self.drawComboNumbersCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"The number inside circles / sliders", None))
#endif // QT_CONFIG(tooltip)
        self.drawComboNumbersCheckBox.setText(QCoreApplication.translate("MainWindow", u"Draw Combo Numbers", None))
#if QT_CONFIG(tooltip)
        self.scaleToTheBeatCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Sliders and circles will bounce to the rhythm of the music", None))
#endif // QT_CONFIG(tooltip)
        self.scaleToTheBeatCheckBox.setText(QCoreApplication.translate("MainWindow", u"Scale To The Beat", None))
#if QT_CONFIG(tooltip)
        self.sliderMergeCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Merges sliders, can be nice for some type of maps but it is not something you'd see in osu!", None))
#endif // QT_CONFIG(tooltip)
        self.sliderMergeCheckBox.setText(QCoreApplication.translate("MainWindow", u"Slider Merge", None))
#if QT_CONFIG(tooltip)
        self.objectsRainbowCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Makes the sliders and circles rainbow! Enabling this will override \"Use skin combo colors\" and \"Use beatmap combo colors\"", None))
#endif // QT_CONFIG(tooltip)
        self.objectsRainbowCheckBox.setText(QCoreApplication.translate("MainWindow", u"Rainbow", None))
#if QT_CONFIG(tooltip)
        self.flashToTheBeatCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Sliders and circles will flash to the beat!", None))
#endif // QT_CONFIG(tooltip)
        self.flashToTheBeatCheckBox.setText(QCoreApplication.translate("MainWindow", u"Flash To The Beat", None))
        self.useHitCircleColorCheckBox.setText(QCoreApplication.translate("MainWindow", u"Use Hit Circle Color", None))
        self.sliderSnakingInCheckBox.setText(QCoreApplication.translate("MainWindow", u"Slider Snaking In", None))
        self.sliderSnakingOutCheckBox.setText(QCoreApplication.translate("MainWindow", u"Slider Snaking Out", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.skinSettings), QCoreApplication.translate("MainWindow", u"Skin", None))
        self.playfieldGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Play Field", None))
#if QT_CONFIG(tooltip)
        self.seizureWarningCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Can be nice if you upload the video to YouTube for example.", None))
#endif // QT_CONFIG(tooltip)
        self.seizureWarningCheckBox.setText(QCoreApplication.translate("MainWindow", u"Seizure Warning", None))
        self.loadStoryboardCheckBox.setText(QCoreApplication.translate("MainWindow", u"Load Storyboard", None))
        self.loadVideoCheckBox.setText(QCoreApplication.translate("MainWindow", u"Load Video", None))
        self.bgParallaxCheckBox.setText(QCoreApplication.translate("MainWindow", u"Background parallax", None))
        self.showDanserLogoCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show Danser Logo", None))
        self.skipIntroCheckBox.setText(QCoreApplication.translate("MainWindow", u"Skip Intro", None))
        self.quickStartCheckBox.setText(QCoreApplication.translate("MainWindow", u"Quick Start", None))
        self.backgroundDimGroupBox.setTitle(QCoreApplication.translate("MainWindow", u" Background dim", None))
        self.introBGDimLabel.setText(QCoreApplication.translate("MainWindow", u"Intro:", None))
        self.inGameBGDimLabel.setText(QCoreApplication.translate("MainWindow", u"In Game:", None))
        self.breakBGDimLabel.setText(QCoreApplication.translate("MainWindow", u"Break:", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.otherSettings), QCoreApplication.translate("MainWindow", u"Other", None))
        self.danserGuiDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"About Title", None))
        self.aboutMainMarkdownLabel.setText(QCoreApplication.translate("MainWindow", u"About Description", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.aboutPage), QCoreApplication.translate("MainWindow", u"About", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.settingsTab), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

