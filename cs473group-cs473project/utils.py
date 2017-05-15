from config import CUSTOMER_CSV, IP_ADDRESS, USERNAME, SERVER_PATH, TICKETS_DIR
import re
import subprocess
import cups
import uuid
import os
import csv


def sanitizeInput(string):
    """sanitize any plaintext input so that it doesn't interfere with latex parsing"""
    return re.sub(r'[^a-zA-Z0-9\-\ ]','', string) #alphanumeric, spaces and hyphens only

def getCustomers():
    """parses the customer csv file and returns an array of dictionaries"""
    customers = []
    with open(CUSTOMER_CSV, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            customers.append(dict(name = row[0],
                        smallbagsQ = int(row[1]),
                        smallbagsP = float(row[2]),
                        bigbagsQ =  int(row[3]),
                        bigbagsP =    float(row[4]),
                        smallblockQ = int(row[5]),
                        smallblockP =  float(row[6]),
                        largeblockQ = int(row[7]),
                        largeblockP = float(row[8]),
                        vendorQ = int(row[9]),
                        vendorP = float(row[10]),
                        storageQ = int(row[11]),
                        storageP = float(row[12]),
                        freightQ = int(row[13]),
                        freightP = float(row[14]),
                        otherQ = int(row[15]),
                        otherP = float(row[16])))
    return customers


def sync():
    cmd = 'rsync -a --progress {ticket_directory} {username}@{ip_address}:{server_path}'.format(ticket_directory=TICKETS_DIR,
        username=USERNAME, ip_address=IP_ADDRESS, server_path=SERVER_PATH)
    subprocess.Popen(cmd, shell=True)

    
def printFile(fileName):
    conn = cups.Connection()
    printers = conn.getPrinters()
    printer_name = list(printers.keys())[0]
    jobName = str(uuid.uuid4())
    conn.printFile(printer_name, fileName, jobName, {})


