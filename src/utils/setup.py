#!/usr/bin/env python3
import sys, toml, logging, traceback
import consts
from autologging import TRACE
from munch import Munch
from os.path import join, abspath, exists
from ui.setupMainWindow import *
from utils.exception_handling import customInfo, isEmptyWarning, customError
from utils.exec_wrapper import SongsDBUpdateThread
import ui.danserGuiRes as danserGuiRes

class setupUiMainWindow(Ui_setupMainWindow):
    def __init__(self, setupMainWindow):
        super().__init__()
        self.config = setupMainWindow.config
        self.setupUi(setupMainWindow)

        self.trans = QTranslator(setupMainWindow)
        self.setLanguage(setupMainWindow)

        self.songsDBUpdateThread = SongsDBUpdateThread()
        self.songsDBUpdateThread.started.connect(self.songsDBUpdateEventStarted)
        self.songsDBUpdateThread.finished.connect(lambda: (self.songsDBUpdateEventFinished(setupMainWindow)))

        self.languageComboBox.activated.connect(lambda: (self.languageComboBoxChanged(setupMainWindow)))
        self.songsDBModeComboBox.activated[str].connect(self.songsDBModeComboBoxChanged)
        self.osuRootPathLineEdit.clicked.connect(lambda: (self.osuRootPathLineEditClicked(setupMainWindow)))
        self.songsPathLineEdit.clicked.connect(lambda: (self.songsPathLineEditClicked(setupMainWindow)))
        self.skinsPathLineEdit.clicked.connect(lambda: (self.skinsPathLineEditClicked(setupMainWindow)))
        self.danserPathLineEdit.clicked.connect(lambda: (self.danserPathLineEditClicked(setupMainWindow)))

        self.buttonBox.accepted.connect(self.setupSettings)
        self.buttonBox.rejected.connect(setupMainWindow.close)

    def setLanguage(self, setupMainWindow):
        if self.config.General.Language == 0:
            self.trans.load(join(consts.langs_path, 'en-US'))
        else:
            self.trans.load(join(consts.langs_path, 'zh-CN'))
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(setupMainWindow)
    
    def languageComboBoxChanged(self, setupMainWindow):
        self.config.General.Language = self.languageComboBox.currentIndex()
        self.setLanguage(setupMainWindow)

    def songsDBModeComboBoxChanged(self, section):
        if section != 'osu!':
            self.osuRootPathLineEdit.setDisabled(True)
        else:
            self.osuRootPathLineEdit.setEnabled(True)
    
    def osuRootPathLineEditClicked(self, MainWindow):
        start_path = consts.root_path
        osu_root_path = QFileDialog.getExistingDirectory(MainWindow, QCoreApplication.translate("setupMainWindow", u"Choose osu root folder", None), start_path)
        if osu_root_path:
            self.osuRootPathLineEdit.setText(abspath(osu_root_path))
            songs_path = abspath(join(osu_root_path, 'Songs'))
            skins_path = abspath(join(osu_root_path, 'Skins'))
            if exists(songs_path): self.songsPathLineEdit.setText(songs_path)
            if exists(skins_path): self.skinsPathLineEdit.setText(skins_path)
        else:
            pass

    def songsPathLineEditClicked(self, MainWindow):
        songs_db_mode = self.songsDBModeComboBox.currentText()
        if songs_db_mode == 'osu!':
            start_path = self.osuRootPathLineEdit.text() or consts.root_path
        else:
            start_path = consts.root_path
        songs_path = QFileDialog.getExistingDirectory(MainWindow, QCoreApplication.translate("setupMainWindow", u"Choose osu songs folder", None), start_path)
        if songs_path:
            self.songsPathLineEdit.setText(abspath(songs_path))
        else:
            pass
    
    def skinsPathLineEditClicked(self, MainWindow):
        songs_db_mode = self.songsDBModeComboBox.currentText()
        if songs_db_mode == 'osu!':
            start_path = self.osuRootPathLineEdit.text() or consts.root_path
        else:
            start_path = consts.root_path
        skins_path = QFileDialog.getExistingDirectory(MainWindow, QCoreApplication.translate("setupMainWindow", u"Choose osu skins folder", None), start_path)
        if skins_path:
            self.skinsPathLineEdit.setText(abspath(skins_path))
        else:
            pass

    def danserPathLineEditClicked(self, MainWindow):
        start_path = consts.root_path
        danser_path = QFileDialog.getExistingDirectory(MainWindow, QCoreApplication.translate("setupMainWindow", u"Choose danser root folder", None), start_path)
        if danser_path:
            self.danserPathLineEdit.setText(abspath(danser_path))
        else:
            pass

    def writeConfigFile(self):
        config_path = consts.config_path
        with open(config_path, 'w', encoding='utf-8') as f:
            toml.dump(self.config.toDict(), f)

    def checkWidgetsIsValid(self):
        if self.songsDBModeComboBox.currentText() == 'osu!' and not self.osuRootPathLineEdit.text():
            return (False, isEmptyWarning(QCoreApplication.translate("setupMainWindow", u"osu Root Path", None)))
        if not self.songsPathLineEdit.text():
            return (False, isEmptyWarning(QCoreApplication.translate("setupMainWindow", u"Songs Path", None)))
        if not self.skinsPathLineEdit.text():
            return (False, isEmptyWarning(QCoreApplication.translate("setupMainWindow", u"Skins Path", None)))
        if not self.danserPathLineEdit.text():
            return (False, isEmptyWarning(QCoreApplication.translate("setupMainWindow", u"danser Path", None)))
        return True, None
 
    def songsDBUpdateEvent(self): # generate danser default.json
        songs_db_mode = "danser"
        osu_root_path = None
        danser_root_path = self.config.General.DanserRootDir
        self.songsDBUpdateThread.init(songs_db_mode, osu_root_path, danser_root_path)
        self.songsDBUpdateThread.start()

    def songsDBUpdateEventStarted(self):
        logging.info("[GUI] songsDBUpdateEvent Started")
        self.songsDBModeComboBox.setDisabled(True)

    def songsDBUpdateEventFinished(self, setupMainWindow):
        logging.info("[GUI] songsDBUpdateEvent Finished")
        self.songsDBModeComboBox.setEnabled(True)
        customInfo(QCoreApplication.translate("setupMainWindow", u"Please update songs db at first!", None))
        setupMainWindow.accepted.emit()
        setupMainWindow.close()

    def setupSettings(self):
        if not self.checkWidgetsIsValid()[0]: return
        config = self.config
        config.General.Language = self.languageComboBox.currentIndex()
        config.General.OsuRootDir = self.osuRootPathLineEdit.text()
        config.General.OsuSongsDir = self.songsPathLineEdit.text()
        config.General.OsuSkinsDir = self.skinsPathLineEdit.text()
        config.General.DanserRootDir = self.danserPathLineEdit.text()
        config.General.SongsDBMode = self.songsDBModeComboBox.currentText()

        self.writeConfigFile()
        self.songsDBUpdateEvent()

class setupMainWindow(QMainWindow):
    accepted = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.old_hook = sys.excepthook
        sys.excepthook = self.catch_exceptions
        logging.basicConfig(level=TRACE, filename=consts.LogPath.setup, filemode="w", format="%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s")

        self.config = Munch.fromDict(toml.loads(consts.default_settings_toml))
        self.UiMainWindow = setupUiMainWindow(self)
        gui_icon = QIcon()
        gui_icon.addFile(u":/assets/danser-gui.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(gui_icon)
        self.show()

    def catch_exceptions(self, ty, value, traceback_object):
        traceback_format = traceback.format_exception(ty, value, traceback_object)
        traceback_string = "".join(traceback_format)
        customError(traceback_string)
        self.old_hook(ty, value, traceback_object)

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    App = QApplication(sys.argv)
    window = setupMainWindow()
    
    ret = App.exec_()
    sys.exit(ret)