import time
from tkinter import *


def digiclock():
    # formatting time
    watch = time.strftime('%I:%M:%S')
    # "I" will show 12 hours format of time or else can replace "I" with "H" to show 24 hours format of time.
    # '-' before 'I' will discard any leading zeros
    # assigning watch as text to label1
    label1['text'] = watch
    # after 100 milliseconds call my clock
    label1.after(100, digiclock)



win = Tk()
win.geometry('400x200')
#
win.title('Digital clock')
# title of the clock

label1 = Label(win, bg='yellow', font=('Times new roman', 40))
# bg will set up the background color, win indicates window parents of label,font as tuple  to set up font style , size.
label1.pack(fill=BOTH, expand=True)
# fill both in 'x' and 'y' directions and expand true will fill entire region

# calling digiclock function
digiclock()
win.mainloop()