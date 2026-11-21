from tkinter import *
canvas=Canvas(width=300,height=300,bg="white")
canvas.pack(expand=True,fill=BOTH)
x0=163
y0=163
x1=175
y1=175
for i in range(19):
    canvas.create_rectangle(x0,y0,x1,y1,width=1,outline="blue")
    x0-=5
    y0-=5
    x1+=5
    y1+=5

mainloop()