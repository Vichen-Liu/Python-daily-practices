from tkinter import *
canvas=Canvas(width=300,height=300,bg="white")
canvas.pack(expand=True,fill=BOTH)
x0=163
y0=163
y1=175
for i in range(19):
    canvas.create_line(x0,y0,x0,y1,width=1,fill="red")
    x0-=5
    y0-=5
    y1+=5

x0=163
y0=163
y1=175
for i in range(19):
    canvas.create_line(x0,y0,x0,y1,width=1,fill="red")
    x0+=5
    y0+=5
    y1+=5

mainloop()

