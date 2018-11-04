from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from sys import platform
from os import system

import tkinter
import editorSettings
import tkinter.scrolledtext as scrollText


commandKey = ''
file_path = 'Untitled'

if platform == 'darwin':
    commandKey = 'Command'
else:
    commandKey = 'Control'


root = Tk()
editArea = scrollText.ScrolledText(
    font=(
        str(editorSettings.fontName),
        int(editorSettings.fontSize)
    )
)

editArea.pack(expand=True, fill='both')


root.title(file_path)



def openFile(event=None):
    global editArea
    global file_path

    file_path = filedialog.askopenfilename()

    try:
        file = open(file_path, 'r')
        editArea.delete('1.0', END)
        editArea.insert(INSERT, file.read())
        file.close()
        root.title(file_path)
    except:
        return


def saveFile(event=None):
    global editArea
    global file_path

    if file_path == 'Untitled':
        saveAsFile()
    elif file_path == 'Settings':
        file = open('src/editorSettings.py', 'w')
        file.write(str(editArea.get(1.0, END)))
        file.close()
        root.title('Settings')
    else:
        file = open(str(file_path), 'w')
        file.write(str(editArea.get(1.0, END)))
        file.close()
        root.title(file_path)


def insertTab(event=None):
    editArea.insert(tkinter.INSERT, " " * editorSettings.tabSize)
    return 'break'


def saveAsFile():
    global editArea
    global file_path
    
    if file_path == 'Settings':
        pass
    else:
        file = filedialog.asksaveasfile(mode='w')
        if file is None:
            return
        
        writeText = str(editArea.get(1.0, END))
        file.write(writeText)
        file.close()

        file_path = file
        root.title(file.name)


def openSettingsFile():
    global editArea
    global file_path
    global settingsState

    try:
        file = open('src/editorSettings.py', 'r')
        editArea.delete('1.0', END)
        editArea.insert(INSERT, file.read())
        file.close()
        file_path = 'Settings'
        root.title('Settings')
    except:
        return



def showAbout():
    messagebox.showinfo('About', 'Author: John Paul Antonovich\n\nLicense: MIT\n\nDescription: A simple text editor built with Python and the Tkinter library.')


menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Open  ' + commandKey + '-o', command=openFile)
filemenu.add_command(label='Save  ' + commandKey + '-s', command=saveFile)
filemenu.add_command(label='Save As  ' + commandKey + '-Shift-S', command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)


settingsmenu = Menu(menubar, tearoff=0)
settingsmenu.add_command(label='Open Prefrences', command=openSettingsFile)
menubar.add_cascade(label='Settings', menu=settingsmenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='About', command=showAbout)
menubar.add_cascade(label='Help', menu=helpmenu)

root.config(menu=menubar)

editArea.bind('<Tab>', insertTab)
root.bind('<' + commandKey + '-s>', saveFile)
root.bind('<' + commandKey + '-o>', openFile)
root.bind('<' + commandKey + '-Shift-S>', saveAsFile)


root.minsize(450, 450)

root.mainloop()
