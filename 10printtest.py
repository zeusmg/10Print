from tkinter import *
import random as r


master = Tk()
master.title("10 Print")
master.config(bg="black")
blankcanvas = Canvas(master, width=800, height=600,bg='dark green')
blankcanvas.pack()

x = 0
y = 0
spacing = 25
 

while y != int(blankcanvas['height']):
	if r.randint(0,1) <= 0.5:
		blankcanvas.create_line(x,y,x+spacing,y+spacing, fill='white')
	else:
		blankcanvas.create_line(x,y+spacing,x+spacing,y, fill='white')
	if int(blankcanvas['width']) < x:
		x = 0
		y=y+spacing
	else:
		x=x+spacing

mainloop()