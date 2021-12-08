//api service that intergrates angular with flask

import { Injectable } from '@angular/core';
import {throwError as observableThrowError, Observable} from 'rxjs'
import {catchError} from 'rxjs/operators'
import {HttpClient,HttpErrorResponse,HttpHeaders} from '@angular/common/http'
import {Products} from './interfaces'

@Injectable({
  providedIn: 'root'
})
export class ApiService {
    products:string ="http://127.0.0.1:5000/getProducts"

  constructor(private http:HttpClient) { }

  getProducts():Observable<Products[]>{
    return this.http.get<Products[]>(this.products).pipe(
      catchError(this.errorHandler))
  }

   errorHandler(error:HttpErrorResponse){

    return observableThrowError(error.message ||"Server Down")

  }
}
