from tkinter import *
canvas=Canvas(width=500,height=400)
canvas.pack(expand=True,fill=BOTH)
k=1
j=1
for i in range(26):
    canvas.create_oval(500-k,500-k,500+k,500+k,width=1)
    k+=j
    j+=0.5

mainloop()