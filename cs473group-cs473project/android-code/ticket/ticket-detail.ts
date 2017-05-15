import { Component } from '@angular/core';
import { NavParams } from 'ionic-angular';
import { Ticket } from './ticket';

@Component({
  selector: 'ticket-details',
  template: `
    <ion-header>
      <ion-navbar>
        <ion-title>Ticket Details</ion-title>
      </ion-navbar>
    </ion-header>

    <ion-content>
        <ion-card>
            <ion-item>
                <ion-note item-left color="primary">
                    Ticket Number
                </ion-note>
                <p item-right>
                    {{ticket.ticketNum}}
                </p>
            </ion-item>
            <ion-item>
                <ion-note item-left color="primary">
                    Date
                </ion-note>
                <p item-right>
                    {{ticket.ticketDate}}
                </p>
            </ion-item>
            <ion-item>
                <ion-note item-left color="primary">
                    Customer
                </ion-note>
                <p item-right>
                    {{ticket.customerName}}
                </p>
            </ion-item>
            <ion-item>
                <ion-note item-left color="primary">
                    Payment Type
                </ion-note>
                <p item-right>
                    {{ticket.paymentType}}
                </p>
            </ion-item>
            <ion-item *ngIf="ticket.isCheck">
                <ion-note item-left >
                    Check Number
                </ion-note>
                <p item-right>
                    {{ticket.checkNumber}}
                </p>
            </ion-item>
            <ion-item>
                <ion-note item-left color="primary">
                    Comment
                </ion-note>
                <p item-right>
                    {{ticket.comment}}
                </p>
            </ion-item>
            <ion-item>
                <ion-note item-left>
                    7 lb bags
                </ion-note>
                <p item-right>
                    {{ticket.bag7.qty}} at \${{ticket.bag7.price}}
                </p>
            </ion-item>
            <ion-item>
                <ion-note item-left>
                    22 lb bags
                </ion-note>
                <p item-right>
                    {{ticket.bag22.qty}} at \${{ticket.bag22.price}}
                </p>
            </ion-item>
            <ion-item>
                <ion-note item-left>
                   10 blocks 
                </ion-note>
                <p item-right>
                    {{ticket.block10.qty}} at \${{ticket.block10.price}}
                </p>
            </ion-item>
            <ion-item>
                <ion-note item-left>
                    Rent
                </ion-note>
                <p item-right>
                    {{ticket.vendor.qty}} at \${{ticket.vendor.price}}
                </p>
            </ion-item>
            <ion-item>
                <ion-note item-left>
                    Storage
                </ion-note>
                <p item-right>
                    {{ticket.storage.qty}} at \${{ticket.storage.price}}
                </p>
            </ion-item>
            <ion-item>
                <ion-note item-left>
                    Freight
                </ion-note>
                <p item-right>
                    {{ticket.freight.qty}} at \${{ticket.freight.price}}
                </p>
            </ion-item>
            <ion-item>
                <ion-note item-left>
                    Other
                </ion-note>
                <p item-right>
                    {{ticket.other.qty}} at \${{ticket.other.price}}
                </p>
            </ion-item>
            <ion-item>
                <ion-note item-left color="primary">
                    Total
                </ion-note>
                <p item-right>
                    \${{ticket.total}}
                </p>
            </ion-item>
            <button ion-button (click)="printTicket()">Print Receipt</button>
            <button ion-button (click)="deleteTicket()">Delete</button>
        </ion-card>
    </ion-content>

  `
})
export class TicketDetails {
    
    private ticket : Ticket;

    constructor(private navParams: NavParams){
        this.ticket = navParams.get('ticket');
    }

    printTicket(){
    }

    deleteTicket(){
    }
}

