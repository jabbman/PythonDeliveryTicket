import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Ticket } from './ticket';
import { TicketDetails } from './ticket-detail';
import { TICKETS } from './tickets';

@Component({
  selector: 'ticket-list',
  template: `
    <ion-header>
      <ion-navbar>
        <ion-title>Tickets</ion-title>
      </ion-navbar>
    </ion-header>

    <ion-content>
        <ion-list>
            <div *ngFor="let ticket of tickets">
                <button ion-item detail-none (click)="showTicket(ticket)">
                    <h2>{{ticket.ticketNum}}</h2>
                    <p>{{ticket.customerName}}</p>
                    <ion-note item-right>
                        {{ticket.ticketDate}}
                    </ion-note>
                </button>
            </div>
        </ion-list>
    </ion-content>

  `
})
export class TicketList {
    
    private tickets:Ticket[] = TICKETS;

    constructor(private navCtrl: NavController){
    }

    showTicket(ticket: Ticket){
        this.navCtrl.push(TicketDetails, {ticket: ticket});
    }
}
