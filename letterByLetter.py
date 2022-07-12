from random import randint
import time
from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

def pick_random_colour():
	random_red = randint(0,255)
	random_green  = randint(0, 255)
	random_blue= randint(0,255)
	return (random_red, random_green, random_blue)

abby = ["A", "B", "B", "Y"]


for i in abby:
	sense.show_letter(i, pick_random_colour())
	time.sleep(1)

sense.clear()

hey = ["S", "U", "P"]


for i in hey:
	sense.show_letter(i, pick_random_colour())
	time.sleep(1)
