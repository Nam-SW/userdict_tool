from os import path

from pandas import read_excel
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (
    QFileDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QShortcut,
    QTextEdit,
    QWidget,
)

from utils import str_to_list


class ToolApp(QWidget):
    def __init__(self):
        super().__init__()

        self.data = None
        self.index = 0
        self.userdict_path = None
        self.userdict = []

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        hbox = QHBoxLayout()
        self.setLayout(grid)

        # lable
        for i, v in enumerate(
            ["datafile", "userdict_filename", "original", "splited", "input_tokens",]
        ):
            grid.addWidget(QLabel(v), i, 0)

        grid.addWidget(QLabel("userdict(reversed)"), 0, 4)

        # 버튼
        self.select_file_button = QPushButton(text="find")
        self.select_file_button.clicked.connect(self.showDialog)
        self.setup_button = QPushButton(text="setup")
        self.setup_button.clicked.connect(self.setup)

        self.end_button = QPushButton(text="Quit")
        self.end_button.clicked.connect(self.quit)

        # 텍스트박스
        self.datafile_lineedit = QLineEdit()
        self.userdict_filename_lineedit = QLineEdit("userdict_ko.txt")

        self.original_textedit = QTextEdit()
        self.original_textedit.setReadOnly(True)
        self.splited_textedit = QTextEdit()
        self.splited_textedit.setReadOnly(True)

        self.userdict_textedit = QTextEdit()
        self.userdict_textedit.setReadOnly(True)
        # self.userdict_textedit.resize(50, 500)

        self.input_tokens_lineedit = QLineEdit()
        self.input_tokens_lineedit.editingFinished.connect(self.add_userdict)

        # hbox widget
        self.prev_button = QPushButton(text="<-")
        self.prev_button.clicked.connect(self.prev_show)
        self.next_button = QPushButton(text="->")
        self.next_button.clicked.connect(self.next_show)
        self.save_button = QPushButton(text="Save")
        self.save_button.clicked.connect(self.save)

        self.index_lineedit = QLineEdit(str(self.index))
        self.index_lineedit.editingFinished.connect(self.go_and_show)

        hbox.addWidget(self.prev_button)
        hbox.addWidget(self.next_button)
        hbox.addWidget(self.index_lineedit)
        hbox.addWidget(self.save_button)

        grid.addWidget(self.datafile_lineedit, 0, 1)
        grid.addWidget(self.select_file_button, 0, 2)
        grid.addWidget(self.setup_button, 0, 3)
        grid.addWidget(self.userdict_filename_lineedit, 1, 1, 1, 3)
        grid.addWidget(self.original_textedit, 2, 1, 1, 3)
        grid.addWidget(self.splited_textedit, 3, 1, 1, 3)
        grid.addWidget(self.input_tokens_lineedit, 4, 1, 1, 3)
        grid.addWidget(self.userdict_textedit, 1, 4, 4, 1)

        grid.addLayout(hbox, 5, 0, 1, 4)
        grid.addWidget(self.end_button, 5, 4)

        # 단축키
        self.save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.save_shortcut.activated.connect(self.save)
        self.quit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.quit_shortcut.activated.connect(self.quit)
        self.prev_shortcut = QShortcut(QKeySequence("Ctrl+["), self)
        self.prev_shortcut.activated.connect(self.prev_show)
        self.next_shortcut = QShortcut(QKeySequence("Ctrl+]"), self)
        self.next_shortcut.activated.connect(self.next_show)
        self.backspace = QShortcut(QKeySequence("Ctrl+Backspace"), self)
        self.backspace.activated.connect(self.delete_last_one)

        self.setWindowTitle("test")
        self.setGeometry(300, 300, 800, 400)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, "Open file", "./")
        self.datafile_lineedit.setText(fname[0])

    def setup(self):
        data_path = self.datafile_lineedit.text()
        if not data_path:
            return

        self.dir_path, _ = path.split(data_path)
        self.userdict_path = path.join(
            self.dir_path, self.userdict_filename_lineedit.text()
        )

        if not path.isfile(self.userdict_path):
            with open(self.userdict_path, mode="w", encoding="utf-8",) as _:
                pass

        with open(self.userdict_path, mode="r", encoding="utf-8",) as f:
            self.userdict = [l[:-1] for l in f.readlines()]
        self.data = read_excel(data_path, engine="openpyxl")
        self.show_line()

    def show_line(self):
        original, _, pynori_splited = self.data.iloc[self.index]
        pynori_splited = " ".join(str_to_list(pynori_splited))

        self.original_textedit.setText(original)
        self.splited_textedit.setText(pynori_splited)
        self.index_lineedit.setText(str(self.index))
        self.userdict_textedit.setText("\n".join(self.userdict))

    def prev_show(self):
        if self.data is None:
            return
        self.index = max(0, self.index - 1)
        self.show_line()

    def next_show(self):
        if self.data is None:
            return
        self.index = min(len(self.data) - 1, self.index + 1)
        self.show_line()

    def go_and_show(self):
        if self.data is not None and self.index_lineedit.text().isdigit():
            self.index = min(
                max(int(self.index_lineedit.text()), 0), len(self.data) - 1
            )
            self.show_line()

    def add_userdict(self):
        pre_token = self.input_tokens_lineedit.text().strip()
        if not pre_token:
            return
        self.userdict.insert(0, pre_token)

        self.input_tokens_lineedit.setText("")
        self.userdict_textedit.setText("\n".join(self.userdict))

    def save(self):
        if self.userdict_path is not None:
            with open(self.userdict_path, mode="w", encoding="utf-8",) as f:
                for token in self.userdict:
                    f.write(token + "\n")

    def delete_last_one(self):
        del self.userdict[0]
        self.userdict_textedit.setText("\n".join(self.userdict))

    def quit(self):
        self.save()
        QCoreApplication.instance().quit()
