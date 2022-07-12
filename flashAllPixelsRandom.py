from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

while True:

    O= [255, 255, 0]

    display_array = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]
    
    newlist = []

    for f in range(64):
        listy = [0, 0, 0]
        for i in range(1):
            listy[0] = random.randint(0, 255)
            listy[1]= random.randint(0, 255)
            listy[2]= random.randint(0, 255)
            newlist.append(listy)

    display_array = newlist
    sense.set_pixels(display_array)
    sleep(.001)
    sense.clear()
