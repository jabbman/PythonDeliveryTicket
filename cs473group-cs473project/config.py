CUSTOMER_CSV = './customers.csv'
TICKETS_DIR = './Tickets'
LATEX_PATH = './LatexTicketTemplate/'
TEMPLATE_LATEX_FILE = 'TicketTemplate.tex'
#for rsync
USERNAME = 'ranuka'
IP_ADDRESS = '45.55.151.100'
SERVER_PATH = './Tickets'
TRUCK_ID = 'T1'
DATE_FORMAT = '%M%H%Y%d%m'


#platform, uses a specific gui. if the platform is not the pi then it imports the office gui with the directory view
platform = 'pi'
#platform = 'office'






TICKET_FORMAT = """Customer  = "{customerName}"
Date      = "{date}"
TicketNum = "{ticketNum}"
PaidState = "{paidState}"
CheckNum  = "{checkNum}"
Comment   = "{comment}"
# Product ========================================
SmallBags       = {smallbagsQ}
PriceSmallBags  = {smallbagsP}
BigBags         = {bigbagsQ}
PriceBigBags    = {bigbagsP}
SmallBlock      = {smallblockQ}
PriceSmallBlock = {smallblockP}
LargeBlock      = {largeblockQ}
PriceLargeBlock = {largeblockP}
# Service ========================================
VenderRent      = {vendorQ}
RateVenderRent  = {vendorP}
Storage         = {storageQ}
PriceStorage    = {storageP}
Frieght         = {freightQ}
PriceFrieght    = {freightP}
Other           = {otherQ}
PriceOther      = {otherP}
# Total ==========================================
TicketTotal     = {total}
"""
