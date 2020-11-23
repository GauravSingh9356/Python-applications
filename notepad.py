from tkinter import *
import os
import webbrowser
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox as tmsg

def newFile():
    global file
    
    root.title("Untitled-Notepad")
    file=None
    textArea.delete(1.0, END)

def openFile():
    file = askopenfilename(defaultextension = ".txt", filetypes=[("All Files", "*.*"), ("Text Documnet", "*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        textArea.delete(1.0, END)
        f  = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()
        

def saveFile():
    global file
    if file==None:
        file = asksaveasfilename(initialfile= "Untitled.txt", defaultextension = ".txt", filetypes=[("All Files", "*.*"), ("Text Documnet", "*.txt")])

        if file=="":
            file=None
        else:
            # save as new file
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()
            
            root.title(os.path.basename(file) + "-Notepad")
    else:
        # save the file
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()
def quitApp():
    root.destroy()


def cut():
    textArea.event_generate("<<Cut>>")


def copy():
    textArea.event_generate("<<Copy>>")


def paste():
    textArea.event_generate("<<Paste>>")


def about():
    tmsg.showinfo("About", "Notepad by Gaurav Singh ")


def MessageMe():
    tmsg.showinfo("Email", "Email - gs935688@gmail.com")
    reply = tmsg.askyesno("Message", "Do you want to contact now?")
    print(reply)
    if reply:
        webbrowser.open_new("https://gmail.com")
    else:
        tmsg.showinfo("Reply", "We will meet soon...")
    
    
def openGithub():
    webbrowser.open_new("https://github.com/gauravsingh9356")
    

def openLinkedIn():
    webbrowser.open_new("https://linkedIn.com/in/gauravsingh9356")
    
def openInstagram():
    webbrowser.open_new("https://instagram.com/gauravsingh9356_")

root = Tk()
root.title("Untitled-Notepad")
root.geometry("744x688")

root.wm_iconbitmap("notepad.ico")

file = None

textArea = Text(root, font="Castoro 14")
textArea.pack(expand = True, fill=BOTH)


# Menubar

MenuBar = Menu(root)
Filemenu = Menu(MenuBar, tearoff=0)


#File menu
# open new file


Filemenu.add_command(label = "New", command = newFile)

# exixting file oopneing
Filemenu.add_command(label = "Open", command = openFile)

# save the current file

Filemenu.add_command(label = "Save", command = saveFile)

Filemenu.add_separator()

Filemenu.add_command(label = "Exit", command = quitApp)


MenuBar.add_cascade(label = "File", menu = Filemenu)

# File menu ends


# Edit Menu


Editmenu = Menu(MenuBar, tearoff=0)

Editmenu.add_command(label="Cut", command = cut)
Editmenu.add_command(label="Copy", command = copy)
Editmenu.add_command(label="Paste", command = paste)



MenuBar.add_cascade(label = "Edit", menu = Editmenu)

# editmenu ends


#help


HelpMenu = Menu(MenuBar, tearoff=0)

HelpMenu.add_command(label="About Notepad", command = about)
HelpMenu.add_command(label="Mesaage Me", command = MessageMe)

MenuBar.add_cascade(label = "Help", menu = HelpMenu)

# help menu ends


ConnectMenu = Menu(MenuBar, tearoff=0)

ConnectMenu.add_command(label = "GitHub", command=openGithub)
ConnectMenu.add_command(label = "LinkedIn", command=openLinkedIn)
ConnectMenu.add_command(label = "Instgram", command=openInstagram)


MenuBar.add_cascade(label ="Connect", menu = ConnectMenu)
root.config(menu = MenuBar)

# Adding scrollbar


Scroll = Scrollbar(textArea)

Scroll.pack(sid=RIGHT, fill=Y)
Scroll.config(command = textArea.yview)

textArea.config(yscrollcommand= Scroll.set)

root.mainloop()
