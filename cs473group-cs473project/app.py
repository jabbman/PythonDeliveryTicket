import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from utils import getCustomers, sync
from ticket import Ticket
from config import *
from gui.gui import MainView


def main():
    customers = getCustomers()
    if not os.path.exists(TICKETS_DIR): 
        os.mkdir(TICKETS_DIR, 0o755)
    if not os.path.exists(LATEX_PATH + '/temp'): 
        os.mkdir(LATEX_PATH + '/temp', 0o755)
    app = QtWidgets.QApplication (sys.argv)
    mainWindow = MainView(customers,Ticket, sync)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
