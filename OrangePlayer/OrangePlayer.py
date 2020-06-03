import pygame
import tkinter as tkr
import os
from tkinter import filedialog, messagebox

#Create window
window = tkr.Tk()
window.title("OrangePlayer")
window.geometry("640x400")
window.configure(bg="black")

#Create menubar
menubar = tkr.Menu(window)
filemenu = tkr.Menu(menubar, tearoff=0)

def onOpenAlbum():
    file = filedialog.askdirectory()
    os.chdir(file)
    songlist = os.listdir()
    for song in songlist:
        pos = 0
        playlist.insert(pos, song)
        pos += 1
    Play()
    
def onOpenSong():
    global filename
    filename = None
    filename = filedialog.askopenfilename()
    song.set(os.path.basename(filename))
    playlist.delete(0, playlist.size())
    playlist.pack(side="left", fill="y")
    Play()

def onAbout():
    messagebox.showinfo("About OrangePlayer", "This is music player build with Python Tkinter by Orange")   

filemenu.add_command(label="Open Album", command=onOpenAlbum)
filemenu.add_command(label="Open Song", command=onOpenSong)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tkr.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=onAbout)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

#Pygame init
pygame.init()
pygame.mixer.init()

#Image import
play_img = tkr.PhotoImage(file=r"\img\play.png")
stop_img = tkr.PhotoImage(file=r"\img\stop.png")
pause_img = tkr.PhotoImage(file=r"\img\pause.png")
resume_img = tkr.PhotoImage(file=r"\img\resume.png")

#Button frame
button_frame = tkr.Frame(window)
button_frame.grid(row=0, column=0, columnspan=4)
button_frame.config(bg="black", padx=10, pady=10)

#Playlist frame
playlist_frame = tkr.Frame(window)
playlist_frame.grid(row=3, column=0, columnspan=4)
playlist_frame.config(bg="black", padx=10, pady=10)

#Playlist
playlist = tkr.Listbox(playlist_frame, highlightcolor="blue",\
selectmode=tkr.SINGLE, bg="orange", width=98, height=10)
playlist.pack(side="left", fill="y")

#Playlist scrollbar
scrollbar = tkr.Scrollbar(playlist_frame, orient="vertical")
scrollbar.config(command=playlist.yview)
scrollbar.pack(side="right", fill="y")
playlist.config(yscrollcommand=scrollbar.set)

#Volume
def Volume(value):
    volume = int(value)/100
    pygame.mixer.music.set_volume(volume)

VolumeLevel = tkr.Scale(button_frame, from_=0, to_=100, length=600,\
orient=tkr.HORIZONTAL, resolution=1, bg="orange", command=Volume)
VolumeLevel.grid(row=1, column=0, columnspan=4, padx=5, pady=15)
VolumeLevel.set(50)

#Play 
def Play():       
    if playlist.size() == 0 and filename == None:
        pass
    else:
        if playlist.size() == 0:
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()              
        else:
            pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
            song.set(playlist.get(tkr.ACTIVE)) 
            pygame.mixer.music.play()
    
play_button = tkr.Button(button_frame, width=120, height=50,\
image=play_img, command=Play, bg="orange", relief="solid")
play_button.grid(row=0, column=0)

#Stop
def Stop():
    pygame.mixer.music.stop()

stop_button = tkr.Button(button_frame, width=120, height=50, image=stop_img, command=Stop, bg="orange", relief="solid")
stop_button.grid(row=0, column=1)

#Pause and Unpause
def Pause():
    pygame.mixer.music.pause()

def Unpause():
    pygame.mixer.music.unpause()

pause_button = tkr.Button(button_frame, width=120, height=50, image=pause_img, command=Pause, bg="orange", relief="solid")
unpause_button = tkr.Button(button_frame, width=120, height=50, image=resume_img, command=Unpause, bg="orange", relief="solid")
pause_button.grid(row=0, column=2)
unpause_button.grid(row=0, column=3)

#Current song name
song = tkr.StringVar()
songtitle = tkr.Label(button_frame, textvariable=song, bg="orange")
songtitle.config(font=("Courier", 12))
songtitle.grid(row=2, column=0, columnspan=4)

window.mainloop()