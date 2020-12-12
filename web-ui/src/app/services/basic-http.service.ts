import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BasicHttpService<T> {

  constructor(private httpClient: HttpClient) {
  }

  get(url: string): Observable<T> {
    return this.httpClient.get<T>(url);
  }

  post(url: string, body: any): Observable<T> {
    return this.httpClient.post<T>(url, body);
  }
}
