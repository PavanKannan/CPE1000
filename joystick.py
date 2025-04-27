# Initialize SenseHat instance
# This tutorial code shows you how to move an LED dot to the right when a right joystick action is made

from sense_hat import SenseHat
sense = SenseHat()

# Intialization
sense.clear()
x = 4
y = 4
sense.set_pixel(x, y, 250, 250, 250)
Done = False


while (Done == False):
  event = sense.stick.wait_for_event()
  if event.action == "pressed":
    print("Joystick was moved:", event.direction)
    if event.direction == "middle":
      Done = True
      
    if event.direction == "right":
      sense.clear()
      x = x + 1
      if x>7:
        x = 0
      sense.set_pixel(x, y, 250, 250, 250)
      
    if event.direction == "left":
      sense.clear()
      x = x - 1
      if x<0:
        x = 7
      sense.set_pixel(x, y, 250, 250, 250)
      
    if event.direction == "up":
        sense.clear()
        y = y - 1
        if y<0:
          y = 7
        sense.set_pixel(x, y, 250, 250, 250)
        
    if event.direction == "down":
        sense.clear()
        y = y + 1
        if y>7:
          y = 0
        sense.set_pixel(x, y, 250, 250, 250)

print('Done')