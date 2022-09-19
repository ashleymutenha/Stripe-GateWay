import { Injectable } from '@angular/core';
import {throwError as observableThrowError, Observable} from 'rxjs'
import {catchError} from 'rxjs/operators'
import {HttpClient,HttpErrorResponse,HttpHeaders} from '@angular/common/http'
import {Products} from './interfaces'

const headers= new HttpHeaders({'Content-Type':'application/json'})
@Injectable({
  providedIn: 'root'
})


export class ApiService {
    _getProducts:string ="http://127.0.0.1:5000/getProducts"
    _postProducts:string ="http://127.0.0.1:5000/orderProduct"

  constructor(private http:HttpClient) { }

  getProducts():Observable<Products[]>{
    return this.http.get<Products[]>(this._getProducts,).pipe(
      catchError(this.errorHandler))
  }

  postProduct(product:any):Observable<any>{
    return this.http.post<any>(this._postProducts,JSON.stringify(product),{'headers':headers}).pipe(
      catchError(this.errorHandler))
  }

   errorHandler(error:HttpErrorResponse){

    return observableThrowError(error.message ||"Server Down")

  }
}
