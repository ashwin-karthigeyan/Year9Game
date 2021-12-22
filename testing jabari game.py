import playsound
import termcolor
import time
from pygame import mixer
def victory_screen():

    text = "victorious"
    printString = termcolor.colored(text,'red','on_blue', attrs=['bold'])
    playsound.playsound('Plants Vs Zombies Victory Jingle.mp3')
    print (printString) 
    answer = input()

print ("you go home happy, the bully leaves you alone, and learn to take calculated risks") 
victory_screen()