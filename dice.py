import tkinter
from PIL import Image, ImageTk
import random

# Setting up the window
window = tkinter.Tk()
WIDTH = 400
HEIGHT = 400
window.geometry(f'{WIDTH}x{HEIGHT}')
window.title('Dice Rolling Simulator')
window.resizable(0, 0)

# Creating title
label = tkinter.Label(window, text='Roll the Dice', font="arial 18 bold")
label.place(x=200, y=30, anchor="center")


# Dice images for rolling
dice_image = ['DICE_1.PNG', 'DICE_2.PNG', 'DICE_3.PNG', 'DICE_4.PNG', 'DICE_5.PNG', 'DICE_6.PNG']
display_image = ImageTk.PhotoImage(Image.open(random.choice(dice_image)))
image_display = tkinter.Label(image=display_image)
image_display.place(x=200, y=200, anchor="center")
image_display.image = display_image


# Rolling the dice
def dice_rolling():
    display_image = ImageTk.PhotoImage(Image.open(random.choice(dice_image)))
    image_display = tkinter.Label(image=display_image)
    image_display.configure(image=display_image)
    image_display.place(x=200, y=200, anchor="center")
    image_display.image = display_image


# Creating a button
button = tkinter.Button(window, text='Roll', font='arial 14 bold', padx=5, command=dice_rolling)
button.place(x=200, y=360, anchor="center")

# Main game loop
window.mainloop()
