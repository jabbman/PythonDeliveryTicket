import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { NewTicket } from '../ticket/new-ticket';
import { TicketList } from '../ticket/ticket-list';
import { App } from 'ionic-angular';

@Component({
  selector: 'menu',
  template: `
  <ion-content padding>
    <div class="row">
        <button  (click)="goTo('new-ticket')" ion-button block>New Ticket</button>
    </div>
    <div class="row">
        <button ion-button (click)="syncTickets()" block>Sync Tickets</button>
    </div>
    <div class="row">
        <button  (click)="goTo('ticket-list')" ion-button block>View Tickets</button>
    </div>
  </ion-content>
  `
})
export class Menu {
  NewTicketPage: any = NewTicket;
  TicketListPage: any = TicketList;

  constructor(public navCtrl: NavController,
              public appCtrl: App) {
    
  }

  goTo(to) {
      if (to === 'new-ticket')
        this.appCtrl.getRootNav().push(this.NewTicketPage);
      else
        this.appCtrl.getRootNav().push(this.TicketListPage);
  }

}
