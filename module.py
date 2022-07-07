import random

feet_in_mile = 5800
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ext(filemane):
    return filemane[filemane.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)