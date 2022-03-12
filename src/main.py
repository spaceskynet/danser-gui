#!/usr/bin/env python3
import os, sys
import PyQt5
import consts
from ui.gui import *
from utils.setup import setupMainWindow

def checkSetup(App, exec_path, debug):
    if not isfile(consts.config_path):
        setup_window = setupMainWindow()
        setup_window.accepted.connect(lambda: (launchMainWindow(App, exec_path, debug)))
    else:
        launchMainWindow(App, exec_path, debug)

def launchMainWindow(App, exec_path, debug):
    window = DanserMainWindow(App, exec_path, debug)
    return

def main(exec_path = "."):
    exec_path = os.path.abspath(exec_path)

    if not os.path.isdir(os.path.join(exec_path, "logs")):
        os.mkdir(os.path.join(exec_path, "logs"))

    consts.LogPath.app = os.path.join(exec_path, "logs", consts.LogPath.app)
    consts.LogPath.setup = os.path.join(exec_path, "logs", consts.LogPath.setup)

    qt_path = os.path.dirname(PyQt5.__file__)
    pluginpath = os.path.join(qt_path, "Qt/plugins")
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = pluginpath

    no_high_dpi_scale = len(sys.argv) > 1 and ('-s' in sys.argv[1:] or '-noscale' in sys.argv[1:])
    if not no_high_dpi_scale:
        QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    App = QApplication(sys.argv)
    
    if consts.running_system == 'Windows':
        font = QFont("Microsoft YaHei", 9)
        App.setFont(font)
    
    debug = len(sys.argv) > 1 and ('-d' in sys.argv[1:] or '-debug' in sys.argv[1:])

    checkSetup(App, exec_path, debug)

    ret = App.exec_()
    sys.exit(ret)

if __name__ == "__main__":
    main()
