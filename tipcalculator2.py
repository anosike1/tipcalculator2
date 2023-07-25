# to see our first TIP CALCULATOR, see the link in the description
# we will be using the tkinter module to create this version of our tip calculator
# import tkinter
from tkinter import *

# define the title of the window
# and configure the dimensions
window = Tk()
window.title ("TIP CALCULATOR")
window.config (width=500, height=300)

# define the labels (texts and positions)
label1 = Label (text="Total Bill")
label1.grid (row=1, column=0)

label2 = Label (text="% Tip")
label2.grid (row=2, column=0)

label3 = Label (text="No. of Persons")
label3.grid (row=3, column=0)

label4 = Label (text="")
label4.grid (row=5, column=1)

# define the entries and their positions
entry1 = Entry()
entry1.grid (row=1, column=1)
entry2 = Entry()
entry2.grid (row=2, column=1)
entry3 = Entry()
entry3.grid (row=3, column=1)

# define the function calc()
# this function takes/ gets the entry responses and assigns them to constants
def calc():
    x = float(entry1.get())
    y = float(entry2.get())
    z = float(entry3.get())
    # calculate th bill per person and round it up to 2 decimal place
    tot = x + (x * y/100)
    bill_per_person = tot/z
    roundd = round (bill_per_person, 2)
    # also change Label 4 which is a blank text
    label4.config (text=f"Each person should pay {roundd}")

# Define a button  
button1 = Button (text="CALCULATE",command=calc)
button1.grid (row=4, column=1)

mainloop()