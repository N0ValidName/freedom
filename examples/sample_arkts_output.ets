import { CommonConstants } from '../common/constants/CommonConstants';
import Logger from '../common/utils/Logger';

@Entry
@Component  
struct MainPage {
  @State stateValue0: string = "A";
  @State stateFlag1: boolean = true;
  @State stateCount2: number = 42;

  build() {
    Column() {
      Row() {
        Text("AAAAAAAAAA")
          .fontSize(16)
          .fontColor("#FF5733")
          .textAlign(TextAlign.Center)
          .maxLines(2)
        
        Button("Click")
          .type(ButtonType.Normal)
          .backgroundColor("#00FF00") 
          .width(100)
          .height(50)
          .onClick(() => {
            console.log('Click event triggered');
            this.handleClick1();
          })
      }
      .justifyContent(FlexAlign.SpaceBetween)
      .alignItems(HorizontalAlign.Center)
      .width('100%')
      .padding(20)
      
      Image($r("app.media.sample"))
        .width(200)
        .height(150)
        .objectFit(ImageFit.Cover)
        .borderRadius(10)
        .margin({top: 20, bottom: 10})
        .onTouch((event: TouchEvent) => {
          console.log('Touch event:', event.type);
        })
      
      List() {
        ForEach([1, 2, 3], (item) => {
          ListItem() {
            Text(`Item ${item}`)
              .fontSize(14)
              .padding(10)
          }
        })
      }
      .space(10)
      .listDirection(Axis.Vertical)
      .height(200)
      .onScrollIndex((start: number, end: number) => {
        console.log('Scroll index changed:', start, end);
      })
    }
    .justifyContent(FlexAlign.Start)
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%')
    .backgroundColor('#F5F5F5')
  }

  handleClick1() {
    this.stateFlag1 = !this.stateFlag1;
  }
  
  updateState0() {
    console.log('Updated stateValue0:', this.stateValue0);
  }
}