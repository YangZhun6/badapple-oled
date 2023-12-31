from machine import I2C,Pin
import time
import uos
import json
addr = 0x3c
i2c=I2C(sda=Pin(22), scl=Pin(21), freq=40000000)
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c,addr)



def image(img_list):   
    s=time.ticks_ms()  
    oled.fill(0)     
    for i in img_list:
        oled.hline(2*i[0],2*i[1],2*i[2],1)
    oled.show()
    e=time.ticks_ms()-s
    if e<100:
        time.sleep_ms(90-e)
    with open('badapple.data','r') as f:
        for i in f:
            z=json.loads(i)
        image(z)