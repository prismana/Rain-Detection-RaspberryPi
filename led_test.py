# install gpiozero

from gpiozero imoprt LED
from time import sleep

# define led
red = LED(16) # pin 17
green = LED(20) #pin 20

while True:
    red.on()
    green.on()
    sleep(1) # sleep 1 second
    red.off()
    green.off()
    sleep(1)
