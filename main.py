# By Jeremy823 on Mon 8 Apr 2024
# https://github.com/Jeremy-JYL/ESP32-Micropython-NTP-Clock

import network
import time
import ntptime
from display import LCD
from machine import SoftI2C, Pin

ssid = "SSID" # Wifi SSID
password = "PASSWORD" # Wifi Password
UTC_OFFSET = 0 # UTC Offset
scl_pin = 22 # SCL Pin
sda_pin = 21 # SDA Pin

# Init GPIO and I2C 1602 Display
p0 = Pin(0, Pin.IN, Pin.PULL_DOWN) # Sync Pin
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000)) # Display

# Connecting to Wifi
lcd.clear()
lcd.puts("Connecting ...")

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

# Waiting the Wifi
while not wifi.isconnected():
    pass

lcd.clear()
lcd.puts("Syncing Time ...")
ntptime.settime()
lcd.clear()

# Functions
def convert_day(year, month, day):
    # Zeller's Congruence algorithm
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    h = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

    days = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]
    return days[h]

def am_pm(hours, minutes, seconds):
    period = 'AM' if hours < 12 else 'PM'
    
    # Convert hours to 12-hour format
    if hours == 0:
        hours = 12
    elif hours > 12:
        hours -= 12
    
    # Return the time in 12-hour format
    return '{:02d}:{:02d}:{:02d} {}'.format(hours, minutes, seconds, period)

# Main loop
while True:
    if p0.value() == 1: # Checking the Sync Pin
        lcd.clear()
        lcd.puts("Syncing Time ...")
        ntptime.settime()
        lcd.clear()
    year, month, days, hours, minutes, seconds, _, _ = time.localtime(time.time() + (UTC_OFFSET * 60 * 60))
    md = convert_day(year, month, days)
    lcd.puts("{}".format(am_pm(hours, minutes, seconds)))
    lcd.puts("{} {} {} {}".format(year, md, days, month), 1)
