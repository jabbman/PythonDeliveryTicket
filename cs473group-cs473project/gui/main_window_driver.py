# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/driver.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 560)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 248, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAcceptDrops(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)
        self.paidState = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.paidState.setObjectName("paidState")
        self.gridLayout_2.addWidget(self.paidState, 3, 1, 1, 1)
        self.checkNum = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.checkNum.setObjectName("checkNum")
        self.gridLayout_2.addWidget(self.checkNum, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.newCustomer = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.newCustomer.setText("")
        self.newCustomer.setPlaceholderText("")
        self.newCustomer.setObjectName("newCustomer")
        self.gridLayout_2.addWidget(self.newCustomer, 2, 1, 1, 1)
        self.comment = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.comment.setPlaceholderText("")
        self.comment.setObjectName("comment")
        self.gridLayout_2.addWidget(self.comment, 6, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 6, 0, 1, 1)
        self.date = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        self.date.setObjectName("date")
        self.gridLayout_2.addWidget(self.date, 0, 1, 1, 1)
        self.customers = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.customers.setObjectName("customers")
        self.gridLayout_2.addWidget(self.customers, 1, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 200, 381, 331))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.otherQ = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.otherQ.setMaximum(1000000)
        self.otherQ.setObjectName("otherQ")
        self.gridLayout_3.addWidget(self.otherQ, 8, 1, 1, 1)
        self.otherP = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.otherP.setMaximum(10000.0)
        self.otherP.setObjectName("otherP")
        self.gridLayout_3.addWidget(self.otherP, 8, 2, 1, 1)
        self.smallbagsQ = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.smallbagsQ.setMaximum(1000000)
        self.smallbagsQ.setObjectName("smallbagsQ")
        self.gridLayout_3.addWidget(self.smallbagsQ, 1, 1, 1, 1)
        self.smallbagsP = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.smallbagsP.setMaximum(10000.0)
        self.smallbagsP.setObjectName("smallbagsP")
        self.gridLayout_3.addWidget(self.smallbagsP, 1, 2, 1, 1)
        self.bigbagsP = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.bigbagsP.setMaximum(10000.0)
        self.bigbagsP.setObjectName("bigbagsP")
        self.gridLayout_3.addWidget(self.bigbagsP, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.storageP = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.storageP.setMaximum(10000.0)
        self.storageP.setObjectName("storageP")
        self.gridLayout_3.addWidget(self.storageP, 6, 2, 1, 1)
        self.storageQ = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.storageQ.setMaximum(1000000)
        self.storageQ.setObjectName("storageQ")
        self.gridLayout_3.addWidget(self.storageQ, 6, 1, 1, 1)
        self.smallblockP = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.smallblockP.setMaximum(10000.0)
        self.smallblockP.setObjectName("smallblockP")
        self.gridLayout_3.addWidget(self.smallblockP, 3, 2, 1, 1)
        self.bigbagsQ = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.bigbagsQ.setMaximum(1000000)
        self.bigbagsQ.setObjectName("bigbagsQ")
        self.gridLayout_3.addWidget(self.bigbagsQ, 2, 1, 1, 1)
        self.vendorP = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.vendorP.setMaximum(10000.0)
        self.vendorP.setObjectName("vendorP")
        self.gridLayout_3.addWidget(self.vendorP, 5, 2, 1, 1)
        self.largeblockP = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.largeblockP.setMaximum(10000.0)
        self.largeblockP.setObjectName("largeblockP")
        self.gridLayout_3.addWidget(self.largeblockP, 4, 2, 1, 1)
        self.freightP = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.freightP.setMaximum(10000.0)
        self.freightP.setObjectName("freightP")
        self.gridLayout_3.addWidget(self.freightP, 7, 2, 1, 1)
        self.smallblockQ = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.smallblockQ.setMaximum(1000000)
        self.smallblockQ.setObjectName("smallblockQ")
        self.gridLayout_3.addWidget(self.smallblockQ, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 7, 0, 1, 1)
        self.vendorQ = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.vendorQ.setMaximum(1000000)
        self.vendorQ.setObjectName("vendorQ")
        self.gridLayout_3.addWidget(self.vendorQ, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)
        self.freightQ = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.freightQ.setMaximum(1000000)
        self.freightQ.setObjectName("freightQ")
        self.gridLayout_3.addWidget(self.freightQ, 7, 1, 1, 1)
        self.largeblockQ = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.largeblockQ.setMaximum(1000000)
        self.largeblockQ.setObjectName("largeblockQ")
        self.gridLayout_3.addWidget(self.largeblockQ, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 8, 0, 1, 1)
        self.total = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.total.setReadOnly(True)
        self.total.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.total.setMaximum(999999999.99)
        self.total.setObjectName("total")
        self.gridLayout_3.addWidget(self.total, 9, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 9, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(260, 10, 131, 181))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.submit = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.submit.setObjectName("submit")
        self.gridLayout.addWidget(self.submit, 0, 0, 1, 1)
        self.clear = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.clear.setObjectName("clear")
        self.gridLayout.addWidget(self.clear, 2, 0, 1, 1)
        self.prnt = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.prnt.setObjectName("prnt")
        self.gridLayout.addWidget(self.prnt, 1, 0, 1, 1)
        self.sync = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.sync.setObjectName("sync")
        self.gridLayout.addWidget(self.sync, 3, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(400, 10, 381, 521))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.image = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.image.setText("")
        self.image.setObjectName("image")
        self.gridLayout_4.addWidget(self.image, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.clear.clicked.connect(self.newCustomer.clear)
        self.clear.clicked.connect(self.checkNum.clear)
        self.clear.clicked.connect(self.comment.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.newCustomer, self.paidState)
        MainWindow.setTabOrder(self.paidState, self.checkNum)
        MainWindow.setTabOrder(self.checkNum, self.comment)
        MainWindow.setTabOrder(self.comment, self.smallbagsQ)
        MainWindow.setTabOrder(self.smallbagsQ, self.smallbagsP)
        MainWindow.setTabOrder(self.smallbagsP, self.bigbagsQ)
        MainWindow.setTabOrder(self.bigbagsQ, self.bigbagsP)
        MainWindow.setTabOrder(self.bigbagsP, self.smallblockQ)
        MainWindow.setTabOrder(self.smallblockQ, self.smallblockP)
        MainWindow.setTabOrder(self.smallblockP, self.largeblockQ)
        MainWindow.setTabOrder(self.largeblockQ, self.largeblockP)
        MainWindow.setTabOrder(self.largeblockP, self.vendorQ)
        MainWindow.setTabOrder(self.vendorQ, self.vendorP)
        MainWindow.setTabOrder(self.vendorP, self.storageQ)
        MainWindow.setTabOrder(self.storageQ, self.storageP)
        MainWindow.setTabOrder(self.storageP, self.freightQ)
        MainWindow.setTabOrder(self.freightQ, self.freightP)
        MainWindow.setTabOrder(self.freightP, self.otherQ)
        MainWindow.setTabOrder(self.otherQ, self.otherP)
        MainWindow.setTabOrder(self.otherP, self.total)
        MainWindow.setTabOrder(self.total, self.submit)
        MainWindow.setTabOrder(self.submit, self.clear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ICEPOS"))
        self.label_3.setText(_translate("MainWindow", "Payment Type"))
        self.label_16.setText(_translate("MainWindow", "New Customer"))
        self.label.setText(_translate("MainWindow", "Date"))
        self.label_4.setText(_translate("MainWindow", "Check Number"))
        self.label_2.setText(_translate("MainWindow", "Customer"))
        self.label_17.setText(_translate("MainWindow", "Comment"))
        self.label_5.setText(_translate("MainWindow", "7lb bags"))
        self.label_11.setText(_translate("MainWindow", "Freight"))
        self.label_8.setText(_translate("MainWindow", "25lb blocks"))
        self.label_9.setText(_translate("MainWindow", "Vendor rent"))
        self.label_6.setText(_translate("MainWindow", "22lb bags"))
        self.label_7.setText(_translate("MainWindow", "10lb blocks"))
        self.label_10.setText(_translate("MainWindow", "Storage"))
        self.label_12.setText(_translate("MainWindow", "Other"))
        self.label_15.setText(_translate("MainWindow", "Total"))
        self.label_14.setText(_translate("MainWindow", "Price"))
        self.label_13.setText(_translate("MainWindow", "Quantity"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.prnt.setText(_translate("MainWindow", "Print"))
        self.sync.setText(_translate("MainWindow", "Sync"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

