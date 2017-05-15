from datetime import datetime
import os
import subprocess
from shutil import copyfile
import itertools
from utils import printFile, sanitizeInput
from config import *
from latex_template import LATEX_TEMP


class Ticket:

    def __init__(self, customerName,  date, ticketNum, paidState, comment, smallbagsQ, smallbagsP,  
            bigbagsQ, bigbagsP, smallblockQ, smallblockP ,
            largeblockQ, largeblockP, vendorQ, vendorP,  storageQ, storageP, freightQ, 
            freightP, otherQ, otherP, total, checkNum):
        self.customerName = sanitizeInput(customerName)
        self.date = date
        self.ticketNum = ticketNum
        self.paidState = paidState
        self.checkNum = '------' if len(checkNum) == 0 else checkNum
        self.comment = '------' if len(comment) == 0 else sanitizeInput(comment)
        self.smallbagsQ = smallbagsQ
        self.smallbagsP = smallbagsP
        self.bigbagsQ = bigbagsQ
        self.bigbagsP = bigbagsP
        self.smallblockQ = smallblockQ
        self.filePath = None
        self.smallblockP = smallblockP
        self.largeblockQ = largeblockQ
        self.largeblockP = largeblockP
        self.vendorQ = vendorQ
        self.vendorP = vendorP
        self.storageQ = storageQ
        self.storageP = storageP
        self.freightQ = freightQ
        self.freightP = freightP
        self.otherQ = otherQ
        self.otherP = otherP
        self.total = total
        self.calcFields = [self.smallbagsQ,self.smallbagsP,self.bigbagsQ,self.bigbagsP,self.smallblockQ,
            self.smallblockP,self.largeblockQ,self.largeblockP,self.vendorQ,self.vendorP,self.storageQ,
            self.storageP,self.freightQ,self.freightP,self.otherQ,self.otherP]
    
    def getDetails(self):
        """a getter method returns all the variables inside an instance"""
        return vars(self)

    def writeTicket(self):
        """Writes the instance to the hard drive as a python receipt."""
        #py file hasn't been created yet so need to create file
        fullpath = self.getTicketPath()
        ticketLoc = fullpath + ("/%s.py" % self.ticketNum)
        with open(ticketLoc, 'w') as f:
            f.write(TICKET_FORMAT.format(customerName=self.customerName, date = self.date ,
                ticketNum = self.ticketNum ,paidState = self.paidState ,checkNum = self.checkNum ,
                comment = self.comment ,smallbagsQ = self.smallbagsQ ,
                smallbagsP = self.smallbagsP ,bigbagsQ = self.bigbagsQ ,
                bigbagsP = self.bigbagsP ,smallblockQ = self.smallblockQ ,
                smallblockP = self.smallblockP ,largeblockQ = self.largeblockQ ,
                largeblockP = self.largeblockP ,vendorQ = self.vendorQ ,vendorP = self.vendorP ,
                storageQ = self.storageQ ,storageP = self.storageP ,freightQ = self.freightQ ,
                freightP = self.freightP ,otherQ = self.otherQ ,
                otherP = self.otherP ,total = self.total))
    

    def getTicketPath(self):
        """Used to get the directory path of the ticket to be created.
        If path does not exist it creates it
        """
        dt = datetime.strptime(self.date, '%m-%d-%Y %H:%M')
        path = '/{year}/{month}'.format(year=dt.year, month=dt.strftime('%B'))
        fullpath = TICKETS_DIR  + path
        if not os.path.exists(fullpath): 
            os.makedirs(fullpath, 0o755)
        return fullpath



    def ticketToPdf(self):
        """This method calls writeTicket to generate the Python receipt
        it then calls pdflatex to generate the pdf file
        """
        if not os.path.exists(self.ticketNum): #py file hasn't been created yet so need to create file
            self.writeTicket()

        #create a new stripped tex file that mirrors StripedTicket.tex except with the correct ticket details
        #store the file in the temp directory inside LatexTicketTemplate
        strippedLatex = LATEX_PATH + '/temp/' + self.ticketNum + '.tex'
        date = datetime.strptime(self.date, '%m-%d-%Y %H:%M').strftime('%B %d %Y')
        calcs = []
        colorFields = [1,3,4,5,6,7]
        isColor = False
        for i,field in enumerate(self.calcFields[::2]):
            calcs.append(field)
            calcs.append(self.calcFields[i*2+1])
            r = self.calcFields[i*2+1]*field
            calcs.append(r)
            if r > 0: 
                isColor = True
            if i in colorFields:
                if i == 3:
                    r = self.calcFields[i*2+2]*self.calcFields[i*2+3]
                    if r > 0:
                        isColor = True
                    calcs.append('white' if not isColor else 'black')
                else:
                    calcs.append('white' if not isColor else 'black')
                isColor = False

        formatList = [self.customerName, date, self.ticketNum.replace('_','\_') ,
                self.paidState , self.checkNum , self.comment]
        formatList += calcs
        formatList.append(self.total)

                
        with open(strippedLatex, 'w') as f: 
            f.write(LATEX_TEMP%tuple(formatList))


        #copy the TicketTemplate.tex file to the temp directory 
        #modify line 9 with the correct tex file on the copied templte file, replacing default StripedTicket name
        copyfile(LATEX_PATH + TEMPLATE_LATEX_FILE, LATEX_PATH + '/temp/template' + self.ticketNum + '.tex')
        f = open(LATEX_PATH + '/temp/template' + self.ticketNum + '.tex', 'r')
        data = f.readlines()
        data[8] = '\\input{temp/%s}' % (self.ticketNum)
        f.close()
        f = open(LATEX_PATH + '/temp/template' + self.ticketNum + '.tex', 'w')
        f.writelines(data)
        f.close()


        pdf =  self.ticketNum + '.pdf'
        #call pdf.sh bash script to create the pdf
        cmd = 'bash pdf.sh {latexFile} {pdfFile}'.format(latexFile='temp/template' + self.ticketNum + '.tex', pdfFile= 'temp/template'+pdf)
        os.system(cmd)
        return LATEX_PATH + 'temp/template' + pdf


    def printTicket(self):
        if self.filePath is None:
            self.filePath = self.ticketToPdf()
        printFile(self.filePath)

    def displayTicket(self):
        """This method converts a ticket instance to a pdf. It then takes that filepath
        and depending on which platform it's own, either converts it into a png
        which can be shown or displays it as pdf using the xpdf command.
        """
        self.filePath = self.ticketToPdf()
        self.filePath = self.ticketToPdf()
        if platform == 'pi':
            pngFile = self.filePath[:-4] + '.png'
            cmd = 'convert -flatten -density 60 {pdf} {png}'.format(pdf=self.filePath, png=self.filePath[:-4] + '.png')
            os.system(cmd)
            return pngFile 
        else:
            cmd = 'xpdf {pdf}'.format(pdf=self.filePath)
            subprocess.Popen(cmd, shell=True)

    @staticmethod
    def getTicket(ticketPath):
        """Parses an existing Python ticket into a Ticket instance.

        ticketPath -- the path of the way the python ticket file is located in the directory
        """
        ticketLoc = ticketPath
        ticketLoc =  ticketPath
        f = open(ticketLoc, "r")
        ns = {}
        exec(f.read(), ns)
        ticket = Ticket(ns['Customer'], ns['Date'], ns['TicketNum'], ns['PaidState'], ns['Comment'], ns['SmallBags'], ns['PriceSmallBags'],
                ns['BigBags'], ns['PriceBigBags'], ns['SmallBlock'], ns['PriceSmallBlock'], ns['LargeBlock'], ns['PriceLargeBlock'],
                ns['VenderRent'], ns['RateVenderRent'], ns['Storage'], ns['PriceStorage'], ns['Frieght'], ns['PriceFrieght'], ns['Other'],
                ns['PriceOther'], ns['TicketTotal'], ns['CheckNum'])
        f.close()
        return ticket


    @staticmethod
    def getTicketList():
        """Parses the ticket directory and returns a list of all tickets. Only used in office mode."""
        fullpathTickets = []
        for root, dirs, files in os.walk(TICKETS_DIR):
            #ignore hidden files cause they shouldnt be there..
            files = [f for f in files if not f[0] == '.']
            dirs[:] = [d for d in dirs if not d[0] == '.']

            fullPathFiles = map(lambda name : os.path.join(root, name), files)
            fullpathTickets.append(fullPathFiles)
        tickets = []
        for ticket in list(itertools.chain(*fullpathTickets)):
            tickets.append(dict(fullpath=ticket,desc=' '.join(ticket.split('/')[-1].split('_')[:-1])))

        #sort by date
        tickets.sort(key = lambda ticket: datetime.strptime(ticket['fullpath'].split('/')[-1].split('_')[0], DATE_FORMAT), 
                    reverse=True)
        return tickets


    @staticmethod
    def getTicketNum(date):
        """Takes the date and returns a ticket number generated from the date, 
        modify this method to control how ticket numbers appear, as of now if a driver
        submits a ticket within a minute the original ticket will get overwritten."""
        #raspberry timezone needs to be set
        return date.strftime(DATE_FORMAT)+ '_' + TRUCK_ID






