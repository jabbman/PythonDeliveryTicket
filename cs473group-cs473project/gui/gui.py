import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import PyQt5.QtWebEngineWidgets as web
from PyQt5.QtCore import *
from gui.combobox_search import ExtendedComboBox
from datetime import datetime
import config

if config.platform == 'pi':
    from gui.main_window_driver import Ui_MainWindow
else:
    from gui.main_window_office import Ui_MainWindow


class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self, customers,  ticketClass, sync, parent = None, name=None):
        super(MainView, self).__init__(parent)
        self.Ticket = ticketClass
        self.setupUi(self)
        self.currentTicket = None
        self.date.setDateTime(QDateTime.currentDateTime())
        
        #set up event handlers for each button. if prnt button is clicked call self.printTicket etc.
        self.submit.clicked.connect(self.newTicket)            
        self.prnt.setEnabled(False)
        self.prnt.clicked.connect(self.printTicket)            
        self.sync.clicked.connect(sync)            
        self.clear.clicked.connect(self.clearForm)            
        self.customerList = customers

        self.ticketList = ticketClass.getTicketList()
        self.ticketClass = ticketClass
        self.customers = ExtendedComboBox(self.gridLayoutWidget)
        self.customers.setObjectName("customers")
        self.gridLayout_2.addWidget(self.customers, 1, 1, 1, 1)
        self.customers.addItems(['new'] + [c['name'] for c in customers])
        self.paidState.addItems(['cash','charge','check'])
        self.customers.currentIndexChanged.connect(self.onCustomerSelect)
        self.calcFields = [self.smallbagsQ,self.smallbagsP,self.bigbagsQ,self.bigbagsP,self.smallblockQ,
            self.smallblockP,self.largeblockQ,self.largeblockP,self.vendorQ,self.vendorP,self.storageQ,
            self.storageP,self.freightQ,self.freightP,self.otherQ,self.otherP]
        for field in self.calcFields:
            field.valueChanged.connect(self.calculateTotal)

        #for office version
        if config.platform != 'pi':
            self.view.clicked.connect(self.viewTicket)            
            self.tickets.setHorizontalHeaderLabels(('Tickets',))
            self.tickets.setRowCount(len(self.ticketList))
            for i, ticket in enumerate(self.ticketList):
                self.tickets.setItem(i,0, QTableWidgetItem(ticket['desc']))

    def viewTicket(self):
        """used in office mode, if a ticket gets selected when the View Ticket gets clicked, 
        the ticket information is loaded into the form
        """
        ticketFile = self.ticketList[self.tickets.currentRow()]['fullpath']
        ticket = self.Ticket.getTicket(ticketFile)
        ticketDetails = ticket.getDetails()
        i = self.customers.findText(ticketDetails['customerName'])
        if i == -1:
            self.newCustomer.setText(ticketDetails['customerName'])
            self.customers.setCurrentIndex(0)
        else:
            self.customers.setCurrentIndex(i)
            self.newCustomer.clear()

        date = datetime.strptime( ticketDetails['date'], '%m-%d-%Y %H:%M')
        self.date.setDateTime(QDateTime(date.year, date.month, date.day, date.hour, date.minute))
        self.paidState.setCurrentIndex(self.paidState.findText(ticketDetails['paidState']))
        self.checkNum.setText(ticketDetails['checkNum'])
        self.comment.setText(ticketDetails['comment'])
        self.smallbagsQ.setValue(ticketDetails['smallbagsQ'])
        self.smallbagsP.setValue(ticketDetails['smallbagsP'])
        self.bigbagsQ.setValue(ticketDetails['bigbagsQ'])
        self.bigbagsP.setValue(ticketDetails['bigbagsP'])
        self.smallblockQ.setValue(ticketDetails['smallblockQ'])
        self.smallblockP.setValue(ticketDetails['smallblockP'])
        self.largeblockQ.setValue(ticketDetails['largeblockQ'])
        self.largeblockP.setValue(ticketDetails['largeblockP'])
        self.vendorQ.setValue(ticketDetails['vendorQ'])
        self.vendorP.setValue(ticketDetails['vendorP'])
        self.storageQ.setValue(ticketDetails['storageQ'])
        self.storageP.setValue(ticketDetails['storageP'])
        self.freightQ.setValue(ticketDetails['freightQ'])
        self.freightP.setValue(ticketDetails['freightP'])
        self.otherQ.setValue(ticketDetails['otherQ'])
        self.otherP.setValue(ticketDetails['otherP'])
        self.total.setValue(ticketDetails['total'])
    
    def displayTicket(self):
        """In pi mode, this displays the png version of the pdf"""
        ticketPng = self.currentTicket.displayTicket()
        pixmap = QPixmap(ticketPng)
        self.image.setGeometry(10, 10, 300, 100)
        self.image.setPixmap(pixmap)


    def newTicket(self):
        """when the submit button gets clicked this method is called to generate a Python receipt"""
        ticket = self.getTicket()
        self.currentTicket = ticket
        ticket.writeTicket()
        #enable the print button since a ticket has been submitted.
        self.prnt.setEnabled(True)
        if config.platform != 'pi':
            self.updateTicketList()
            ticket.displayTicket()
        else:
            self.displayTicket()
    
    def updateTicketList(self):
        """once a new ticket is submitted update the ticket list in office mode"""
        self.tickets.clear()
        self.tickets.setHorizontalHeaderLabels(('Tickets',))
        self.ticketList = self.ticketClass.getTicketList()
        self.tickets.setRowCount(len(self.ticketList))
        for i, ticket in enumerate(self.ticketList):
            self.tickets.setItem(i,0, QTableWidgetItem(ticket['desc']))


    #print button needs to disabled until ticket is submitted
    def printTicket(self):
        if self.currentTicket is not None:
            self.currentTicket.printTicket()

    def getTicket(self):
        """Takes the form values and passes it into a new ticket instance"""
        date = self.date.dateTime().toPyDateTime().strftime('%m-%d-%Y %H:%M')
        customerName = str(self.newCustomer.text()).strip()
        if len(customerName) == 0:
            if  self.customers.currentIndex() == 0:
                name = 'noname'
            else:
                name = self.customerList[self.customers.currentIndex()-1]['name']
        else:
            name = customerName

        ticketNum = self.Ticket.getTicketNum(self.date.dateTime().toPyDateTime())
        return self.Ticket(customerName,date,ticketNum,self.paidState.currentText(),self.comment.text(),
            self.smallbagsQ.value(),self.smallbagsP.value(),self.bigbagsQ.value(),self.bigbagsP.value(),
            self.smallblockQ.value(),self.smallblockP.value(),self.largeblockQ.value(),
            self.largeblockP.value(),self.vendorQ.value(),self.vendorP.value(),self.storageQ.value(),
            self.storageP.value(),self.freightQ.value(),self.freightP.value(),self.otherQ.value(),
            self.otherP.value(),self.total.value(),str(self.checkNum.text()))


    def clearForm(self):
        for i,field in enumerate(self.calcFields[::2]):
            field.setValue(0)
            self.calcFields[i*2+1].setValue(0.0)
        self.customers.setCurrentIndex(0)
        self.paidState.setCurrentIndex(0)


    def onCustomerSelect(self):
        """update the prices/quantities based on customer selected"""
        i = self.customers.currentIndex() 
        if i != 0:
            #self.smallbagsQ.setValue(self.customerList[i-1]['smallbagsQ'])
            self.smallbagsP.setValue(self.customerList[i-1]['smallbagsP'])
            #self.bigbagsQ.setValue(self.customerList[i-1]['bigbagsQ'])
            self.bigbagsP.setValue(self.customerList[i-1]['bigbagsP'])
            #self.smallblockQ.setValue(self.customerList[i-1]['smallblockQ'])
            self.smallblockP.setValue(self.customerList[i-1]['smallblockP'])
            #self.largeblockQ.setValue(self.customerList[i-1]['largeblockQ'])
            self.largeblockP.setValue(self.customerList[i-1]['largeblockP'])
            #self.vendorQ.setValue(self.customerList[i-1]['vendorQ'])
            self.vendorP.setValue(self.customerList[i-1]['vendorP'])
            #self.storageQ.setValue(self.customerList[i-1]['storageQ'])
            self.storageP.setValue(self.customerList[i-1]['storageP'])
            #self.freightQ.setValue(self.customerList[i-1]['freightQ'])
            self.freightP.setValue(self.customerList[i-1]['freightP'])
            #self.otherQ.setValue(self.customerList[i-1]['otherQ'])
            self.otherP.setValue(self.customerList[i-1]['otherP'])
            self.calculateTotal()


    def calculateTotal(self):
        total = 0
        for i,field in enumerate(self.calcFields[::2]):
            total += field.value() * self.calcFields[i*2+1].value()
        self.total.setValue(total)

        


