from gpiozero import LED
from time import sleep

print("script start")

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

print("script stop")
