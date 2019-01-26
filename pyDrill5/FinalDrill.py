
from tkinter import *
import tkinter as tk
import FinalDrillFunc

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)

        # define our master fram configuration
        self.master = master
        self.master.minsize(600,200) #height,width
        self.master.maxsize(600,200)
        self.master.title("Final Drill")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clocks the upper corner, "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: FinalDrillFunc.ask_quit(self))
        arg = self.master

        self.master = master
        self.master.geometry('{}x{}'.format(600, 200))
        self.master.title("Final Drill")
        self.master.config(bg='lightgray')

        self.btnBrowse1 = Button(self.master, text="Browse Source", width=12, height=1, command=lambda: FinalDrillFunc.BrowSrc(self))
        self.btnBrowse1.grid(row=0,column=1,padx=(20,0),pady=(40,10))

        self.btnBrowse2 = Button(self.master, text="Browse Dest.", width=12, height=1, command=lambda: FinalDrillFunc.BrowDir(self))
        self.btnBrowse2.grid(row=1,column=1,padx=(20,0),pady=(20,10))

        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2, command=lambda: FinalDrillFunc.dirSwitch(self))
        self.btnCheck.grid(row=2,column=1,padx=(20,0),pady=(0))

        
        self.txtBox1 = Entry(self.master,font=('Helvetica', 16), fg='black', bg='white',width=30)
        self.txtBox1.grid(row=0,column=2,padx=(20,0),pady=(30,0), columnspan=2)

        self.txtBox2 = Entry(self.master,font=('Helvetica', 16), fg='black', bg='white',width=30)
        self.txtBox2.grid(row=1,column=2,padx=(20,0),pady=(10,0), columnspan=2)

        

        


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
