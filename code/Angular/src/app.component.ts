import { Component,Input } from '@angular/core';
import {faHome,faBookmark,faToggleOn,faNewspaper} from '@fortawesome/free-solid-svg-icons'
import {ApiService} from './api.service'
import {Name} from './interfaces'
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
 @Input() data:any;
 public productDetails:any

 public currentView ="home"
 public model = new Name("")


constructor(private api:ApiService) { }

  ngOnInit(): void {
    this.getProducts()
  }

getProducts(){
  this.api.getProducts().subscribe(data=>this.productDetails=data,
    error=>this.currentView="serverDown")
}

purchaseProduct(product:any){
 this.api.postProduct(product.Name).subscribe(error=>this.currentView="serverDown")
}
}
