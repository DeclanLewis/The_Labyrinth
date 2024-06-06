# The author of this file is Declan Lewis. Made 5th of March 2024.
# This software will be distributed with a GNU lesser general public license
# Pygame also uses this GNU lesser general public license
# This as me figuring out the mixer function in pygame

from pygame import mixer
import time

mixer.init()

mixer.music.load("../Sounds/StartRoom_sound.mp3")

mixer.music.play()
while mixer.music.get_busy():
    time.sleep(0.1)