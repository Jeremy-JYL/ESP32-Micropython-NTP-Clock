# ESP32-Micropython-NTP-Clock
![Capture-2024-04-08-74818 PM](https://github.com/Jeremy-JYL/ESP32-Micropython-NTP-Clock/assets/108569568/08cc4b4b-7f65-4b24-9c51-36ffccda457f)

# How to use?
Clone / Download the files and change the Wifi SSID, Password and UTC Offset, and wired like the image above

| Pin | Button | 1602 I2C Diplay |
|-----|--------|-----------------|
| 0   | √      | X               |
| 21  | X      | √ ( SDA )       |
| 22  | X      | √ ( SCL )       |

| Time Zone                               | UTC Offset |
|-----------------------------------------|------------|
| UTC (Coordinated Universal Time)        | +00:00     |
| GMT (Greenwich Mean Time)               | +00:00     |
| EST (Eastern Standard Time)             | -05:00     |
| EDT (Eastern Daylight Time)             | -04:00     |
| CST (Central Standard Time)             | -06:00     |
| CDT (Central Daylight Time)             | -05:00     |
| MST (Mountain Standard Time)            | -07:00     |
| MDT (Mountain Daylight Time)            | -06:00     |
| PST (Pacific Standard Time)             | -08:00     |
| PDT (Pacific Daylight Time)             | -07:00     |
| BST (British Summer Time)               | +01:00     |
| IST (Irish Standard Time)               | +01:00     |
| CET (Central European Time)             | +01:00     |
| CEST (Central European Summer Time)     | +02:00     |
| AEST (Australian Eastern Standard Time) | +10:00     |
| AEDT (Australian Eastern Daylight Time) | +11:00     |
| ACST (Australian Central Standard Time) | +09:30     |
| ACDT (Australian Central Daylight Time) | +10:30     |
| AWST (Australian Western Standard Time) | +08:00     |

Note: The button is for syncing the time.

Try it on Wokwi [Link](https://wokwi.com/projects/394601619168114689)
