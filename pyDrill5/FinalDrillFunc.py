import tkinter
from tkinter import *
from tkinter import filedialog
import os
import sqlite3
import FinalDrill
from tkinter import messagebox
import os
import shutil

def BrowSrc(self): #searches a folder and places path into txtbox1
    global folder_selected1
    folder_selected1 = filedialog.askdirectory()
    self.txtBox1.insert(INSERT, folder_selected1)
    dirSwitch(self,folder_selected1)


def BrowDir(self): #searches a folder and places path into txtbox2
    global folder_selected2
    folder_selected2 = filedialog.askdirectory()
    self.txtBox2.insert(INSERT, folder_selected2)

def ask_quit(self):
    if messagebox.askokcancel("Exit Progress", "Okay to exit application?"):
        #this closes the app
        self.master.destroy()
        os._exit(0)

def dirSwitch(folder_selected1,folder_selected2):
    myPath = (folder_selected1)
    listDir = os.listdir(myPath)
    dirArray = []
    i = 0
    while i < len(listDir):
    #isolate extention
        splitPath = os.path.splitext(listDir[i])
        #does it end in .txt
        if splitPath[1] == ".txt":
        #if .txt concat path and time
            print(listDir[i])
            shutil.move(listDir[i],folder_selected2)

        i += 1
    print(dirArray)



if __name__ == "__main__":
    pass
