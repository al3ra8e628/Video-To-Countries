import {Component, OnInit} from '@angular/core';
import {BasicHttpService} from './services/basic-http.service';
import {NgxUiLoaderService} from 'ngx-ui-loader';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  videoUrl = null;

  processResponse = null;
  spinnerType: any;

  constructor(private httpService: BasicHttpService<any>,
              private ngxService: NgxUiLoaderService) {
  }

  canUpload() {
    return !this.processResponse;
  }

  submitVideo() {
    this.httpService.post(serviceUrl + '/api/v1/processes', {url: this.videoUrl})
      .subscribe(res => {
          this.processResponse = res;
          this.ngxService.start();
          this.loadResponse();
        },
        error => {
          console.error(error);
        });
  }

  changeValue($event) {
    this.videoUrl = $event;
  }

  private loadResponse() {
    const process_id = this.processResponse.process_id;
    this.httpService.get(`${serviceUrl}/api/v1/processes/${process_id}`)
      .subscribe(response => {
        this.processResponse = response;
        if (this.processResponse.status === 'PROCESSING') {
          setTimeout(() => {
            this.loadResponse();
          }, 5000);
        } else {
          this.ngxService.stop();
          this.handleCompletedVideo();
        }
      });
  }

  ngOnInit(): void {
    this.spinnerType = 'rectangle-bounce-pulse-out-rapid';
    // this.spinnerType = 'rectangle-bounce';
    // this.spinnerType = 'rectangle-bounce-party';
    // this.spinnerType = 'rectangle-bounce-pulse-out';
    // this.spinnerType = 'rotating-plane';
  }

  private handleCompletedVideo() {
    const dataStr = 'data:text/json;charset=utf-8,' +
      JSON.stringify(this.processResponse, null, 2);
    const downloadAnchorNode = document.createElement('a');

    downloadAnchorNode.setAttribute('href', dataStr);
    downloadAnchorNode.setAttribute('download', this.processResponse.process_id + '.json');

    document.body.appendChild(downloadAnchorNode);
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
  }

}

export const serviceUrl = 'http://localhost:5000';
