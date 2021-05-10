import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class TranScreen:
    def __init__(self):
        super().__init__()
        # ---------------------------label--------------------------
        lh = QLabel('Fund Transaction Mechanism')
        lh.setFont(QFont('jokerman', 16))
        l1 = QLabel('Enter Card Number:')
        l2 = QLabel('Enter Pin:')
        l3 = QLabel('Enter Bank:')
        l4 = QLabel('Enter Acc. Name:')
        l5 = QLabel('Enter Acc. Number:')
        l6 = QLabel('Acc. type:')
        l7 = QLabel('Enter Amount:')
        l8 = QLabel('Payment details:')
        # ----------------------------entry-------------------------
        form.addRow(lh)
        e1 = QLineEdit()
        form.addRow(l1, e1)
        e2 = QLineEdit()
        e2.setMaxLength(4)      # limit number of entry
        e2.setEchoMode(QLineEdit.PasswordEchoOnEdit)       # make entry invisible
        form.addRow(l2, e2)
        cb = QComboBox()
        cb.setFixedSize(110, 20)
        cb.addItems(['First Bank', 'Zenith', 'Sterling'])
        form.addRow(l3, cb)
        e3 = QLineEdit()
        form.addRow(l4, e3)
        e4 = QLineEdit()
        form.addRow(l5, e4)
        at = QHBoxLayout()
        r1 = QRadioButton('Current')
        r1.setChecked(True)     # to select the button by default.
        at.addWidget(r1)
        r2 = QRadioButton('Savings')
        r2.setChecked(False)        # to select the button by default.
        at.addWidget(r2)
        form.addRow(l6, at)
        e5 = QLineEdit()
        form.addRow(l7, e5)
        t1 = QTextEdit()
        form.addRow(l8, t1)
        # --------------------create progressbar--------------------
        self.bar = QProgressBar()
        self.bar.resize(300, 50)
        self.bar.setValue(0)
        form.addRow(self.bar)
        # -------------------------buttons-------------------------
        b1 = QPushButton(clicked=start)
        b1.setFixedSize(30, 30)
        b1.setIcon(QIcon(QPixmap('C:/Users/Hp/Pictures/Programming Tools/gui/forward.png')))
        b1.setIconSize(QSize(30, 30))

        b2 = QPushButton('Cancel', clicked=stop)
        b2.setFixedSize(50, 30)
        form.addRow(b1, b2)

# --------------------define button functions--------------------
def start(self):
    count = 0
    while count < 100:
        count += 0.0001
        self.bar.setValue(count)
    self.bar.setValue(0)

def stop(self):
    self.bar.setValue(0)

app = QApplication(sys.argv)
app.setStyle("Fusion")
qp = QPalette()
qp.setColor(QPalette.Window, Qt.cyan)
qp.setColor(QPalette.Button, Qt.gray)
app.setPalette(qp)
Ftm = QWidget()
Ftm.setWindowTitle('ftm')
Ftm.setWindowIcon(QIcon('C:/Users/Hp/Pictures/Personal Images/IME Logo.jpg'))
Ftm.resize(300, 300)
Ftm.setFont(QFont('simsun', 12))
vb = QVBoxLayout(Ftm)

# -------------------------menu bar-------------------------
def about():
    msg = QMessageBox.about(
        Ftm, 'About', 'Created by Oyelegbin Philip K.\n(c)2020\nmail: philipoyelegbin@gmail.com')

menu = QMenuBar()
vb.addWidget(menu)
help = menu.addMenu('Help')
help.addAction('About', about)
help.addAction('Exit', Ftm.close)

# ---------creating frames to hold widget together----------
gb = QGroupBox()
vb.addWidget(gb)
form = QFormLayout(gb)

Ts = TranScreen()
Ftm.show()
sys.exit(app.exec_())