from tkinter import *

window = Tk()
window.title("TODO-list")

content = Listbox(window, font="Ariel 18 bold")
test = StringVar()
e = Entry(window, font="Ariel 15", textvariable = test)
add = Button(window, text="ADD", font="Ariel 17", command=lambda content=content, test=test: 
content.insert(END, test.get()))
delete = Button(window, text="DELETE", font="Ariel 17", 
command=lambda content=content: content.delete(ANCHOR))

content.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
e.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
add.grid(row=2, column=0, padx=2, pady=2)
delete.grid(row=2, column=1, padx=2, pady=2)
window.mainloop()