import { CommonConstants } from '../common/constants/CommonConstants';
import Logger from '../common/utils/Logger';
import cryptoFramework from '@ohos.security.cryptoFramework';
import deviceInfo from '@ohos.deviceInfo';
import vibrator from '@ohos.vibrator';
import window from '@ohos.window';
import geoLocationManager from '@ohos.geoLocationManager';
import request from '@ohos.request';

@Entry
@Component
struct MainPage {
  @State dataList1: string = "Hello World";
  @State errorMessage2: number = 79;
  @State selectedIndex0: number = 36;
  @State itemCount2: number = 39;
  @State itemCount0: string = "Sample Text";
  @State userName: string = "Item";

  build() {
    Column() {
      ScrollArea() {
      .visibility(Visibility.Hidden)
      Radio() {
      .backgroundColor("#CA4A9C")
      .opacity(1.0)
      .width(200)
      .id("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
      .visibility(Visibility.Hidden)
      .height(200)
    }
  }

  updateState0() {
    this.itemCount2 = this.itemCount2 + 3;
    console.log('Updated itemCount2:', this.itemCount2);
    this.itemCount0 = "Updated";
    console.log('Updated itemCount0:', this.itemCount0);
  }
  updateState1() {
    this.userName = "Modified";
    console.log('Updated userName:', this.userName);
    this.itemCount2 = this.itemCount2 * 1;
    console.log('Updated itemCount2:', this.itemCount2);
  }
  updateState2() {
    this.itemCount0 = "New Value";
    console.log('Updated itemCount0:', this.itemCount0);
    this.errorMessage2 = this.errorMessage2 - 6;
    console.log('Updated errorMessage2:', this.errorMessage2);
  }
  updateState3() {
    this.itemCount2 = this.itemCount2 - 7;
    console.log('Updated itemCount2:', this.itemCount2);
    this.errorMessage2 = this.errorMessage2 - 6;
    console.log('Updated errorMessage2:', this.errorMessage2);
  }
  @Watch('onWatchitemCount0')
  onitemCount0Changed(propName: string) {
    console.log(`Property ${propName} changed to: ${this.itemCount0}`);
  }
  async callSystemAPI0() {
    try {
      await window.setStatusBarColor("#2EF200");
      console.log('API call successful: setStatusBarColor');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
  async callSystemAPI1() {
    try {
      await vibrator.vibrate(343);
      console.log('API call successful: vibrate');
      await window.setStatusBarColor("#2EF200");
      console.log('API call successful: setStatusBarColor');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
  async callSystemAPI2() {
    try {
      await window.setStatusBarColor("#2EF200");
      console.log('API call successful: setStatusBarColor');
      await request.download({url: "https://example.com/file.png""});
      console.log('API call successful: download');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
}