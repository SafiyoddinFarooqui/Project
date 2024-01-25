from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

def roll_dice():
    random_img = random.randrange(1, 7)
    image_name = f"{random_img}.png"
    
    # Open the image using PIL (Pillow) and convert it to Tkinter PhotoImage
    img = Image.open(image_name)
    img = ImageTk.PhotoImage(img)
    
    # Keep a reference to the image
    roll_dice.image = img
    
    label.config(image=img)
    label.image = img  # Keep a reference to the image to prevent garbage collection

root = Tk()
root.title("Dice")

label = ttk.Label(text="Please Click On Roll Button For Results")
label.pack()

roll_dice.image = None  # Initialize the image reference

rolldice = ttk.Button(text="Roll", command=roll_dice)
rolldice.pack()

quit_button = ttk.Button(text="Quit", command=root.destroy)
quit_button.pack()

root.mainloop()
