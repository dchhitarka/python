from tkinter import *
from tkinter import filedialog
#import ScrolledText

window = Tk()
window.title("Text Editor")

#textPad = ScrolledText.ScrolledText(root, width=100, height=80)


mainMenu = Menu(window)
window.config(menu=mainMenu)

def openFile(): 
    try:
        fileOpen = filedialog.askopenfile('r', title="Select File", 
        filetypes=[("All Files", "*.*")])
        content.insert(END, fileOpen.read())
    except:
        print("Unable to load the file")
    finally:
        if fileOpen:
            fileOpen.close()

def saveFile():
    save = filedialog.asksaveasfile('w', defaultextension=".txt")
    if save is None:
        return
    try:
        fileText = str(content.get(1.0, END))
        save.write(fileText)
    except:
        print("Cannot Save the File")
    finally:
        save.close()

def close():
    window.destroy()

    
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
#fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Exit", command=close)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)
# editMenu.add_command(label="Undo", command=undoFile)
# editMenu.add_command(label="Redo", command=redoFile)
# editMenu.add_command(label="Cut", command=cutFile)
# editMenu.add_command(label="Copy", command=copyFile)
# editMenu.add_command(label="Paste", command=pasteFile)

content = Text(window, width=100)
content.grid(row=0, column=0, padx=5, pady=5)

#textPad.pack()
window.mainloop()