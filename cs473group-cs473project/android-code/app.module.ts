import { NgModule, ErrorHandler } from '@angular/core';
import { IonicApp, IonicModule, IonicErrorHandler } from 'ionic-angular';
import { App } from './app.component';
import { Menu } from './menu/menu';
import { NewTicket } from './ticket/new-ticket';
import { TicketDetails } from './ticket/ticket-detail';
import { TicketList } from './ticket/ticket-list';

@NgModule({
  declarations: [
    App,
    NewTicket,
    TicketDetails,
    TicketList,
    Menu
  ],
  imports: [
    IonicModule.forRoot(App)
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    App,
    NewTicket,
    TicketDetails,
    TicketList,
    Menu
  ],
  providers: [{provide: ErrorHandler, useClass: IonicErrorHandler}]
})
export class AppModule {}
