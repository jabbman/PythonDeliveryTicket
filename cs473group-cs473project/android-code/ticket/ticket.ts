export class Ticket {
    constructor(
        private customerName: String,
        private ticketDate: String,
        private paymentType: String,
        private checkNumber: String,
        private ticketNum: String,
        private comment: String,
        private bag7: {price:number,qty:number},
        private bag22: {price:number,qty:number},
        private block10: {price:number,qty:number},
        private block25: {price:number,qty:number},
        private vendor: {price:number,qty:number},
        private storage:{price:number,qty:number},
        private freight:{price:number,qty:number},
        private other: {price:number,qty:number},
        private total: number
    ){}


    get isCheck(){
        return this.paymentType === 'check';
    }

}
