import {Component, OnInit} from '@angular/core';
import {BasicHttpService} from './services/basic-http.service';
import {NgxUiLoaderService} from 'ngx-ui-loader';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  languages = ["English", "Arabic"];

  videoUrl = null;
  videoLanguage = 'English';
  processResponse = null;
  spinnerType: any;
  serviceUrl = 'http://localhost:5000';

  constructor(private httpService: BasicHttpService<any>,
              private ngxService: NgxUiLoaderService) {
  }

  canUpload() {
    return !this.processResponse;
  }

  submitVideo() {
    this.httpService.post(this.serviceUrl + '/api/v1/processes', {
      url: this.videoUrl,
      lang: this.videoLanguage
    })
      .subscribe(res => {
          this.processResponse = res;
          this.ngxService.start();
          this.loadResponse();
        },
        error => {
          console.error(error);
        });
  }

  changeUrl($event) {
    this.videoUrl = $event;
  }

  private loadResponse() {
    const process_id = this.processResponse.process_id;
    this.httpService.get(`${this.serviceUrl}/api/v1/processes/${process_id}`)
      .subscribe(response => {
        this.processResponse = response;
        if (this.processResponse.status === 'PROCESSING'
          || this.processResponse.status === 'DOWNLOADING') {
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
    this.clearLastProcessedVideo();
  }

  changeLanguage(value: any) {
    this.videoLanguage = value;
  }

  private clearLastProcessedVideo() {
    this.videoLanguage = 'English';
    this.videoUrl = null;
    this.processResponse = null;
  }

  getVideoLanguageValue(): string {
    return this.videoLanguage;
  }

  getProcessingMessage(): string {
    if (!this.processResponse)
      return "PROCESSING"
    if (this.processResponse.progress)
      return `${this.processResponse.status} ${this.processResponse.progress}`
    return this.processResponse.status
  }
}
