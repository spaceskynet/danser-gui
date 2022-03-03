#!/usr/bin/env python3
import consts
import logging, sys, traceback, platform, os
import ui.danserGuiRes as danserGuiRes
from autologging import traced, logged
from autologging import TRACE
from ui import *
from ui.bindKeyDialog import Ui_bindKeyDialog
from ui.MainWindow import Ui_MainWindow
from ui.debugModeWindow import Ui_debugModeWindow
from utils.config import DanserGUIConfig
from os.path import dirname, join, abspath, splitext, isfile
from utils.skin import get_skins
from utils.osrparser import get_latest_replay
from utils.beatmap import (find_beatmap_by_mapfile, find_beatmap_by_replay, parse_replay_file)
from utils.exec_wrapper import SongsDBUpdateThread, DanserExecByArgsThread, ReplayModifyThread
from utils.exception_handling import isEmptyWarning, customWarning, customError, customInfo

class ProgressDialog(QDialog):
    def __init__(self):
        super().__init__()
        if not self.objectName():
            self.setObjectName(u"progressDialog")
        self.resize(260, 60)
        gui_icon = QIcon()
        gui_icon.addFile(u":/assets/danser-gui.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(gui_icon)
        self.progressVerticalLayout = QVBoxLayout(self)
        self.progressVerticalLayout.setObjectName(u"progressVerticalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.leftTimeFormLayout = QFormLayout()
        self.leftTimeFormLayout.setObjectName(u"leftTimeFormLayout")
        self.leftTimeNameLabel = QLabel(self)
        self.leftTimeNameLabel.setObjectName(u"leftTimeNameLabel")

        self.leftTimeFormLayout.setWidget(0, QFormLayout.LabelRole, self.leftTimeNameLabel)

        self.leftTimeLabel = QLabel(self)
        self.leftTimeLabel.setObjectName(u"leftTimeLabel")
        self.leftTimeLabel.setText(u"*m*s")

        self.leftTimeFormLayout.setWidget(0, QFormLayout.FieldRole, self.leftTimeLabel)
        self.verticalLayout.addLayout(self.leftTimeFormLayout)

        self.leftProgressBar = QProgressBar(self)
        self.leftProgressBar.setObjectName(u"leftProgressBar")
        self.leftProgressBar.setValue(0)
        self.verticalLayout.addWidget(self.leftProgressBar)
        self.progressVerticalLayout.addLayout(self.verticalLayout)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.leftTimeNameLabel.setText(QCoreApplication.translate("MainWindow", u"Left time:", None))
    # retranslateUi

    def setDefault(self):
        self.leftTimeLabel.setText(u"*m*s")
        self.leftProgressBar.setValue(0)

class BindKeyUiDialog(Ui_bindKeyDialog):
    def __init__(self, bindKeyDialog):
        super().__init__()
        self.setupUi(bindKeyDialog)
                 
class BindKeyWindow(QDialog):
    setKey = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.Dialog = BindKeyUiDialog(self)
        gui_icon = QIcon()
        gui_icon.addFile(u":/assets/danser-gui.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(gui_icon)
        self.setWindowModality(Qt.ApplicationModal)
       
    def accept(self):
        if self.Dialog.inputKeyPushButtonIsDefault():
            customWarning(QCoreApplication.translate("bindKeyDialog", u"Please press the key you want to bind.", None))
            return
        self.setKey.emit(self.Dialog.inputKeyPushButton.text())
        return super().accept()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() != Qt.Key_Escape:
            self.Dialog.inputKeyPushButton.setText(event.text())
            return super().keyPressEvent(event)

class DanserDebugModeMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = Ui_debugModeWindow()
        self.MainWindow.setupUi(self)
        gui_icon = QIcon()
        gui_icon.addFile(u":/assets/danser-gui.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(gui_icon)
        window_width, window_height = 400, 400

        self.setMinimumSize(400, 400)
        self.default_width, self.default_height = window_width, window_height

        self.show()

@logged(logging.getLogger(__name__))
@traced
class DanserUiMainWindow(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().__init__()
        self.setupUi(MainWindow)
        self.gui_config = MainWindow.gui_config
        self.rewriteClassesInit()

        self.trans = QTranslator(MainWindow)
        self.setLanguage(MainWindow)

        self.songsDBUpdateThread = SongsDBUpdateThread()
        self.songsDBUpdateThread.started.connect(self.songsDBUpdateEventStarted)
        self.songsDBUpdateThread.finished.connect(self.songsDBUpdateEventFinished)

        self.progressDialog = ProgressDialog()
        
        self.danserExecByArgsThread = DanserExecByArgsThread(self.progressDialog)
        self.danserExecByArgsThread.started.connect(self.startDanserByArgumentsEventStarted)
        self.danserExecByArgsThread.finished.connect(self.startDanserByArgumentsEventFinished)

        self.replayModifyThread = ReplayModifyThread()
        self.replayModifyThread.started.connect(self.replayModifyEventStarted)
        self.replayModifyThread.finished.connect(self.replayModifyEventFinished)

        self.openKnockoutReplaysFolderPushButton.clicked.connect(self.openKnockoutReplaysFolder)

        self.graphicsWidth.setValidator(QIntValidator(self.graphicsWidth))
        self.graphicsHeight.setValidator(QIntValidator(self.graphicsHeight))
        self.recordingWidth.setValidator(QIntValidator(self.recordingWidth))
        self.recordingHeight.setValidator(QIntValidator(self.recordingHeight))
        self.outputNameLineEdit.setValidator(QRegExpValidator(QRegExp("^[^\/:*?""<>|]+$"))) # ?

        self.recordingEncoderComboBox.activated[int].connect(self.encoderConfigGroupBoxEnabled)

        self.danserModeComboBox.activated[str].connect(lambda section:(self.generalSettingEnabled(section, MainWindow)))
        self.skinsComboBoxInit()
        self.osuSelectButton.clicked.connect(lambda: (self.osuSelectButtonClicked(MainWindow)))
        self.osrSelectButton.clicked.connect(lambda: (self.osrSelectButtonClicked(MainWindow)))
        self.osuPathLineEdit.clicked.connect(lambda: (self.osuSelectButtonClicked(MainWindow)))
        self.osrPathLineEdit.clicked.connect(lambda: (self.osrSelectButtonClicked(MainWindow)))
        self.isRecordCheckBox.clicked.connect(self.recordingGroupBox.setEnabled)

        self.songsPathLineEdit.clicked.connect(lambda: (self.songsPathLineEditClicked(MainWindow)))
        self.skinsPathLineEdit.clicked.connect(lambda: (self.skinsPathLineEditClicked(MainWindow)))
        self.danserPathLineEdit.clicked.connect(lambda: (self.danserPathLineEditClicked(MainWindow)))
        self.outputPathLineEdit.clicked.connect(lambda: (self.outputPathLineEditClicked(MainWindow)))
        self.songsDBUpdatePushButton.clicked.connect(lambda: (self.songsDBUpdateEvent(MainWindow)))

        self.modifyOsrMD5CheckBox.clicked.connect(self.replayModifyWarningEvent)
        self.addDateAfterPlayerNamecheckBox.clicked.connect(self.replayModifyWarningEvent)

        self.leftKeyPushButton.clicked.connect(lambda: (self.bindKeyEvent(self.leftKeyPushButton)))
        self.rightKeyPushButton.clicked.connect(lambda: (self.bindKeyEvent(self.rightKeyPushButton)))
        self.restartKeyPushButton.clicked.connect(lambda: (self.bindKeyEvent(self.restartKeyPushButton)))
        self.smokeKeyPushButton.clicked.connect(lambda: (self.bindKeyEvent(self.smokeKeyPushButton)))

        self.songsDBModeComboBox.activated.connect(lambda: (self.songsDBModeComboBoxChanged(MainWindow)))
        self.languageComboBox.activated.connect(lambda: (self.languageComboBoxChanged(MainWindow)))

        self.mainTabWidget.currentChanged.connect(lambda: (self.syncGuiConfigWithMainWindow(MainWindow)))
        self.settingsTabWidget.currentChanged.connect(lambda: (self.syncGuiConfigWithMainWindow(MainWindow)))

        self.startLogo.clicked.connect(lambda: (self.startDanserByArgumentsEvent(MainWindow)))
        self.startLogo.setStyleSheet("QLabel {background-color: transparent;}")
        self.danserGuiLogoPixmap = QPixmap(u":/assets/danser-gui.png")
        self.startLogo.setPixmap(self.danserGuiLogoPixmap)
        self.startLogo.setScaledContents(True)

        self.danserGuiLogo.setPixmap(self.danserGuiLogoPixmap)
        self.danserGuiLogo.setScaledContents(True)

    def rewriteClassesInit(self):
        self.cursorSizeSlider.setMinimum(0.1)
        self.cursorSizeSlider.setMaximum(2)
        self.cursorSizeSlider.setSingleStep(0.01)
        self.cursorSizeSlider.setPageStep(0.5)
        self.cursorSizeSlider.setValue(1)
        self.cursorSizeSlider.setTickInterval(0.1)

        self.knockoutCursorSizeSlider.setMinimum(0.1)
        self.knockoutCursorSizeSlider.setMaximum(2)
        self.knockoutCursorSizeSlider.setSingleStep(0.01)
        self.knockoutCursorSizeSlider.setPageStep(0.5)

        self.CSHorizontalSlider.setSingleStep(0.01)
        self.ARHorizontalSlider.setSingleStep(0.01)
        self.ODHorizontalSlider.setSingleStep(0.01)
        self.HPHorizontalSlider.setSingleStep(0.01)

        self.setTimingRangeSlider(60)

        self.beatmapSpeedDoubleSpinBox.setValue(1)
        self.beatmapPitchDoubleSpinBox.setValue(1)

    def setTimingRangeSlider(self, songs_length):
        self.timingRangeSlider.setMinimum(0)
        self.timingRangeSlider.setMaximum(songs_length)
        self.timingRangeSlider.setValue((0, songs_length))
        
    def checkWidgetsIsEnabled(self, MainWindow):
        self.generalSettingEnabled(self.danserModeComboBox.currentText(), MainWindow)
        self.recordingGroupBox.setEnabled(self.isRecordCheckBox.isEnabled() and self.isRecordCheckBox.isChecked())
        self.encoderConfigGroupBoxEnabled(self.recordingEncoderComboBox.currentIndex())

        self.resultsScreenUseLocalTimeZoneCheckBox.setEnabled(self.resultsScreenShowCheckBox.isChecked())
        self.resultsScreenTimeSpinBox.setEnabled(self.resultsScreenShowCheckBox.isChecked())
        self.modsHideInReplaysCheckBox.setEnabled(self.modsShowCheckBox.isChecked())
        self.modsFoldInReplaysCheckBox.setEnabled(self.modsShowCheckBox.isChecked())
        self.scoreBoardHideOthersCheckBox.setEnabled(self.scoreBoardShowCheckBox.isChecked())
        self.scoreBoardShowAvatarsCheckBox.setEnabled(self.scoreBoardShowCheckBox.isChecked())
        self.hitErrorMeterShowUnstableRateCheckBox.setEnabled(self.hitErrorMeterShowCheckBox.isChecked())

        self.longTrailDensitySpinBox.setEnabled(self.forceLongTrailCheckBox.isChecked())
        self.longTrailLengthSpinBox.setEnabled(self.forceLongTrailCheckBox.isChecked())
        
        self.cursorsInMirrorCollageSpinBox.setEnabled(self.cursorsInMirrorCollageCheckBox.isChecked())
        self.cursorsInTagModeSpinBox.setEnabled(self.cursorsInTagModeCheckBox.isChecked())
        self.skipIntroCheckBox.setChecked(self.quickStartCheckBox.isChecked())

        self.danserNameLineEdit.setEnabled(self.addDanserCheckBox.isChecked())
        self.dateFormatComboBox.setEnabled(self.addDateAfterPlayerNamecheckBox.isChecked())

    def checkSongsDBIsExists(self, MainWindow):
        songs_db_mode, songs_db_path = self.getSongsDBModeAndPath()
        if songs_db_mode == 'osu!':
            exist = isfile(join(songs_db_path, 'osu!.sqlite3.db'))
        else:
            exist = isfile(join(songs_db_path, 'danser.db'))
        if not exist:
            customError(QCoreApplication.translate("MainWindow", u"Please update songs db at first!", None))
            self.songsDBUpdateEvent(MainWindow)
        return exist

    def checkWidgetsValueIsValid(self):
        danser_mode = self.danserModeComboBox.currentText()

        if not self.songsPathLineEdit.text():
            return (False, isEmptyWarning(QCoreApplication.translate("MainWindow", u"Songs Path", None)))
        if not self.skinsPathLineEdit.text():
            return (False, isEmptyWarning(QCoreApplication.translate("MainWindow", u"Skins Path", None)))
        if not self.danserPathLineEdit.text():
            return (False, isEmptyWarning(QCoreApplication.translate("MainWindow", u"danser Path", None)))
        if not self.graphicsWidth.text() or not self.graphicsHeight.text():
            return (False, isEmptyWarning(QCoreApplication.translate("MainWindow", u"Graphics Resolution", None)))
        
        if not self.osuPathLineEdit.text():
            return (False, isEmptyWarning(QCoreApplication.translate("MainWindow", u"Beatmap(.osu) path", None)))
        
        if danser_mode == 'replay':
            if not self.osrPathLineEdit.text():
                return (False, isEmptyWarning(QCoreApplication.translate("MainWindow", u"Replay(.osr) path", None)))
            
        is_record = self.isRecordCheckBox.isChecked() and danser_mode != 'play'
        if is_record:
            if not self.outputPathLineEdit.text():
                return (False, isEmptyWarning(QCoreApplication.translate("MainWindow", u"Output Path", None)))
            if not self.outputNameLineEdit.text():
                return (False, isEmptyWarning(QCoreApplication.translate("MainWindow", u"Output Name", None)))
            if not self.recordingHeight.text() or not self.recordingWidth.text():
                return (False, isEmptyWarning(QCoreApplication.translate("MainWindow", u"Recording Resolution", None)))

        start, end = self.timingRangeSlider.value()
        if end < 12: # danser -> panic: runtime error: index out of range [1] with length 1
            return (False, customWarning(QCoreApplication.translate("MainWindow", u"end time must greater than 12", None)))

        return (True, None)

    def bindKeyEvent(self, bindPushButton):
        bind_key_window = BindKeyWindow()
        bind_key_window.setKey.connect(bindPushButton.setText)
        bind_key_window.show()
        bind_key_window.exec_()

    def generateArgumentsByGuiConfig(self, MainWindow):
        self.syncDanserConfigWithGuiConfig(MainWindow)
        config = self.gui_config
        songs_db_mode, songs_db_path = self.getSongsDBModeAndPath()
        danser_mode = self.danserModeComboBox.currentText()
        if danser_mode == 'replay':
            replay_path = self.osrPathLineEdit.text()
            replay = parse_replay_file(replay_path)
        arguments = [] 
        arguments.append('-noupdatecheck') # skips checking GitHub for a newer version of danser
        arguments.append('-nodbcheck') # skips updating the database with new, changed or deleted maps

        # Skip Intro & Quick Start
        if self.quickStartCheckBox.isChecked():
            arguments.append("-quickstart")
        elif self.skipIntroCheckBox.isChecked():
            arguments.append("-skip")

        # Beatmap Arguments
        beatmap_path = self.osuPathLineEdit.text()
        beatmap = find_beatmap_by_mapfile(beatmap_path, songs_db_path, songs_db_mode)
        arguments.append(f'-md5={beatmap.MD5}')
        
        # Output File Name
        isRecord = self.isRecordCheckBox.isChecked() and danser_mode != 'play'
        if isRecord:
            output_file_name = self.outputNameLineEdit.text()
            # {Player} - {Artist}[{Creator}] - {MapTitle}[Difficulty].mp4
            game_mode_map = ['std', 'taiko', 'ctb', 'mania']
            replace_map = {
                            '{Player}': self.usernameLineEdit.text() if danser_mode != 'replay' else replay.username,
                            '{Artist}': beatmap.Artist,
                            '{ArtistUnicode}': beatmap.ArtistUnicode,
                            '{MapTitle}': beatmap.MapTitle,
                            '{MapTitleUnicode}': beatmap.MapTitleUnicode,
                            '{Creator}': beatmap.Creator,
                            '{Difficulty}': beatmap.Difficulty,
                            '{GameMode}': game_mode_map[beatmap.GameMode],
                            '{CS}': str(beatmap.CS),
                            '{AR}': str(beatmap.AR),
                            '{HP}': str(beatmap.HP),
                            '{OD}': str(beatmap.OD),
                            '{TotalTime}': str(beatmap.TotalTime // 1000), # ms
                            '{MapID}': str(beatmap.MapID),
                            '{SetID}': str(beatmap.SetID),
                            '{MD5}': beatmap.MD5,
                        }
            invalid_filename_char = r'\/<>?*|:"'
            for replace_pair in replace_map.items():
                output_file_name = output_file_name.replace(*replace_pair)
            for c in invalid_filename_char:
                output_file_name = output_file_name.replace(c, '_')
            output_file_name = splitext(output_file_name)[0]
            logging.info(f"[GUI] Output file name: {output_file_name}")
            if MainWindow.debug: MainWindow.danserUiDebugModeWindow.recordingOutputNameLineEdit.setText(output_file_name)
            arguments.append('-out'), arguments.append(f'{output_file_name}')
        
        # Timing
        start_time, end_time = self.timingRangeSlider.value()
        if start_time != self.timingRangeSlider.minimum(): arguments.append(f"-start={start_time}")
        if end_time != self.timingRangeSlider.maximum(): arguments.append(f"-end={end_time}")

        # Beatmap Attributes
        danser_mode_fit = danser_mode == 'danser' or danser_mode == 'play'
        if danser_mode_fit and self.customizeBeatmapAttributesCheckBox.isChecked():
            customize_CS = self.CSHorizontalSlider.value()
            customize_AR = self.ARHorizontalSlider.value()
            customize_HP = self.HPHorizontalSlider.value()
            customize_OD = self.ODHorizontalSlider.value()

            if beatmap.CS != customize_CS: arguments.append(f"-cs={round(customize_CS, 2)}")
            if beatmap.AR != customize_AR: arguments.append(f"-ar={round(customize_AR, 2)}")
            if beatmap.HP != customize_HP: arguments.append(f"-hp={round(customize_HP, 2)}")
            if beatmap.OD != customize_OD: arguments.append(f"-od={round(customize_OD, 2)}")

        # Beatmap Speed And Pitch
        beatmap_speed, beatmap_pitch = self.beatmapSpeedDoubleSpinBox.value(), self.beatmapPitchDoubleSpinBox.value()
        if beatmap_speed != 1.0: arguments.append(f"-speed={beatmap_speed}")
        if beatmap_pitch != 1.0: arguments.append(f"-pitch={beatmap_pitch}")

        # Beatmap Special
        if self.cursorsInMirrorCollageCheckBox.isChecked():
            arguments.append(f"-cursors={self.cursorsInMirrorCollageSpinBox.value()}")
        if self.cursorsInTagModeCheckBox.isEnabled() and self.cursorsInTagModeCheckBox.isChecked():
            arguments.append(f"-tag={self.cursorsInTagModeSpinBox.value()}")

        # Beatmap Mods
        if danser_mode != 'replay' and danser_mode != 'knockout':
            mods_combination = ""
            if self.SDPFCheckBox.checkState() == Qt.PartiallyChecked: mods_combination += "SD"
            if self.SDPFCheckBox.checkState() == Qt.Checked: mods_combination += "PF"
            if self.NFCheckBox.isChecked(): mods_combination += "NF"
            if self.HDCheckBox.isChecked(): mods_combination += "HD"
            if self.FLCheckBox.isChecked(): mods_combination += "FL"
            if self.DTNCCheckBox.checkState() == Qt.PartiallyChecked: mods_combination += "DT"
            if self.DTNCCheckBox.checkState() == Qt.Checked: mods_combination += "NC"
            if self.HTCheckBox.isChecked(): mods_combination += "HT"
            if self.EZHRCheckBox.checkState() == Qt.PartiallyChecked: mods_combination += "EZ"
            if self.EZHRCheckBox.checkState() == Qt.Checked: mods_combination += "HR"
            if mods_combination: arguments.append(f"-mods={mods_combination}")

        if danser_mode == 'danser':
            pass
        elif danser_mode == 'knockout':
            arguments.append('-knockout')
        elif danser_mode == 'play':
            arguments.append('-play')
        else:
            arguments.append('-replay'), arguments.append(f'{replay_path}')

        logging.info(f"[GUI] Danser execute arguments: {arguments}")
        if MainWindow.debug: MainWindow.danserUiDebugModeWindow.currentDanserExecArgumentsLineEdit.setText(str(arguments))
        return arguments, isRecord

    def startDanserByArgumentsEvent(self, MainWindow):
        passed, warning_widget = self.checkWidgetsValueIsValid()
        if not passed: return
        arguments, is_record = self.generateArgumentsByGuiConfig(MainWindow)
        root_path = self.gui_config.General.DanserRootDir
        self.danserExecByArgsThread.init(root_path, arguments, is_record)
        is_knockout = self.danserModeComboBox.currentText() == 'knockout'
        is_modify_beatmap_hash = self.modifyOsrMD5CheckBox.isChecked()
        is_add_date = self.addDateAfterPlayerNamecheckBox.isChecked()
        if is_knockout and (is_modify_beatmap_hash or is_add_date):
            self.replayModifyEvent(MainWindow, is_modify_beatmap_hash, is_add_date)
        else:
            self.danserExecByArgsThread.start()
        if is_record:
            self.progressDialog.setDefault()
            self.danserExecByArgsThread.setProgressValue.connect(self.setProgressDialogValue)
            self.progressDialog.show()
            self.progressDialog.exec_()

    def setProgressDialogValue(self, group):
        process, speed, eta = group
        self.progressDialog.leftProgressBar.setValue(int(process))
        self.progressDialog.leftTimeLabel.setText(eta)

    def startDanserByArgumentsEventStarted(self):
        logging.info("[GUI] startDanserByArgumentsEvent Started")
        self.startLogo.setDisabled(True)

    def startDanserByArgumentsEventFinished(self):
        logging.info("[GUI] startDanserByArgumentsEvent Finished")
        if self.danserExecByArgsThread.is_record:
            self.progressDialog.close()
            customInfo(QCoreApplication.translate("MainWindow", u"rendering complete!", None))
        self.startLogo.setEnabled(True)

    def replayModifyWarningEvent(self, checked):
        if not checked: return
        customWarning(QCoreApplication.translate("MainWindow", u"please note that the operation is irreversible, this will modify all osr files in the replays directory! Remember to backup osr files at first!", None))

    def openKnockoutReplaysFolder(self, checked):
        if not self.danserPathLineEdit.text():
            isEmptyWarning(QCoreApplication.translate("MainWindow", u"danser Path", None))
            return
        danser_replays_path = join(self.danserPathLineEdit.text(), 'replays')
        if platform.system()  == 'Windows':
            os.startfile(danser_replays_path)
        else:
            os.system(f"xdg-open {danser_replays_path}")

    def replayModifyEvent(self, MainWindow, is_modify_beatmap_hash, is_add_date):
        root_path = self.gui_config.General.DanserRootDir
        beatmap_hash, date_format_index = None, None
        if is_modify_beatmap_hash:
            songs_db_mode, songs_db_path = self.getSongsDBModeAndPath()
            if not self.checkSongsDBIsExists(MainWindow): return
            beatmap = find_beatmap_by_mapfile(self.osuPathLineEdit.text(), songs_db_path, songs_db_mode)
            beatmap_hash = beatmap.MD5
        if is_add_date:
            date_format_index = self.dateFormatComboBox.currentIndex()
        self.replayModifyThread.init(root_path, beatmap_hash, date_format_index)
        self.replayModifyThread.start()

    def replayModifyEventStarted(self):
        logging.info("[GUI] replayModifyEvent Started")
        self.startLogo.setDisabled(True)

    def replayModifyEventFinished(self):
        logging.info("[GUI] replayModifyEvent Finished")
        customInfo(QCoreApplication.translate("MainWindow", u"replay files is completely modified!", None))        
        self.startLogo.setEnabled(True)
        self.danserExecByArgsThread.start()

    def syncGuiConfigWithMainWindow(self, MainWindow):
        MainWindow.setConfigByMainWindow()
        MainWindow.dansergui_settings.write()
        logging.info("[GUI] sync GuiConfig With MainWindow Done!")
    
    def syncDanserConfigWithGuiConfig(self, MainWindow):
        self.syncGuiConfigWithMainWindow(MainWindow)
        MainWindow.dansergui_settings.sync()
        MainWindow.dansergui_settings.danser_config.write()
        logging.info("[GUI] sync Danser Config With GuiConfig Done!")

    def getSongsDBModeAndPath(self):
        songs_db_mode = self.gui_config.General.SongsDBMode
        if songs_db_mode == 'osu!':
            songs_db_path = consts.root_path
        else:
            songs_db_path = self.gui_config.General.DanserRootDir
        return songs_db_mode, songs_db_path

    def encoderConfigGroupBoxEnabled(self, index):
        self.encoderConfigGroupBox.setEnabled(index + 1 == self.recordingEncoderComboBox.count())
    
    def generalSettingEnabled(self, section, MainWindow):
        if section != 'replay':
            self.osuSelectButton.setEnabled(True)
            self.osuPathLineEdit.setEnabled(True)
            self.osrSelectButton.setEnabled(False)
            self.osrPathLineEdit.setEnabled(False)
            self.beatmapModsGroupBox.setEnabled(True)
        else:
            self.osuSelectButton.setEnabled(False)
            self.osuPathLineEdit.setEnabled(False)
            self.osrSelectButton.setEnabled(True)
            self.osrPathLineEdit.setEnabled(True)
            self.beatmapModsGroupBox.setEnabled(False)

        if section != 'play':
            self.isRecordCheckBox.setEnabled(True)
            self.recordingGroupBox.setEnabled(self.isRecordCheckBox.isChecked()) # !
        else:
            self.isRecordCheckBox.setEnabled(False)
            self.recordingGroupBox.setEnabled(False)

        if section != 'danser':
            self.cursorsInTagModeCheckBox.setEnabled(False)
            self.cursorsInTagModeSpinBox.setEnabled(False)
        else:
            self.cursorsInTagModeCheckBox.setEnabled(True)
            self.cursorsInTagModeSpinBox.setEnabled(self.cursorsInTagModeCheckBox.isChecked())

        if section != 'play' and section != 'danser':
            self.customizeBeatmapAttributesCheckBox.setEnabled(False)
            self.beatmapAttributesGroupBox.setEnabled(False)
        else:
            self.customizeBeatmapAttributesCheckBox.setEnabled(True)
            self.beatmapAttributesGroupBox.setEnabled(self.customizeBeatmapAttributesCheckBox.isChecked())

        if section != 'knockout':
            self.knockoutGeneralGroupBox.setEnabled(False)
            self.excludeModsGroupBox.setEnabled(False)
            self.hideModsGroupBox.setEnabled(False)
            self.experimentalFeaturesGroupBox.setEnabled(False)
        else:
            self.knockoutGeneralGroupBox.setEnabled(True)
            self.excludeModsGroupBox.setEnabled(True)
            self.hideModsGroupBox.setEnabled(True)
            self.experimentalFeaturesGroupBox.setEnabled(True)

        songs_db_mode, songs_db_path = self.getSongsDBModeAndPath()
        if section == 'replay':
            self.osrPathLineEdit.setText("")
            if songs_db_mode != 'osu!': return
            osu_root_path = dirname(self.gui_config.General.OsuSongsDir)
            lastest_replay_path = get_latest_replay(osu_root_path)
            if lastest_replay_path:
                self.osrPathLineEdit.setText(abspath(lastest_replay_path))
                if not self.checkSongsDBIsExists(MainWindow): return
                beatmap = find_beatmap_by_replay(lastest_replay_path, songs_db_path, songs_db_mode)
                if not self.setBeatmap(beatmap):
                    self.osuPathLineEdit.setText("")
            else:
                customWarning(QCoreApplication.translate("MainWindow", u"no recent replay, please pick a replay yourself!", None))
    
    def setBeatmap(self, beatmap):
        if not beatmap:
            customWarning(QCoreApplication.translate("MainWindow", u"no such beatmap, maybe you need update db or download beatmap from internet or place the beatmap file in the right songs folder!", None))
            return False
        if beatmap.GameMode != 0:
            customWarning(QCoreApplication.translate("MainWindow", u"danser only support std map!", None))
            return False

        osu_file_path = abspath(join(self.gui_config.General.OsuSongsDir, beatmap.FolderName, beatmap.MapFile))
        logging.info(f"[GUI] Chosen osu file: {osu_file_path}")

        self.osuPathLineEdit.setText(osu_file_path)

        song_length = beatmap.TotalTime // 1000
        self.timingRangeSlider.setMaximum(song_length)
        self.timingRangeSlider.setValue((0, song_length))

        self.CSHorizontalSlider.setValue(beatmap.CS)
        self.ARHorizontalSlider.setValue(beatmap.AR)
        self.HPHorizontalSlider.setValue(beatmap.HP)
        self.ODHorizontalSlider.setValue(beatmap.OD)
        return True

    def skinsComboBoxInit(self):
        osu_skins_path, skin_name = self.gui_config.General.OsuSkinsDir, self.gui_config.Skin.CurrentSkin
        skins_list = get_skins(osu_skins_path)
        self.skinsComboBox.addItems(skins_list)
        if not skin_name:
            skin_name = "default"
        self.skinsComboBox.setCurrentIndex(self.skinsComboBox.findText(skin_name))

    def osuSelectButtonClicked(self, MainWindow):
        osu_file_path, osu_file_type = QFileDialog.getOpenFileName(MainWindow, QCoreApplication.translate("MainWindow", u"Choose osu beatmap file", None), self.gui_config.General.OsuSongsDir, "osu beatmap file(*.osu)")
        songs_db_mode, songs_db_path = self.getSongsDBModeAndPath()
        if not osu_file_path: return
        if not self.checkSongsDBIsExists(MainWindow): return
        beatmap = find_beatmap_by_mapfile(osu_file_path, songs_db_path, songs_db_mode)
        if not self.setBeatmap(beatmap):
            pass
    
    def osrSelectButtonClicked(self, MainWindow):
        songs_db_mode, songs_db_path = self.getSongsDBModeAndPath()
        osu_replay_path = dirname(self.gui_config.General.OsuSongsDir)
        if songs_db_mode == 'osu!':
            osu_replay_path = join(osu_replay_path, "Replays")
        osr_file_path, osr_file_type = QFileDialog.getOpenFileName(MainWindow, QCoreApplication.translate("MainWindow", u"Choose osu replay file", None), osu_replay_path, "osu replay file(*.osr)")

        if osr_file_path:
            logging.info(f"[GUI] Chosen osr file: {osr_file_path}")
            self.osrPathLineEdit.setText(abspath(osr_file_path))
            if not self.checkSongsDBIsExists(MainWindow): return
            beatmap = find_beatmap_by_replay(osr_file_path, songs_db_path, songs_db_mode)
            if not self.setBeatmap(beatmap):
                self.osuPathLineEdit.setText("")
        else:
            pass

    def songsPathLineEditClicked(self, MainWindow):
        songs_db_mode, songs_db_path = self.getSongsDBModeAndPath()
        if songs_db_mode == 'osu!':
            start_path = self.gui_config.General.OsuRootDir
        else:
            start_path = consts.root_path
        songs_path = QFileDialog.getExistingDirectory(MainWindow, QCoreApplication.translate("MainWindow", u"Choose osu songs folder", None), start_path)
        if songs_path:
            self.songsPathLineEdit.setText(abspath(songs_path))
        else:
            pass
    
    def skinsPathLineEditClicked(self, MainWindow):
        songs_db_mode, songs_db_path = self.getSongsDBModeAndPath()
        if songs_db_mode == 'osu!':
            start_path = self.gui_config.General.OsuRootDir
        else:
            start_path = consts.root_path
        skins_path = QFileDialog.getExistingDirectory(MainWindow, QCoreApplication.translate("MainWindow", u"Choose osu skins folder", None), start_path)
        if skins_path:
            self.skinsPathLineEdit.setText(abspath(skins_path))
        else:
            pass

    def danserPathLineEditClicked(self, MainWindow):
        start_path = consts.root_path
        danser_path = QFileDialog.getExistingDirectory(MainWindow, QCoreApplication.translate("MainWindow", u"Choose danser root folder", None), start_path)
        if danser_path:
            self.danserPathLineEdit.setText(abspath(danser_path))
            MainWindow.dansergui_settings.danser_config.__init__(abspath(join(danser_path, consts.danser_config_path)))
        else:
            pass

    def outputPathLineEditClicked(self, MainWindow):
        start_path = consts.root_path
        output_path = QFileDialog.getExistingDirectory(MainWindow, QCoreApplication.translate("MainWindow", u"Choose danser record video output folder", None), start_path)
        if output_path:
            self.outputPathLineEdit.setText(abspath(output_path))
        else:
            pass
    
    def songsDBUpdateEvent(self, MainWindow):
        songs_db_mode, songs_db_path = self.getSongsDBModeAndPath()
        if songs_db_mode == 'osu!':
            self.syncGuiConfigWithMainWindow(MainWindow)
            root_path = self.gui_config.General.OsuRootDir
        else:
            self.syncDanserConfigWithGuiConfig(MainWindow)
            root_path = self.gui_config.General.DanserRootDir
        self.songsDBUpdateThread.init(songs_db_mode, root_path)
        # self.songsDBUpdateEventStarted()
        self.songsDBUpdateThread.start()

    def songsDBUpdateEventStarted(self):
        logging.info("[GUI] songsDBUpdateEvent Started")
        # self.songsDBGridLayout.setEnabled(False)
        self.songsDBModeComboBox.setDisabled(True)
        self.songsDBUpdatePushButton.setDisabled(True)

    def songsDBUpdateEventFinished(self):
        logging.info("[GUI] songsDBUpdateEvent Finished")
        # self.songsDBGridLayout.setEnabled(True)
        self.songsDBModeComboBox.setEnabled(True)
        self.songsDBUpdatePushButton.setEnabled(True)
        customInfo(QCoreApplication.translate("MainWindow", u"songs db is updated successfully!", None))

    def songsDBModeComboBoxChanged(self, MainWindow):
        self.gui_config.General.SongsDBMode = self.songsDBModeComboBox.currentText()
        self.songsDBUpdateEvent(MainWindow)
    
    def setLanguage(self, MainWindow):
        if self.gui_config.General.Language == 0:
            self.trans.load(join(consts.langs_path, 'en-US'))
        else:
            self.trans.load(join(consts.langs_path, 'zh-CN'))
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(MainWindow)

    def languageComboBoxChanged(self, MainWindow):
        self.gui_config.General.Language = self.languageComboBox.currentIndex()
        self.setLanguage(MainWindow)

class DanserMainWindow(QMainWindow):
    closed = pyqtSignal()
    def __init__(self, App, execpath, debug=False):
        super().__init__()
        self.App = App
        self.execpath = execpath
        self.debug = debug
        self.old_hook = sys.excepthook
        sys.excepthook = self.catch_exceptions

        logging.basicConfig(level=TRACE, filename=consts.LogPath.app, filemode="w", format="%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s")
        if debug:
            self.danserDebugModeMainWindow = DanserDebugModeMainWindow()
            self.danserUiDebugModeWindow = self.danserDebugModeMainWindow.MainWindow
            logging.getLogger().addHandler(self.danserUiDebugModeWindow.fullLogPlainTextEdit)
            self.closed.connect(self.danserDebugModeMainWindow.close)

        self.dansergui_settings = DanserGUIConfig()
        self.gui_config = self.dansergui_settings.config

        self.MainWindow = DanserUiMainWindow(self)

        gui_icon = QIcon()
        gui_icon.addFile(u":/assets/danser-gui.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(gui_icon)


        # avoid logging api key
        logging.info("[GUI] Current settings is updated to: {}".format(self.dansergui_settings.no_api_config()))

        self.setMainWindowByConfig()
        self.MainWindow.checkWidgetsIsEnabled(self)

        self.setFocus()
        # self.setWindowTitle("Danser GUI")

        windows_width, windows_height = 704, 396
        linux_width, linux_height = 848, 477 

        if platform.system() == 'Windows':
            self.default_width, self.default_height = windows_width, windows_height
        else:
            self.default_width, self.default_height = linux_width, linux_height
            self.setMinimumSize(self.default_width, self.default_height)
            self.resize(self.default_width, self.default_height)
        self.show()
	
    def catch_exceptions(self, ty, value, traceback_object):
        traceback_format = traceback.format_exception(ty, value, traceback_object)
        traceback_string = "".join(traceback_format)
        customError(traceback_string)
        self.old_hook(ty, value, traceback_object)

    def closeEvent(self, a0: QCloseEvent):
        self.MainWindow.syncGuiConfigWithMainWindow(self)
        self.closed.emit()
        return super().closeEvent(a0)

    def splitModesToSetMainWindow(self, MainWindow, choice):
        modes = ["SD","PF","NF","HD","FL","DT","NC","HT","EZ","HR","V2","AT","RX","AP","TD","SO",]
        modes_string = self.gui_config.Knockout.ExcludeMods if choice == 'exclude' else self.gui_config.Knockout.HideMods
        modes_string = modes_string[:len(modes_string) // 2 * 2] # ignore odd length string
        for i in range(0, len(modes_string), 2):
            mode = modes_string[i : i + 2]
            if mode in modes:
                eval(f"MainWindow.{choice}Mods{mode}CheckBox.setChecked(True)")

    def mergeModesToSetConfig(self, MainWindow, choice):
        modes = ["SD","PF","NF","HD","FL","DT","NC","HT","EZ","HR","V2","AT","RX","AP","TD","SO",]
        modes_string = ""
        for mode in modes:
            is_checked = eval(f"MainWindow.{choice}Mods{mode}CheckBox.isChecked()")
            if is_checked:
                modes_string += mode
        if choice == 'exclude':
            self.gui_config.Knockout.ExcludeMods = modes_string
        else:
            self.gui_config.Knockout.HideMods = modes_string

    def updateConfigByDefault(self):
        config, default_config = self.gui_config, self.dansergui_settings.default_config
        if config.Knockout is None: 
            config.Knockout = default_config.Knockout
        if config.Playfield.QuickStart is None:
            config.Playfield.QuickStart = default_config.Playfield.QuickStart
            config.Playfield.SkipIntro = default_config.Playfield.SkipIntro

    def setMainWindowByConfig(self):
        self.updateConfigByDefault()
        MainWindow, config = self.MainWindow, self.gui_config

        # Settings
        ## General
        MainWindow.usernameLineEdit.setText(config.Gameplay.PlayUsername)
        if config.General.SongsDBMode == 'osu!':
            MainWindow.songsDBModeComboBox.setCurrentIndex(0)
        else:
            MainWindow.songsDBModeComboBox.setCurrentIndex(1)
        MainWindow.songsPathLineEdit.setText(abspath(config.General.OsuSongsDir))
        MainWindow.skinsPathLineEdit.setText(abspath(config.General.OsuSkinsDir))
        MainWindow.danserPathLineEdit.setText(abspath(config.General.DanserRootDir))
        MainWindow.danserModeComboBox.setCurrentIndex(abs(MainWindow.danserModeComboBox.findText(config.General.DanserMode))) # if toml is modified to be invalid
        MainWindow.isRecordCheckBox.setChecked(config.General.IsRecord)
        MainWindow.osuApiLineEdit.setText(config.General.OsuApi)
        MainWindow.languageComboBox.setCurrentIndex(config.General.Language)
        
        ## Graphics
        MainWindow.graphicsWidth.setText(str(config.Graphics.Width))
        MainWindow.graphicsHeight.setText(str(config.Graphics.Height))
        MainWindow.fullScreenCheckBox.setChecked(config.Graphics.Fullscreen)
        MainWindow.vsyncCheckBox.setChecked(config.Graphics.VSync)
        MainWindow.showFPSCheckBox.setChecked(config.Graphics.ShowFPS)
        MainWindow.MSAASpinBox.setValue(config.Graphics.MSAA)  
        MainWindow.FPSCapSpinBox.setValue(config.Graphics.FPSCap)
      
        ## Audio
        MainWindow.globalVolumeSlider.setValue(config.Audio.GlobalVolume)
        MainWindow.musicVolumeSlider.setValue(config.Audio.MusicVolume)
        MainWindow.hitSoundVolumeSlider.setValue(config.Audio.HitSoundVolume)

        ## Knockout
        MainWindow.knockoutModeComboBox.setCurrentIndex(config.Knockout.Mode)
        MainWindow.maxPlayersSpinBox.setValue(config.Knockout.MaxPlayers)
        MainWindow.bubbleMinimumComboSpinBox.setValue(config.Knockout.BubbleMinimumCombo)
        MainWindow.revivePlayersAtEndCheckBox.setChecked(config.Knockout.RevivePlayersAtEnd)
        MainWindow.liveSortCheckBox.setChecked(config.Knockout.LiveSort)
        MainWindow.sortByComboBox.setCurrentIndex(abs(MainWindow.sortByComboBox.findText(config.Knockout.SortBy)))
        MainWindow.HideOverlayOnBreaksCheckBox.setChecked(config.Knockout.HideOverlayOnBreaks)
        MainWindow.addDanserCheckBox.setChecked(config.Knockout.AddDanser)
        MainWindow.danserNameLineEdit.setText(config.Knockout.DanserName)
        MainWindow.dateFormatComboBox.setCurrentIndex(config.Knockout.DateFormat)
        MinCursorSize, MaxCursorSize = min(config.Knockout.MinCursorSize, config.Knockout.MaxCursorSize), max(config.Knockout.MinCursorSize, config.Knockout.MaxCursorSize)
        MainWindow.knockoutCursorSizeSlider.setValue((MinCursorSize, MaxCursorSize))
        self.splitModesToSetMainWindow(MainWindow, "exclude")
        self.splitModesToSetMainWindow(MainWindow, "hide")
        
        ## Recording
        MainWindow.recordingWidth.setText(str(config.Recording.FrameWidth))
        MainWindow.recordingHeight.setText(str(config.Recording.FrameHeight))
        MainWindow.recordingFPSSpinBox.setValue(config.Recording.FPS)
        MainWindow.motionBlurcheckBox.setChecked(config.Recording.MotionBlur)
        MainWindow.outputPathLineEdit.setText(abspath(config.Recording.OutputPath))
        MainWindow.outputNameLineEdit.setText(config.Recording.OutputName)

        encoder_options = {'cpu':0, 'nvidia':1, 'amd':2, 'intel':3, 'customize':4}
        MainWindow.recordingEncoderComboBox.setCurrentIndex(encoder_options[config.Recording.Encoder])

        #if MainWindow.recordingEncoderComboBox.currentIndex() + 1 == MainWindow.recordingEncoderComboBox.count():
        MainWindow.videoCodecCustomizeLineEdit.setText(config.Recording.EncoderConfig.VideoCodec)
        MainWindow.encoderOptionCustomizeLineEdit.setText(config.Recording.EncoderConfig.EncoderOptions)
        MainWindow.presetCustomizeLineEdit.setText(config.Recording.EncoderConfig.Preset)
        MainWindow.audioCodecCustomizeLineEdit.setText(config.Recording.EncoderConfig.AudioCodec)
        MainWindow.audioOptionCustomizeLineEdit.setText(config.Recording.EncoderConfig.AudioOptions)

        ## Gameplay
        MainWindow.hitErrorMeterShowCheckBox.setChecked(config.Gameplay.HitErrorMeter.Show)
        MainWindow.hitErrorMeterShowUnstableRateCheckBox.setChecked(config.Gameplay.HitErrorMeter.ShowUnstableRate)
        MainWindow.scoreShowCheckBox.setChecked(config.Gameplay.Score.Show)
        MainWindow.hpBarShowCheckBox.setChecked(config.Gameplay.HpBar.Show)
        MainWindow.comboCounterShowCheckBox.setChecked(config.Gameplay.ComboCounter.Show)
        MainWindow.ppCounterShowCheckBox.setChecked(config.Gameplay.PPCounter.Show)
        MainWindow.ppCounterUseLazerPPCheckBox.setChecked(config.Gameplay.PPCounter.UseLazerPP)
        MainWindow.strainGraphShowCheckBox.setChecked(config.Gameplay.StrainGraph.Show)
        MainWindow.keyOverlayShowCheckBox.setChecked(config.Gameplay.KeyOverlay.Show)
        MainWindow.scoreBoardShowCheckBox.setChecked(config.Gameplay.ScoreBoard.Show)
        MainWindow.scoreBoardShowAvatarsCheckBox.setChecked(config.Gameplay.ScoreBoard.ShowAvatars)
        MainWindow.scoreBoardHideOthersCheckBox.setChecked(config.Gameplay.ScoreBoard.HideOthers)
        MainWindow.hitCounterShowCheckBox.setChecked(config.Gameplay.HitCounter.Show)
        MainWindow.aimErrorMeterShowCheckBox.setChecked(config.Gameplay.AimErrorMeter.Show)
        MainWindow.boundariesShowCheckBox.setChecked(config.Gameplay.Boundaries.Show)
        MainWindow.modsShowCheckBox.setChecked(config.Gameplay.Mods.Show)
        MainWindow.modsHideInReplaysCheckBox.setChecked(config.Gameplay.Mods.HideInReplays)
        MainWindow.modsFoldInReplaysCheckBox.setChecked(config.Gameplay.Mods.FoldInReplays)
        MainWindow.resultsScreenShowCheckBox.setChecked(config.Gameplay.ResultsScreen.Show)
        MainWindow.resultsScreenTimeSpinBox.setValue(config.Gameplay.ResultsScreen.Time)
        MainWindow.resultsScreenUseLocalTimeZoneCheckBox.setChecked(config.Gameplay.ResultsScreen.UseLocalTimeZone)

        ## Input
        MainWindow.leftKeyPushButton.setText(config.Input.LeftKey)
        MainWindow.rightKeyPushButton.setText(config.Input.RightKey)
        MainWindow.restartKeyPushButton.setText(config.Input.RestartKey)
        MainWindow.smokeKeyPushButton.setText(config.Input.SmokeKey)
        MainWindow.mouseButtonsDisabledCheckBox.setChecked(config.Input.MouseButtonsDisabled)

        ## Skin
        # CurrentSkin Init in DanserUiMainWindow.skinsComboBoxInit
        MainWindow.useSkinColorsRadioButton.setChecked(config.Skin.UseSkinColors)
        MainWindow.useBeatmapColorsRadioButton.setChecked(config.Skin.
        UseBeatmapColors)
        MainWindow.useSkinCursorCheckBox.setChecked(config.Skin.UseSkinCursor)
        MainWindow.useSkinHitsoundsCheckBox.setChecked(config.Skin.UseSkinHitsounds)

        ## Cursor
        MainWindow.scaleToCSCheckBox.setChecked(config.Cursor.ScaleToCS)
        MainWindow.cursorRainbowCheckBox.setChecked(config.Cursor.CursorRainbow)
        MainWindow.cursorTrailGlowCheckBox.setChecked(config.Cursor.CursorTrailGlow)
        MainWindow.cursorSizeSlider.setValue(config.Cursor.CursorSize)
        MainWindow.cursorRipplesCheckBox.setChecked(config.Cursor.CursorRipples)
        MainWindow.forceLongTrailCheckBox.setChecked(config.Cursor.ForceLongTrail)
        MainWindow.longTrailDensitySpinBox.setValue(config.Cursor.LongTrailDensity)
        MainWindow.longTrailLengthSpinBox.setValue(config.Cursor.LongTrailLength)

        ## Objects
        MainWindow.drawFollowPointsCheckBox.setChecked(config.Objects.DrawFollowPoints)
        MainWindow.drawComboNumbersCheckBox.setChecked(config.Objects.DrawComboNumbers)
        MainWindow.scaleToTheBeatCheckBox.setChecked(config.Objects.ScaleToTheBeat)
        MainWindow.sliderMergeCheckBox.setChecked(config.Objects.SliderMerge)
        MainWindow.objectsRainbowCheckBox.setChecked(config.Objects.Rainbow)
        MainWindow.flashToTheBeatCheckBox.setChecked(config.Objects.FlashToTheBeat)
        MainWindow.useHitCircleColorCheckBox.setChecked(config.Objects.UseHitCircleColor)
        MainWindow.sliderSnakingInCheckBox.setChecked(config.Objects.SliderSnakingIn)
        MainWindow.sliderSnakingOutCheckBox.setChecked(config.Objects.SliderSnakingOut)
        
        ## Playfield
        MainWindow.seizureWarningCheckBox.setChecked(config.Playfield.SeizureWarning)
        MainWindow.loadStoryboardCheckBox.setChecked(config.Playfield.LoadStoryboard)
        MainWindow.loadVideoCheckBox.setChecked(config.Playfield.SeizureWarning)
        MainWindow.bgParallaxCheckBox.setChecked(config.Playfield.BGParallax)
        MainWindow.showDanserLogoCheckBox.setChecked(config.Playfield.ShowDanserLogo)
        MainWindow.introBGDimSlider.setValue(config.Playfield.IntroBGDim)
        MainWindow.inGameBGDimSlider.setValue(config.Playfield.InGameBGDim)
        MainWindow.breakBGDimSlider.setValue(config.Playfield.BreakBGDim)
        MainWindow.quickStartCheckBox.setChecked(config.Playfield.QuickStart)
        MainWindow.skipIntroCheckBox.setChecked(config.Playfield.QuickStart or config.Playfield.SkipIntro)
        

    def setConfigByMainWindow(self):
        MainWindow, config = self.MainWindow, self.gui_config

        # Settings
        ## General
        config.Gameplay.PlayUsername = MainWindow.usernameLineEdit.text()
        config.General.SongsDBMode = MainWindow.songsDBModeComboBox.currentText()
        config.General.OsuSongsDir = MainWindow.songsPathLineEdit.text()
        config.General.OsuSkinsDir = MainWindow.skinsPathLineEdit.text()
        config.General.DanserRootDir = MainWindow.danserPathLineEdit.text()
        config.General.DanserMode = MainWindow.danserModeComboBox.currentText()
        config.General.IsRecord = MainWindow.isRecordCheckBox.isChecked()
        config.General.OsuApi = MainWindow.osuApiLineEdit.text()
        config.General.Language = MainWindow.languageComboBox.currentIndex()

        ## Graphics
        config.Graphics.Width = int(MainWindow.graphicsWidth.text() if MainWindow.graphicsWidth.text() else 1920)
        config.Graphics.Height = int(MainWindow.graphicsHeight.text() if MainWindow.graphicsHeight.text() else 1080)
        config.Graphics.Fullscreen = MainWindow.fullScreenCheckBox.isChecked()
        config.Graphics.VSync = MainWindow.vsyncCheckBox.isChecked()
        config.Graphics.ShowFPS = MainWindow.showFPSCheckBox.isChecked()
        config.Graphics.MSAA = MainWindow.MSAASpinBox.value()
        config.Graphics.FPSCap = MainWindow.FPSCapSpinBox.value()

        ## Audio
        config.Audio.GlobalVolume = MainWindow.globalVolumeSlider.value()
        config.Audio.MusicVolume = MainWindow.musicVolumeSlider.value()
        config.Audio.HitSoundVolume = MainWindow.hitSoundVolumeSlider.value()

        ## Knockout
        config.Knockout.Mode = MainWindow.knockoutModeComboBox.currentIndex()
        config.Knockout.MaxPlayers = MainWindow.maxPlayersSpinBox.value()
        config.Knockout.BubbleMinimumCombo = MainWindow.bubbleMinimumComboSpinBox.value()
        config.Knockout.RevivePlayersAtEnd = MainWindow.revivePlayersAtEndCheckBox.isChecked()
        config.Knockout.LiveSort = MainWindow.liveSortCheckBox.isChecked()
        config.Knockout.SortBy = MainWindow.sortByComboBox.currentText()
        config.Knockout.HideOverlayOnBreaks = MainWindow.HideOverlayOnBreaksCheckBox.isChecked()
        config.Knockout.AddDanser = MainWindow.addDanserCheckBox.isChecked()
        config.Knockout.DanserName = MainWindow.danserNameLineEdit.text()
        config.Knockout.DateFormat = MainWindow.dateFormatComboBox.currentIndex()
        config.Knockout.MinCursorSize, config.Knockout.MaxCursorSize = map(lambda x: round(x, 2), MainWindow.knockoutCursorSizeSlider.value())
        self.mergeModesToSetConfig(MainWindow, "exclude")
        self.mergeModesToSetConfig(MainWindow, "hide")

        ## Recording
        config.Recording.FrameWidth = int(MainWindow.recordingWidth.text() if MainWindow.recordingWidth.text() else 1920)
        config.Recording.FrameHeight = int(MainWindow.recordingHeight.text() if MainWindow.recordingHeight.text() else 1080)
        config.Recording.FPS = MainWindow.recordingFPSSpinBox.value()
        config.Recording.MotionBlur = MainWindow.motionBlurcheckBox.isChecked()
        config.Recording.OutputPath = MainWindow.outputPathLineEdit.text()
        config.Recording.OutputName = MainWindow.outputNameLineEdit.text()
        encoder_options = ['cpu', 'nvidia', 'amd', 'intel', 'customize']
        config.Recording.Encoder = encoder_options[MainWindow.recordingEncoderComboBox.currentIndex()]
        # if MainWindow.recordingEncoderComboBox.currentIndex() + 1 == MainWindow.recordingEncoderComboBox.count():
        config.Recording.EncoderConfig.VideoCodec = MainWindow.videoCodecCustomizeLineEdit.text()
        config.Recording.EncoderConfig.EncoderOptions = MainWindow.encoderOptionCustomizeLineEdit.text()
        config.Recording.EncoderConfig.Preset = MainWindow.presetCustomizeLineEdit.text()
        config.Recording.EncoderConfig.AudioCodec = MainWindow.audioCodecCustomizeLineEdit.text()
        config.Recording.EncoderConfig.AudioOptions = MainWindow.audioOptionCustomizeLineEdit.text()

        ## Gameplay
        config.Gameplay.HitErrorMeter.Show = MainWindow.hitErrorMeterShowCheckBox.isChecked()
        config.Gameplay.HitErrorMeter.ShowUnstableRate = MainWindow.hitErrorMeterShowUnstableRateCheckBox.isChecked()
        config.Gameplay.Score.Show = MainWindow.scoreShowCheckBox.isChecked()
        config.Gameplay.HpBar.Show = MainWindow.hpBarShowCheckBox.isChecked()
        config.Gameplay.ComboCounter.Show = MainWindow.comboCounterShowCheckBox.isChecked()
        config.Gameplay.PPCounter.Show = MainWindow.ppCounterShowCheckBox.isChecked()
        config.Gameplay.PPCounter.UseLazerPP = MainWindow.ppCounterUseLazerPPCheckBox.isChecked()
        config.Gameplay.StrainGraph.Show = MainWindow.strainGraphShowCheckBox.isChecked()
        config.Gameplay.KeyOverlay.Show = MainWindow.keyOverlayShowCheckBox.isChecked()
        config.Gameplay.ScoreBoard.Show = MainWindow.scoreBoardShowCheckBox.isChecked()
        config.Gameplay.ScoreBoard.ShowAvatars = MainWindow.scoreBoardShowAvatarsCheckBox.isChecked()
        config.Gameplay.ScoreBoard.HideOthers = MainWindow.scoreBoardHideOthersCheckBox.isChecked()
        config.Gameplay.HitCounter.Show = MainWindow.hitCounterShowCheckBox.isChecked()
        config.Gameplay.AimErrorMeter.Show = MainWindow.aimErrorMeterShowCheckBox.isChecked()
        config.Gameplay.Boundaries.Show = MainWindow.boundariesShowCheckBox.isChecked()
        config.Gameplay.Mods.Show = MainWindow.modsShowCheckBox.isChecked()
        config.Gameplay.Mods.HideInReplays = MainWindow.modsHideInReplaysCheckBox.isChecked()
        config.Gameplay.Mods.FoldInReplays = MainWindow.modsFoldInReplaysCheckBox.isChecked()
        config.Gameplay.ResultsScreen.Show = MainWindow.resultsScreenShowCheckBox.isChecked()
        config.Gameplay.ResultsScreen.Time = MainWindow.resultsScreenTimeSpinBox.value()
        config.Gameplay.ResultsScreen.UseLocalTimeZone = MainWindow.resultsScreenUseLocalTimeZoneCheckBox.isChecked()

        ## Input
        config.Input.LeftKey = MainWindow.leftKeyPushButton.text()
        config.Input.RightKey = MainWindow.rightKeyPushButton.text()
        config.Input.RestartKey = MainWindow.restartKeyPushButton.text()
        config.Input.SmokeKey = MainWindow.smokeKeyPushButton.text()
        config.Input.MouseButtonsDisabled = MainWindow.mouseButtonsDisabledCheckBox.isChecked()

        ## Skin
        config.Skin.CurrentSkin = MainWindow.skinsComboBox.currentText()
        config.Skin.UseSkinColors = MainWindow.useSkinColorsRadioButton.isChecked()
        config.Skin.UseBeatmapColors = MainWindow.useBeatmapColorsRadioButton.isChecked()
        config.Skin.UseSkinCursor = MainWindow.useSkinCursorCheckBox.isChecked()
        config.Skin.UseSkinHitsounds = MainWindow.useSkinHitsoundsCheckBox.isChecked()

        ## Cursor
        config.Cursor.ScaleToCS = MainWindow.scaleToCSCheckBox.isChecked()
        config.Cursor.CursorRainbow = MainWindow.cursorRainbowCheckBox.isChecked()
        config.Cursor.CursorTrailGlow = MainWindow.cursorTrailGlowCheckBox.isChecked()
        config.Cursor.CursorSize = round(float(MainWindow.cursorSizeSlider.value()), 2)
        config.Cursor.CursorRipples = MainWindow.cursorRipplesCheckBox.isChecked()
        config.Cursor.ForceLongTrail = MainWindow.forceLongTrailCheckBox.isChecked()
        config.Cursor.LongTrailDensity = MainWindow.longTrailDensitySpinBox.value()
        config.Cursor.LongTrailLength = MainWindow.longTrailLengthSpinBox.value()

        ## Objects
        config.Objects.DrawFollowPoints = MainWindow.drawFollowPointsCheckBox.isChecked()
        config.Objects.DrawComboNumbers = MainWindow.drawComboNumbersCheckBox.isChecked()
        config.Objects.ScaleToTheBeat = MainWindow.scaleToTheBeatCheckBox.isChecked()
        config.Objects.SliderMerge = MainWindow.sliderMergeCheckBox.isChecked()
        config.Objects.Rainbow = MainWindow.objectsRainbowCheckBox.isChecked()
        config.Objects.FlashToTheBeat = MainWindow.flashToTheBeatCheckBox.isChecked()
        config.Objects.UseHitCircleColor = MainWindow.useHitCircleColorCheckBox.isChecked()
        config.Objects.SliderSnakingIn = MainWindow.sliderSnakingInCheckBox.isChecked()
        config.Objects.SliderSnakingOut = MainWindow.sliderSnakingOutCheckBox.isChecked()

        ## Playfield
        config.Playfield.SeizureWarning = MainWindow.seizureWarningCheckBox.isChecked()
        config.Playfield.LoadStoryboard = MainWindow.loadStoryboardCheckBox.isChecked()
        config.Playfield.LoadVideo = MainWindow.loadVideoCheckBox.isChecked()
        config.Playfield.BGParallax = MainWindow.bgParallaxCheckBox.isChecked()
        config.Playfield.ShowDanserLogo = MainWindow.showDanserLogoCheckBox.isChecked()
        config.Playfield.IntroBGDim = MainWindow.introBGDimSlider.value()
        config.Playfield.InGameBGDim = MainWindow.inGameBGDimSlider.value()
        config.Playfield.BreakBGDim = MainWindow.breakBGDimSlider.value()
        config.Playfield.QuickStart = MainWindow.quickStartCheckBox.isChecked()
        config.Playfield.SkipIntro = config.Playfield.QuickStart or MainWindow.skipIntroCheckBox.isChecked()

    def resizeEvent(self, event):
        height = self.width() * 9 // 16
        self.resize(self.width(), height)
