import { CommonConstants } from '../common/constants/CommonConstants';
import Logger from '../common/utils/Logger';
import media from '@ohos.multimedia.media';
import webSocket from '@ohos.net.webSocket';
import window from '@ohos.window';

@Entry
@Component
struct MainPage {
  @State itemCount1: boolean = false;
  @State dataList1: boolean = true;
  @State userAge2: boolean = true;
  @State loadingState1: boolean = true;
  @State isLoggedIn2: string = "Hello World";
  @State dataList1: boolean = false;

  build() {
    Column() {
      Circle() {
      .borderRadius(15)
      .visibility(Visibility.Hidden)
      .height('50vp')
      .padding(10)
      .backgroundColor("#CCBA3B")
      .width(100)
      .id("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
      .onDisAppear(() => {
    console.log('Component disappeared');
  })
      Tabs() {
        Audio() {
        .id("AAAA")
        .opacity(0.8)
        .enabled(false)
        .width('100%')
        .height(200)
        .backgroundColor("#8A958B")
        .margin(20)
        .borderRadius(5)
        TabContent() {
        .id("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        .width('50vp')
        .enabled(true)
        .borderRadius(15)
        .backgroundColor("#9B5EEF")
        .opacity(0.8)
        .height('100%')
        .margin(10)
        .onAppear(() => {
    console.log('Component appeared');
  })
        Row() {
          Swiper() {
            Column() {
              Circle() {
              .height('100%')
              .visibility(Visibility.Visible)
              .borderRadius(10)
              .opacity(1.0)
              .padding(10)
              .width('50vp')
              .onClick(() => {
    console.log('Click event triggered');
    this.handleOnclick35();
  })
              Slider() {
              .borderRadius(10)
              .padding(10)
              .margin(20)
              .width(300)
              .opacity(1.0)
              .height(300)
              .onAppear(() => {
    console.log('Component appeared');
  })
              .onFocus(() => {
    console.log('Component focused');
  })
              .onPinchGesture((event: PinchGestureEvent) => {
    console.log('Pinch gesture:', event.scale);
  })
            }
            .borderRadius(15)
            .height(300)
            .wrap(FlexWrap.Wrap)
            .onClick(() => {
    console.log('Click event triggered');
    this.handleOnclick79();
  })
          }
          .height('100%')
          .onDisAppear(() => {
    console.log('Component disappeared');
  })
        }
        .margin(10)
        Text("AAAA")
        .enabled(true)
        .textAlign(TextAlign.End)
        .visibility(Visibility.Visible)
        .opacity(0.5)
        .maxLines(3)
        .textOverflow(TextOverflow.Ellipsis)
      }
      .backgroundColor("#3105B9")
      .visibility(Visibility.Visible)
      .id("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
      .height('50vp')
      .onDisAppear(() => {
    console.log('Component disappeared');
  })
      Shape() {
      .backgroundColor("#86800E")
      .width(300)
      .borderRadius(10)
      .height(100)
      Row() {
        Stack() {
        .backgroundColor("#6EC86A")
        .alignItems(HorizontalAlign.Center)
        .enabled(true)
        .opacity(1.0)
        .wrap(FlexWrap.Wrap)
        .visibility(Visibility.Visible)
        .direction(Direction.Ltr)
        .onDisAppear(() => {
    console.log('Component disappeared');
  })
        Checkbox() {
        .id("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        .padding(10)
        .enabled(false)
        .margin(20)
        .borderRadius(5)
        .backgroundColor("#9688F3")
        .opacity(0.8)
        .visibility(Visibility.Hidden)
        .onBlur(() => {
    console.log('Component blurred');
  })
        Audio() {
        .borderRadius(15)
        .id("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        .backgroundColor("#1EDA46")
        .height('100%')
        .onFocus(() => {
    console.log('Component focused');
  })
        .onPanGesture((event: PanGestureEvent) => {
    console.log('Pan gesture:', event.offsetX, event.offsetY);
  })
        .onLongPressGesture((event: LongPressGestureEvent) => {
    console.log('Long press gesture');
  })
        Row() {
        .id("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        .onTouch((event: TouchEvent) => {
    console.log('Touch event:', event.type);
  })
      }
      .visibility(Visibility.Visible)
      .opacity(1.0)
      .height(300)
      .width('50vp')
      .padding(10)
      .borderRadius(5)
      .onAppear(() => {
    console.log('Component appeared');
  })
    }
  }

  updateState0() {
    this.isLoggedIn2 = "Updated";
    console.log('Updated isLoggedIn2:', this.isLoggedIn2);
    this.userAge2 = !this.userAge2;
    console.log('Updated userAge2:', this.userAge2);
  }
  updateState1() {
    this.dataList1 = !this.dataList1;
    console.log('Updated dataList1:', this.dataList1);
    this.dataList1 = !this.dataList1;
    console.log('Updated dataList1:', this.dataList1);
    this.userAge2 = !this.userAge2;
    console.log('Updated userAge2:', this.userAge2);
  }
  updateState2() {
    this.dataList1 = !this.dataList1;
    console.log('Updated dataList1:', this.dataList1);
    this.itemCount1 = !this.itemCount1;
    console.log('Updated itemCount1:', this.itemCount1);
  }
  updateState3() {
    this.itemCount1 = !this.itemCount1;
    console.log('Updated itemCount1:', this.itemCount1);
  }
  async callSystemAPI0() {
    try {
      await window.getWindowProperties();
      console.log('API call successful: getWindowProperties');
      await media.createVideoPlayer();
      console.log('API call successful: createVideoPlayer');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
  async callSystemAPI1() {
    try {
      await window.getWindowProperties();
      console.log('API call successful: getWindowProperties');
      await webSocket.send("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
      console.log('API call successful: send');
      await media.createVideoPlayer();
      console.log('API call successful: createVideoPlayer');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
  async callSystemAPI2() {
    try {
      await audioPlayer.play();
      console.log('API call successful: play');
    } catch (error) {
      console.error('API call failed:', error);
    }
  }
}