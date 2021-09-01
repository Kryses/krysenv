import sys

from PySide2 import QtWidgets

from widgets.launcher import Launcher

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = Launcher()
    widget.show()
    sys.exit(app.exec_())