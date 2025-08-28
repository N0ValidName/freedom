import { CommonConstants } from '../common/constants/CommonConstants';
import Logger from '../common/utils/Logger';
import cryptoFramework from '@ohos.security.cryptoFramework';
import dataPreferences from '@ohos.data.preferences';
import window from '@ohos.window';
import abilityAccessCtrl from '@ohos.abilityAccessCtrl';
import dataAbility from '@ohos.data.dataAbility';

@Entry
@Component
struct MainPage {
  @State errorMessage0: boolean = false;
  @State currentPage0: string = "Item";
  @State dataList2: number = 46;
  @State currentPage2: boolean = false;

  build() {
    Stack() {
  }

  updateState0() {
    this.dataList2 = this.dataList2 * 1;
    console.log('Updated dataList2:', this.dataList2);
    this.currentPage2 = !this.currentPage2;
    console.log('Updated currentPage2:', this.currentPage2);
    this.errorMessage0 = !this.errorMessage0;
    console.log('Updated errorMessage0:', this.errorMessage0);
  }
  updateState1() {
    this.errorMessage0 = !this.errorMessage0;
    console.log('Updated errorMessage0:', this.errorMessage0);
  }
  updateState2() {
    this.errorMessage0 = !this.errorMessage0;
    console.log('Updated errorMessage0:', this.errorMessage0);
  }
  @Watch('onWatchdataList2')
  ondataList2Changed(propName: string) {
    console.log(`Property ${propName} changed to: ${this.dataList2}`);
  }
  @Watch('onWatchdataList2')
  ondataList2Changed(propName: string) {
    console.log(`Property ${propName} changed to: ${this.dataList2}`);
  }
  async callSystemAPI0() {
    try {
      await window.setStatusBarColor("#8927BE");
      console.log('API call successful: setStatusBarColor');
      await preferences.removeItem("AAAAAAAAAAAAAAAA");
      console.log('API call successful: removeItem');
      await abilityAccessCtrl.requestPermissions(["ohos.permission.READ_MEDIA"]);
      console.log('API call successful: requestPermissions');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
  async callSystemAPI1() {
    try {
      await abilityAccessCtrl.requestPermissions(["ohos.permission.READ_MEDIA"]);
      console.log('API call successful: requestPermissions');
      await dataAbility.query("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
      console.log('API call successful: query');
      await window.setStatusBarColor("#8927BE");
      console.log('API call successful: setStatusBarColor');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
  async callSystemAPI2() {
    try {
      await cryptoFramework.encrypt("AA");
      console.log('API call successful: encrypt');
      await window.setStatusBarColor("#8927BE");
      console.log('API call successful: setStatusBarColor');
      await common.openLink("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.html");
      console.log('API call successful: openLink');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
}