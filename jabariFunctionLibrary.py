import playsound
import termcolor
import time
from pygame import mixer

def introduction_exposition_dump()
    print ("Welcome to Jabari Jumps: The video game")
    time.sleep(2)
    print ("once upon a time there was a boy named Jabari")
    time.sleep(2)
    print ("one day Jabari and his family decided to go to the pool together")
    time.sleep(2)
    print ("at this pool there was a very very tall diving board")
    time.sleep(2)
    print ("For as long as Jabari could remember he wanted to dive off the tall board, but he could never gather the courage")
    time.sleep(2)
    print ("today was the day he would jump off of it jabari thought")
    time.sleep(5)
    print ("on his way towards the diving boards")
    time.sleep(2)
    print ("He bumped into a bully who scared jabari into not being able to jump of the diving board and then called him a coward.")
    time.sleep(2)
    print("Jabari had to know defeat his fear and prove the bully wrong.")
    time.sleep(2)
    print ("You are faced with a descision: do you want to turn back or do you want to continue (type continue or give up)")

def victory_screen():

    text = "victoriouse"
    printString = termcolor.colored(text,'red','on_blue', attrs=['bold'])
    playsound.playsound('Plants Vs Zombies Victory Jingle.mp3')
    print (printString) 
    answer = input()

def Loserxd():
    gameOverText = "Loser xd"
    printString2 = termcolor.colored(gameOverText,'white', attrs=['bold','blink'])
    playsound.playsound('Regular Show Intro sound effect.mp3')
    print (printString2)
    answer = input()