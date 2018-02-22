from Tkinter import *

top = Tk()
file_path_label = Label(top, text="Path to data set: " )
file_path_label.pack( side = LEFT)
file_path = Entry(top, bd =5)
file_path.pack(side = RIGHT)

top.mainloop()
