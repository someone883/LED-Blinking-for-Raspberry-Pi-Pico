#importing libraries
from machine import Pin
import utime
#defining LED
LED=Pin(15,Pin.OUT)
while True:
    #1 = ON 0 = OFF
    LED.value(1)
    """
    utime.sleep_ms(500)
    LED.value(0)
    utime.sleep(1)
    """
    #Uncomment last 3 lines for LED blinking