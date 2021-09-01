from PySide2 import QtCore
from PySide2.QtUiTools import loadUiType

from core.globals import QT_UI_PATH, DEFAULT_STYLESHEET

LauncherObj, BaseType = loadUiType(str(QT_UI_PATH.joinpath('launcher.ui')))


class Launcher(LauncherObj, BaseType):
    def __init__(self, parent=None):
        super(Launcher, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        with open(str(DEFAULT_STYLESHEET)) as style_sheet:
            self.setStyleSheet(style_sheet.read())


