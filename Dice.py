import tkinter as tk
from PIL import Image, ImageTk
import random

# adding images
dice = ["die1.png", "die2.png", "die3.png",
        "die4.png", "die5.png", "die6.png"]
root = tk.Tk()
root.title("Dice Simulator")
root.geometry("500x400")

# lable
l1 = tk.Label(root, text="Dice Simulator", fg="yellow",
              bg="black", font="Helvetica 16")
l1.pack()
img = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# img lable
l2 = tk.Label(root, image=img)
l2.image = img
l2.pack()


def roll():
    img = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    l2.configure(image=img)
    l2.image = img


# button
button = tk.Button(root, text="Roll The Dice", fg='blue', command=roll)
button.pack()

root.mainloop()
