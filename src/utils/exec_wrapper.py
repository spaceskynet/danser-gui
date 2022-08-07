#!/usr/bin/env python3
import consts
from os import curdir, chdir
from PyQt5.QtCore import QProcess, QThread, pyqtSignal
from os.path import join, abspath
from utils.osudbparser import create_db
from utils.osrparser import add_date_after_user_name, modify_replay_beatmap_hash
import re
import logging
import traceback
from autologging import traced, logged

@logged(logging.getLogger(__name__))
@traced('run')
class SongsDBUpdateThread(QThread):
    def __init__(self, songs_db_mode=None, osu_root_path=None, danser_root_path=None, parent=None):
        super(SongsDBUpdateThread, self).__init__(parent)
        self.init(songs_db_mode, osu_root_path, danser_root_path)
        self.working = True

    def init(self, songs_db_mode=None, osu_root_path=None, danser_root_path=None):
        self.songs_db_mode = songs_db_mode
        self.osu_root_path = osu_root_path
        self.danser_root_path = danser_root_path

    def __del__(self):
        self.working = False
        self.wait()

    def readProcessAllStandardOutput(self):
        return bytes(self.p.readAllStandardOutput()).decode()

    def readProcessAllStandardError(self):
        return bytes(self.p.readAllStandardError()).decode()

    def run(self):
        songs_db_mode, osu_root_path, danser_root_path = self.songs_db_mode, self.osu_root_path, self.danser_root_path

        if songs_db_mode == 'osu!':
            try:
                create_db(join(osu_root_path, 'osu!.db'), join(consts.root_path, 'osu!.sqlite3.db'))
            except Exception as e:
                logging.info(f"[GUI][SongsDBUpdateThread][osu!] {traceback.format_exc()}")
            logging.info("[GUI][SongsDBUpdateThread][osu!] Finshed!")

        # after osu! database updated, danser database must be updated.
        self.p = QProcess()
        self.p.start(join(danser_root_path, consts.danser_exec_file_name), ["-md5=0"])
        self.p.readyReadStandardOutput.connect(lambda: (logging.info(f"[DANSER][STDOUT] {self.readProcessAllStandardOutput()}")))
        self.p.readyReadStandardError.connect(lambda: (logging.info(f"[DANSER][STDERR] {self.readProcessAllStandardError()}")))
        self.p.finished.connect(lambda: (logging.info("[GUI][SongsDBUpdateThread][danser] Finshed!")))
        self.p.waitForStarted() 
        self.p.waitForFinished(-1)

@logged(logging.getLogger(__name__))
@traced("run")
class ReplayModifyThread(QThread):
    def __init__(self, root_path=None, beatmap_hash=None, date_format_index=None, parent=None):
        super(ReplayModifyThread, self).__init__(parent)
        self.init(root_path, beatmap_hash, date_format_index)

    def init(self, root_path=None, beatmap_hash=None, date_format_index=None):
        self.root_path = root_path
        self.beatmap_hash = beatmap_hash
        self.date_format_index = date_format_index

    def run(self):
        if self.beatmap_hash != None:
            modify_replay_beatmap_hash(self.root_path, self.beatmap_hash)
        if self.date_format_index != None:
            add_date_after_user_name(self.root_path, self.date_format_index)

@logged(logging.getLogger(__name__))
@traced("run", "setProgressDialog")
class DanserExecByArgsThread(QThread):
    setProgressValue = pyqtSignal(tuple)
    def __init__(self, progressDialog, root_path=None, arguments=None, is_record=False, parent=None):
        super(DanserExecByArgsThread, self).__init__(parent)
        self.progressDialog = progressDialog
        self.init(root_path, arguments, is_record)
        self.curdir = abspath(curdir)
        self.working = True
        self.success = True
        self.errorMsg = None

    def init(self, root_path=None, arguments=None, is_record=False):
        self.arguments = arguments
        self.root_path = root_path
        self.is_record = is_record
        self.success = True
    
    def __del__(self):
        self.working = False
        chdir(self.curdir)
        self.wait()

    def setProgressDialog(self, standard_output_decode):
        standard_output_decode = standard_output_decode[standard_output_decode.find('Progress:'):]
        pattern = re.compile(r"Progress: (\d+)%, Speed: (\S+)x, ETA: (\S+)")
        match = pattern.match(standard_output_decode)
        if match:
            self.setProgressValue.emit(match.groups())
        # Progress: 10%, Speed: 0.59x, ETA: 35s
    
    def setErrorMsg(self, standard_error_decode):
        self.success = False
        pattern = re.compile(r"panic: (.*)\n")
        match = pattern.search(standard_error_decode)
        if match:
            self.errorMsg = "\n".join(match.groups())

    def readProcessAllStandardOutput(self):
        standardOutputDecode = bytes(self.p.readAllStandardOutput()).decode()
        if self.is_record and 'Progress:' in standardOutputDecode:
            self.setProgressDialog(standardOutputDecode)
        return standardOutputDecode

    def readProcessAllStandardError(self):
        standardErrorDecode = bytes(self.p.readAllStandardError()).decode()
        if 'panic:' in standardErrorDecode:
            self.setErrorMsg(standardErrorDecode)
        return bytes(self.p.readAllStandardError()).decode()

    def run(self):
        self.p = QProcess()
        # self.p.setArguments(self.arguments)
        chdir(self.root_path)
        self.p.start(consts.danser_exec_file_name, self.arguments)
        self.p.readyReadStandardOutput.connect(lambda: (logging.info(f"[DANSER][STDOUT] {self.readProcessAllStandardOutput()}")))
        self.p.readyReadStandardError.connect(lambda: (logging.info(f"[DANSER][STDERR] {self.readProcessAllStandardError()}")))
        self.p.finished.connect(lambda: (logging.info("[GUI][DanserExecByArgsThread] Finshed!")))
        self.p.waitForStarted()
        self.p.waitForFinished(-1)
    

if __name__ == "__main__":
    pass