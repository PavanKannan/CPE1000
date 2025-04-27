from sense_hat import SenseHat
import time

s=SenseHat()

red = (255,0,0)
blue = (0,0,255)

usr_input = input("Enter your message: ")

usr_color = int(input("Enter 1 for Red or 2 for Blue: "))

if usr_color == 1:
	s.show_message(usr_input, text_colour=red)
elif usr_color == 2:
	s.show_message(usr_input, text_colour=blue)
else:
	print("Invaild Input! Choose Red or Blue.")
