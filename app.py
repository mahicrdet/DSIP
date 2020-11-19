import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5 import QtWidgets as qw
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from git import Repo
import os

def dialog():
    mbox = QMessageBox()
    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    mbox.exec_()

def dialog_newproj():
    mbox = QMessageBox()
    mbox.setText("select project directory")
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    mbox.exec_()

def pick_new(event):
    dialog = QFileDialog()
    folder_path = dialog.getExistingDirectory(None, "Select Folder")
    return folder_path

def create_newproj(dir):
    os.makedirs(dir, exist_ok=True)
    os.makedirs(dir+'/codebase/python_src')
    os.makedirs(dir+'/artifacts/configs')
    os.makedirs(dir + '/artifacts/models')
    os.makedirs(dir + '/codebase/inference_lib')
    os.makedirs(dir + '/codebase/Notebooks')


def gitClone(url, repo_dir):
    Repo.clone_from(url, repo_dir)

def page1():
    w = QWidget()
    w.resize(1180, 760)
    w.setWindowTitle("MlPlatform")

    label = QLabel(w)
    label.setText("<h2>Data Platform Community</h2>")
    label.setFont(QFont('Arial', 12))
    label.move(60, 200)
    label.show()

    btn = QPushButton(w)
    btn.setText('Clone a ML Project')
    btn.move(60, 250)
    btn.resize(480, 75)
    btn.setFont(QFont('Arial', 12))
    btn.show()
    btn.clicked.connect(dialog)

    btn = QPushButton(w)
    btn.setText('Open ML Project')
    btn.move(60, 328)
    btn.resize(480, 75)
    btn.setFont(QFont('Arial', 12))
    btn.show()
    btn.clicked.connect(dialog)

    btn = QPushButton(w)
    btn.setText('Create New ML Project')
    btn.frameSize()
    btn.move(60, 406)
    btn.resize(480, 75)
    btn.setFont(QFont('Arial', 12))
    btn.show()
    btn.clicked.connect(pick_new)
    return w


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = page1()
    w.show()
    sys.exit(app.exec_())
    #Qtcore.Qobject
