import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

def blink_led(rate, tduration):
    end_time = time.time() + tduration
    while time.time() < end_time:
        GPIO.output(21, GPIO.HIGH)
        time.sleep(rate)
        GPIO.output(21, GPIO.LOW)
        time.sleep(rate)

while True:
    rate = input("Enter blink rate (L/M/H): ").upper()
    if rate in ['L', 'M', 'H']:
        break
    print("Invalid input! Please enter L, M, or H.")

if rate == 'L':
    b_rate = 0.5
elif rate == 'M':
    b_rate = 0.3
else: 
    b_rate = 0.1

print("LED blinking at", b_rate," second intervals for 5 seconds...")
blink_led(b_rate, 5)
print("Program completed!")