from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

def james():
    message = 'scholar james😂'
    print(message)
    word.config(text=message)
window = Tk()
window.minsize(width=500, height=500)
button = Button(text='submit', command=james)
window.title('python app')
word =Label(text='Enter your username')
word.pack()
input = Entry()
input.pack()
button.pack()
window.mainloop()