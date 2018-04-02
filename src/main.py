from Tkinter import *
import sys
import subprocess as sub

p = sub.Popen(["python", "./PyD3.py"] + sys.argv[1:],stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()

root = Tk()
text = Text(root)
text.pack()
text.insert(END, output)
root.mainloop()
