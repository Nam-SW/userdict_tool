from sys import argv as sys_argv
from sys import exit as sys_exit

from PyQt5.QtWidgets import QApplication

from app import ToolApp

if __name__ == "__main__":
    app = QApplication(sys_argv)
    ex = ToolApp()
    sys_exit(app.exec_())
