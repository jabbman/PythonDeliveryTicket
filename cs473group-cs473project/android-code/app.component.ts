import { Component } from '@angular/core';
import { Platform } from 'ionic-angular';
import { StatusBar, Splashscreen } from 'ionic-native';
import { Menu } from './menu/menu';


@Component({
  template: '<ion-nav [root]="rootPage"></ion-nav>'
})

export class App {
  rootPage = Menu;

  constructor(platform: Platform) {
    platform.ready().then(() => {
      StatusBar.styleDefault();
      Splashscreen.hide();
    });
  }
}
