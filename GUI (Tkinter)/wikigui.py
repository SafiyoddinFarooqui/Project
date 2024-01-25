from tkinter import *
import tkinter as tk

import wikipedia

def wiki():
    topic = enrty.get()
    try:
        summary = wikipedia.summary(topic, sentences =2)
        output.delete(2.0,tk.END)
        output.insert(1.0,summary)
    except Exception as e:
        output.delete(1.0,tk.END)
        output.insert(1.0,e)

root = Tk()
root.title("Wikipedia Summary App")

enrty = tk.Entry(root)
enrty.pack()

button1 = tk.Button(text="Search on WIKI", command=wiki)
button1.pack()

output = tk.Text(root, height =10, width = 50 , wrap = tk.WORD)
output.pack()
button = tk.Button(text="Quit", command=root.destroy)
button.pack()

root.mainloop()