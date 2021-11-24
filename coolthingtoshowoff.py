import time

print("Watch this")

time.sleep(2)

print("I am a cool kid")

time.sleep(2)

print("I can count to 100")

for i in range(1, 100):
    print(i)
    time.sleep(1)

#pip install pygame
import mixers
import time
mixer.init() #Initialzing pyamge mixer

mixer.music.load('lovingly-618.mp3') #Loading Music File

mixer.music.play() #Playing Music with Pygame

time.sleep(5)


mixer.music.stop()
