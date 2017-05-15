import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { CUSTOMERS } from './customers';
import { Ticket } from './ticket';
import { TicketDetails } from './ticket-detail';
import {Validators, FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'new-ticket',
  template: `
    <ion-header>
      <ion-navbar>
        <ion-title>New Ticket</ion-title>
      </ion-navbar>
    </ion-header>

    <ion-content>
        <form [formGroup]="ticketForm" (ngSubmit)="submit();">
        <ion-item>
            <ion-label>Customer</ion-label>
            <ion-select formControlName="customer">
                <ion-option [value]="new" selected="false">new</ion-option>
                <div *ngFor="let c of customers">
                    <ion-option [value]="c.name" selected="false">{{c.name}}</ion-option>
                </div>
            </ion-select>
        </ion-item>
        <ion-item *ngIf="ticketForm.value.customer === 'new'">
            <ion-input placeholder="Customer Name" formControlName="newCustomer"></ion-input>
        </ion-item>
        <ion-item>
            <ion-label>Date</ion-label>
            <ion-datetime formControlName="ticketDate" displayFormat="YYYY/MM/DD" ></ion-datetime>
        </ion-item>
        <ion-item>
            <ion-label>Payment Type</ion-label>
            <ion-select formControlName="paymentType">
                <ion-option value="check">Check</ion-option>
                <ion-option value="cash">Cash</ion-option>
                <ion-option value="credit">Credit</ion-option>
            </ion-select>
        </ion-item>
        <ion-item *ngIf="ticketForm.value.paymentType === 'check' ">
            <ion-input formControlName="checkNumber" placeholder="Check number"></ion-input>
        </ion-item>

        <ion-row>
            <ion-col offset-20>
                <ion-label color="primary">Quantity</ion-label>
            </ion-col>
            <ion-col>
                <ion-label color="primary">Price</ion-label>
            </ion-col>
        </ion-row>
   <ion-row class="item-md">
            <ion-col width-20>
                <ion-label color="primary" >7 lb bags</ion-label>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="bag7.qty" (ngModelChange)="updateTotal()" step="1"  min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="bag7.price" (ngModelChange)="updateTotal()"  step="any" min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
        </ion-row>
        <ion-row class="item-md">
            <ion-col width-20>
                <ion-label color="primary" >22 lb bags</ion-label>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="bag22.qty" (ngModelChange)="updateTotal()" step="1"  min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="bag22.price" (ngModelChange)="updateTotal()" step="any" min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
        </ion-row>
        <ion-row class="item-md">
            <ion-col width-20>
                <ion-label color="primary" >10 lb blocks</ion-label>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="block10.qty" (ngModelChange)="updateTotal()" step="1"  min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="block10.price" (ngModelChange)="updateTotal()" step="any" min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
        </ion-row>
        <ion-row class="item-md">
            <ion-col width-20>
                <ion-label color="primary" >25 lb blocks</ion-label>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="block25.qty" (ngModelChange)="updateTotal()" step="1"  min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="block25.price" (ngModelChange)="updateTotal()" step="any" min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
        </ion-row>
        <ion-row class="item-md">
            <ion-col width-20>
                <ion-label color="primary" >Vendor rent</ion-label>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="vendor.qty" (ngModelChange)="updateTotal()" step="1"  min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="vendor.price" (ngModelChange)="updateTotal()" step="any" min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
        </ion-row>
        <ion-row class="item-md">
            <ion-col width-20>
                <ion-label color="primary" >Storage</ion-label>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="storage.qty" (ngModelChange)="updateTotal()" step="1"  min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="storage.price" (ngModelChange)="updateTotal()" step="any" min="0" value="0"  [ngModelOptions]="{standalone: true}"></ion-input>
            </ion-col>
        </ion-row>
        <ion-row class="item-md">
            <ion-col width-20>
                <ion-label color="primary" >Freight</ion-label>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="freight.qty" (ngModelChange)="updateTotal()" step="1"  min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="freight.price" (ngModelChange)="updateTotal()" step="any" min="0" value="0"  [ngModelOptions]="{standalone: true}"></ion-input>
            </ion-col>
        </ion-row>
        <ion-row class="item-md">
            <ion-col width-20>
                <ion-label color="primary" >Other</ion-label>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="other.qty" (ngModelChange)="updateTotal()" step="1"  min="0" value="0" [ngModelOptions]="{standalone: true}" ></ion-input>
            </ion-col>
            <ion-col width-40>
                <ion-input type="number" [(ngModel)]="other.price" (ngModelChange)="updateTotal()" step="any" min="0" value="0"  [ngModelOptions]="{standalone: true}"></ion-input>
            </ion-col>
        </ion-row>
        <ion-item>
            <ion-label>Comments</ion-label>
            <ion-textarea formControlName="comment" ></ion-textarea>
        </ion-item>
        <ion-item>
            <ion-label color="primary">Total</ion-label>
            <ion-input [(ngModel)]="total" type="number" value="0.0"   [ngModelOptions]="{standalone: true}" disabled></ion-input>
        </ion-item>
        </form>
        <ion-item>
            <button ion-button (click)="submit($event)" [disabled]="!ticketForm.valid">Submit</button>
            <button ion-button (click)="clear($event)">Clear</button>
        </ion-item>
    </ion-content>

  `
})
export class NewTicket {
    
    private ticketForm : FormGroup;
    private customers: any[] = CUSTOMERS;

    private bag7: any = {'price': 0, 'qty': 0};
    private bag22: any = {'price': 0, 'qty': 0};
    private block10: any = {'price': 0, 'qty': 0};
    private block25: any = {'price': 0, 'qty': 0};
    private vendor: any = {'price': 0, 'qty': 0};
    private storage: any = {'price': 0, 'qty': 0};
    private freight: any = {'price': 0, 'qty': 0};
    private other: any = {'price': 0, 'qty': 0};

    private total: number = 0;
    private items: any[] = [this.bag7,this.bag22,this.block10,this.block25,this.vendor,this.storage,this.freight,this.other];


    constructor(public navCtrl: NavController, private formBuilder: FormBuilder){
        this.ticketForm = this.formBuilder.group({
            customer: [null, Validators.required],
            ticketDate: [new Date().toISOString(), Validators.required],
            paymentType: [null, Validators.required],
            checkNumber: [''],
            newCustomer: [''],
            comment: ['']
        });
    
    }

    updateTotal(){
        this.total = this.items.reduce( (total, item) => parseFloat(item.price)*parseInt(item.qty) + total, 0);
    }

    submit(event){
        let vals: any = this.ticketForm.value;
        console.log(this.ticketForm);
        if (vals.customer === 'new' && vals.customerName === ''){
            alert("Please enter a name for the new customer or select a customer.");
            return;
        }
        if (vals.paymentType === 'check' && vals.checkNumber === ''){
            alert("Please enter a check number for the check.");
            return;
        }

        let customerName: string = (vals.customer === 'new') ? vals.customerName : vals.customer;

        let ticket: Ticket = new Ticket( customerName, 
                                         vals.ticketDate, vals.paymentType, vals.checkNumber,
                                         'foo', 
                                         vals.comment, 
                                         {price:this.bag7.price, qty: this.bag7.qty},
                                         {price:this.bag22.price, qty: this.bag22.qty},
                                         {price:this.block10.price, qty: this.block25.qty},
                                         {price:this.block25.price, qty: this.block25.qty},
                                         {price:this.vendor.price, qty: this.vendor.qty},
                                         {price:this.storage.price, qty: this.storage.qty},
                                         {price:this.freight.price, qty: this.freight.qty},
                                         {price:this.other.price, qty: this.other.qty},
                                         this.total);
                                         
        this.navCtrl.push(TicketDetails, {ticket: ticket});

    }

    clear(event){
        this.items.forEach(item => {item.price = 0; item.qty = 0});
        this.total = 0;
        this.ticketForm.reset();
    }



}
