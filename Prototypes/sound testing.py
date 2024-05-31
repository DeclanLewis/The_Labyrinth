# The author of this file is Declan Lewis. Made 5th of March 2024.

from pygame import mixer
import time

mixer.init()

mixer.music.load("../Sounds/StartRoom_sound.mp3")

mixer.music.play()
while mixer.music.get_busy():
    time.sleep(0.1)