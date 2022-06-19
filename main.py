import os
import pygame
from tkinter import *
from tkinter import Button
from tkinter import Label
from tkinter import Tk
from tkinter import filedialog

from pygame import mixer

current_volume = float(0.5)

def play_song():
    filename = filedialog.askopenfilename(initialdir="C:", title="select song")
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]
    print(song_title)

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="grey", text="now playing" + str(song_title))
        volume_label.config(fg="grey", text="Volume:" + str(current_volume))
    except EXCEPTION as e:
        print(e)
        song_title_label.config(fg="red", text="error")

def reduce_volume():
    try:
        global current_volume
        if current_volume <= 0:
            volume_label.config(fg="grey" , text="Volume : Muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="grey", text="Volume:" +str(current_volume))
    except EXCEPTION as e:
        print()
        song_title_label.config(fg="red", text="Track hasn't been selected")


def increase_volume():
    try:
        global current_volume
        if current_volume >= 1:
            volume_label.config(fg="grey", text="Volume : Max")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="grey", text="Volume:" + str(current_volume))
    except EXCEPTION as e:
        print()
        song_title_label.config(fg="red", text="Track hasn't been selected")

def pause():
    try:
        mixer.music.pause()
    except EXCEPTION as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn't been selected")


def resume():
    try:
        mixer.music.unpause()
    except EXCEPTION as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn't been selected")


root = Tk()
root.title(" Mood Based Music Player")

Label(root, text="Music Player", font=("Calibri", 15), fg="black").grid(sticky="N", row=0, padx=120)
Label(root, text="please select", font=("Calibri", 12), fg="grey").grid(sticky="N", row=1)
Label(root, text="Volume", font=("Calibri", 12), fg="black").grid(sticky="N", row=4)
song_title_label = Label(root, font=("Calibri", 12))
song_title_label.grid(sticky="N", row=3)
volume_label = Label(root, font=("Calibri", 12))
volume_label.grid(sticky="N", row=5)


Button(root, text="Select Song", font=("Calibri", 15), fg="black",command=play_song).grid(sticky="N", row=2)
Button(root, text="Pause", font=("Calibri", 15), fg="black", command=pause).grid(sticky="E", row=3, )
Button(root, text="Resume", font=("Calibri", 15), fg="black", command=resume).grid(sticky="W", row=3)
Button(root, text="+", font=("Calibri", 15), fg="black", width=5, command=increase_volume).grid(sticky="W", row=5)
Button(root, text="-", font=("Calibri", 15), fg="black", width=5, command=reduce_volume).grid(sticky="E", row=5)

root.mainloop()
