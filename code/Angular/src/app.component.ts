import { Component } from '@angular/core';
import {faHome,faBookmark,faToggleOn,faNewspaper} from '@fortawesome/free-solid-svg-icons'
import {ApiService} from './api.service'
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
 faBookmark=faBookmark;
 faHome =faHome;
 faToggleOn =faToggleOn;
 faNewspaper =faNewspaper

 public productDetails:any

 public currentView ="home"


constructor(private api:ApiService) { }

  ngOnInit(): void {
    this.getProducts()
  }

getProducts(){
  this.api.getProducts().subscribe(data=>this.productDetails=data,
    error=>this.currentView="serverDown")
}
}