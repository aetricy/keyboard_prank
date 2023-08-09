from pygame import mixer
from pynput.keyboard import Key, Listener

import random
import os

file_path = os.getcwd()
soundsList = os.listdir(file_path+"/sounds")
soundsList.remove("diff") # Remove diff folder


print("\n\n Press ""END"" to STOP \n\n")
print(" Listener Started")
def on_press(key):
    print(key)      
    if key == Key.space:
        playSound("diff/yamete.mp3")
    elif key == Key.enter:
        x = random.randint(1, 3)
        if x == 1:
            playSound("diff/hoo1.mp3")
        elif x == 2:
            playSound("diff/hoo2.mp3")
        else:
            playSound("diff/hoo3.mp3")
    if (key != Key.enter and key != Key.space and key !=Key.esc and key != Key.end):
        playSound(random.choice(soundsList)) # Choose random mp3 sound  
    
    if (key == Key.end): # To stop program press "end" key
        return False

def playSound(name):
    mixer.init()
    mixer.music.load("sounds/"+name) # Music file can only be MP3
    mixer.music.play()
    
with Listener(on_press=on_press) as listener:
    listener.join()
