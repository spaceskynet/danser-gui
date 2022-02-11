#!/usr/bin/env python3
import logging
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication, QSize
import danserGuiRes

def isEmptyWarning(text):
    customWarning("{} {}".format(text, QCoreApplication.translate('MainWindow', u'is Empty!', None)))

def customWarning(content):
    msg_box = QMessageBox(QMessageBox.Warning, QCoreApplication.translate("MainWindow", u'Warning', None), content)
    gui_icon = QIcon()
    gui_icon.addFile(u":/assets/danser-gui.ico", QSize(), QIcon.Normal, QIcon.Off)
    msg_box.setWindowIcon(gui_icon)
    logging.info(f"[GUI][WARNING] {content}")
    msg_box.exec_()

def customError(content):
    msg_box = QMessageBox(QMessageBox.Critical, QCoreApplication.translate("MainWindow", u'Error', None), content)
    gui_icon = QIcon()
    gui_icon.addFile(u":/assets/danser-gui.ico", QSize(), QIcon.Normal, QIcon.Off)
    msg_box.setWindowIcon(gui_icon)
    logging.info(f"[GUI][ERROR] {content}")
    msg_box.exec_()

def customInfo(content):
    msg_box = QMessageBox(QMessageBox.Information, QCoreApplication.translate("MainWindow", u'Info', None), content)
    gui_icon = QIcon()
    gui_icon.addFile(u":/assets/danser-gui.ico", QSize(), QIcon.Normal, QIcon.Off)
    msg_box.setWindowIcon(gui_icon)
    logging.info(f"[GUI][INFO] {content}")
    msg_box.exec_()
