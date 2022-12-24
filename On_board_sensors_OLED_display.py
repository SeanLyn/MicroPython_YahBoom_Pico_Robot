import array, time
import machine,onewire
from machine import Pin, PWM, I2C
from onewire import OneWire
import rp2
import framebuf

from pico_car import pico_car, SSD1306_I2C, sensors, ultrasonic

###################################
# Setup OLED DISPLAY
# set IIC pin
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
# initialization oled
oled = SSD1306_I2C(128, 32, i2c)
line_size = 8
###################################

###################################
# initialization on-board Sensors and ultrasonic
sensors = sensors() # tempearture sensor and battery readings.
ultrasonic = ultrasonic() # distance sensor
###################################

###################################
# Code Starts Here
if __name__=="__main__":
    while True: 
        [temperature_celcius, temperature_fahrenheit] = sensors.read_temperature()
        distance = ultrasonic.Distance_accurate()  #get distance
        oled.fill(0)  # clear OLED display
        oled.text(str(temperature_celcius)[0:4]+" degree C", 0, 0)
        oled.text(str(temperature_fahrenheit)[0:4]+" degree F", 0, line_size)
        oled.text(sensors.check_battery_level(), 0, 2*line_size)
        oled.text('distance:'+str(distance)+'cm', 0, 3*line_size)
        oled.show()
        time.sleep(0.5)