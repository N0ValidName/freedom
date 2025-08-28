import { CommonConstants } from '../common/constants/CommonConstants';
import Logger from '../common/utils/Logger';
import dataPreferences from '@ohos.data.preferences';
import vibrator from '@ohos.vibrator';

@Entry
@Component
struct MainPage {
  @State errorMessage2: string = "Hello World";
  @State selectedIndex2: string = "Sample Text";
  @State dataList2: number = 13;
  @State userAge2: number = 22;
  @State selectedIndex0: string = "";

  build() {
    Column() {
  }

  updateState0() {
    this.selectedIndex0 = "Updated";
    console.log('Updated selectedIndex0:', this.selectedIndex0);
    this.selectedIndex2 = "Modified";
    console.log('Updated selectedIndex2:', this.selectedIndex2);
  }
  @Watch('onWatchselectedIndex2')
  onselectedIndex2Changed(propName: string) {
    console.log(`Property ${propName} changed to: ${this.selectedIndex2}`);
  }
  async callSystemAPI0() {
    try {
      await vibrator.vibrate(276);
      console.log('API call successful: vibrate');
      await preferences.removeItem("AAAA");
      console.log('API call successful: removeItem');
      await preferences.setItem("AAAAAAAAAA", "AAAAAAAAAAAAAAAA");
      console.log('API call successful: setItem');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
  async callSystemAPI1() {
    try {
      await preferences.removeItem("AAAA");
      console.log('API call successful: removeItem');
      await vibrator.vibrate(276);
      console.log('API call successful: vibrate');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
}