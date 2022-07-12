from random import randint
from sense_hat import SenseHat
sense = SenseHat()


sense.show_message("Hello to you", text_colour = [randint(0,255), randint(0,255), randint(0,255)])
