from pygame import mixer
import keyboard

import random
import os

import config

file_path = config.PATH
print(file_path)
soundsList = os.listdir(file_path + "\sounds")
soundsList.remove("diff")  # Remove diff folder

print("\n\n Press 'END' to STOP \n\n")
print(" Listener Started")

def on_key_release(e):
    print(e.name)
    if e.name == 'space':
        playSound("diff\yamete.mp3")
    elif e.name == 'enter':
        x = random.randint(1, 3)
        if x == 1:
            playSound("diff\hoo1.mp3")
        elif x == 2:
            playSound("diff\hoo2.mp3")
        else:
            playSound("diff\hoo3.mp3")
    if e.name not in ['enter', 'space', 'esc', 'end']:
        playSound(random.choice(soundsList))  # Choose random mp3 sound

    if e.name == 'end':  # To stop program press "end" key
        return False


def playSound(name):
    mixer.init()
    mixer.music.load(file_path + "\sounds\\" + name)  # Music file can only be MP3
    mixer.music.play()


keyboard.hook(on_key_release)
keyboard.wait('end')