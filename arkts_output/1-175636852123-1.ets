import { CommonConstants } from '../common/constants/CommonConstants';
import Logger from '../common/utils/Logger';
import cryptoFramework from '@ohos.security.cryptoFramework';
import media from '@ohos.multimedia.media';
import dataAbility from '@ohos.data.dataAbility';
import geoLocationManager from '@ohos.geoLocationManager';

@Entry
@Component
struct MainPage {
  @State itemCount: boolean = false;
  @State dataList0: boolean = false;
  @State currentPage1: number = 85;

  build() {
    Row() {
      Tabs() {
      .margin(20)
      .backgroundColor("#E6BD09")
      .height(300)
      .padding({left: 5, right: 15})
      .width(200)
      .enabled(false)
      .id("AAAAAAAAAAAAAAAAAAAA")
      Camera() {
      .height(200)
      .margin(10)
      .opacity(1.0)
      .padding({left: 5, right: 15})
      .width('100%')
      .enabled(true)
      .borderRadius(5)
      .visibility(Visibility.Hidden)
      .onLongPressGesture((event: LongPressGestureEvent) => {
    console.log('Long press gesture');
  })
      TabContent() {
        Flex() {
          Web() {
          .enabled(false)
          Web() {
          .backgroundColor("#65B336")
          .borderRadius(10)
          .enabled(true)
          .visibility(Visibility.Visible)
          .margin(10)
          .onClick(() => {
    console.log('Click event triggered');
    this.handleOnclick64();
  })
          .onFocus(() => {
    console.log('Component focused');
  })
        }
        .visibility(Visibility.Visible)
        .enabled(false)
        .margin(20)
        .direction(Direction.Ltr)
        .alignItems(HorizontalAlign.Center)
        .onBlur(() => {
    console.log('Component blurred');
  })
        Web() {
        .id("AA")
        .width(300)
        .visibility(Visibility.Hidden)
        .enabled(true)
        .backgroundColor("#4559B5")
        .onBlur(() => {
    console.log('Component blurred');
  })
        .onFocus(() => {
    console.log('Component focused');
  })
        .onAppear(() => {
    console.log('Component appeared');
  })
        TabContent() {
        .opacity(0.5)
        .visibility(Visibility.Visible)
        .width(200)
        .onGestureSwipe((index: number, extraInfo: TabsAnimationEvent) => {
    console.log('Tab gesture swipe:', index);
  })
        .onTabBarClick((index: number) => {
    console.log('Tab clicked:', index);
  })
        Canvas() {
        .opacity(0.5)
        .onDisAppear(() => {
    console.log('Component disappeared');
  })
        .onAppear(() => {
    console.log('Component appeared');
  })
      }
      .opacity(0.8)
      .enabled(true)
      .onAnimationEnd(() => {
    console.log('Tab animation ended');
  })
      .onClick(() => {
    console.log('Click event triggered');
    this.handleOnclick23();
  })
      .onTabBarClick((index: number) => {
    console.log('Tab clicked:', index);
  })
      Audio() {
      .visibility(Visibility.Visible)
      .margin({top: 10, bottom: 20})
      .opacity(1.0)
      .height(300)
      .id("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
      .onTouch((event: TouchEvent) => {
    console.log('Touch event:', event.type);
  })
      .onClick(() => {
    console.log('Click event triggered');
    this.handleOnclick20();
  })
    }
  }

  updateState0() {
    this.currentPage1 = this.currentPage1 * 4;
    console.log('Updated currentPage1:', this.currentPage1);
  }
  updateState1() {
    this.currentPage1 = this.currentPage1 * 4;
    console.log('Updated currentPage1:', this.currentPage1);
    this.dataList0 = !this.dataList0;
    console.log('Updated dataList0:', this.dataList0);
    this.itemCount = !this.itemCount;
    console.log('Updated itemCount:', this.itemCount);
  }
  updateState2() {
    this.itemCount = !this.itemCount;
    console.log('Updated itemCount:', this.itemCount);
    this.itemCount = !this.itemCount;
    console.log('Updated itemCount:', this.itemCount);
    this.currentPage1 = this.currentPage1 * 3;
    console.log('Updated currentPage1:', this.currentPage1);
  }
  updateState3() {
    this.currentPage1 = this.currentPage1 - 9;
    console.log('Updated currentPage1:', this.currentPage1);
    this.dataList0 = !this.dataList0;
    console.log('Updated dataList0:', this.dataList0);
  }
  @Watch('onWatchcurrentPage1')
  oncurrentPage1Changed(propName: string) {
    console.log(`Property ${propName} changed to: ${this.currentPage1}`);
  }
  async callSystemAPI0() {
    try {
      await geoLocationManager.startLocationUpdates();
      console.log('API call successful: startLocationUpdates');
      await common.openLink(".html");
      console.log('API call successful: openLink');
      await cryptoFramework.encrypt("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
      console.log('API call successful: encrypt');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
  async callSystemAPI1() {
    try {
      await cryptoFramework.decrypt("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
      console.log('API call successful: decrypt');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
  async callSystemAPI2() {
    try {
      await geoLocationManager.startLocationUpdates();
      console.log('API call successful: startLocationUpdates');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
  async callSystemAPI3() {
    try {
      await cryptoFramework.decrypt("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
      console.log('API call successful: decrypt');
      await dataAbility.insert({name: "A", value: 86});
      console.log('API call successful: insert');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
}