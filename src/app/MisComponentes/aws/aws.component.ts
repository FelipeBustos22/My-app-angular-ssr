import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { OnInit } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-aws',
  standalone: true,
  imports: [HttpClientModule],
  templateUrl: './aws.component.html',
  styleUrl: './aws.component.css'
})
export class AWSComponent {
  constructor (private http: HttpClient) {

  }
  data: any = [];

  
  ngOnInit() { 
    this.http.get('https://felipebustos.hopto.org/hola').subscribe(data => { 
      console.log(data);
      this.data = data;
    });
  }
}
