from sense_hat import SenseHat
import time

s = SenseHat()
s.clear()
time.sleep(1)
x=0
y=0

for i in range (0,8):
  x = i
  s.set_pixel(x,y, 255,255,255)
  time.sleep(.25)
  if (i == 7):
    for j in range (0,8):
        y = j
        s.set_pixel(x,y, 255,255,255)
        time.sleep(.25)
        if (j == 7):
          for i in range (7,-1,-1):
            x = i
            s.set_pixel(x,y, 255,255,255)
            time.sleep(.25)
            if (i == 0):
              for j in range (7,-1,-1):
                y = j
                s.set_pixel(x,y, 255,255,255)
                time.sleep(.25)