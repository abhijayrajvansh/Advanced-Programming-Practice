#/
#    author:   abhijayrajvansh
#    created:  24.04.2022 16:46:22
#/
from tkinter import *

# Global Dimensions Parameters
HEIGHT = 300
WEIDTH = 500


# Root Functioning
root = Tk()


# Canvas creation
canvas = Canvas(root, height = HEIGHT, width = WEIDTH)
canvas.pack()

# Frame
frame = Frame(root)
frame.place(relwidth = 1, relheight = 1)

# Objects
button = Button(root, text = "Click here to exit", width = 20, command = root.destroy)
button.pack()

# Lable
label = Label(frame, text = "Hello World, This is a Label")
label.pack()

# Entry: Some area to type some text
entry = Entry(frame, bg = 'black')
entry.pack()

root.mainloop()