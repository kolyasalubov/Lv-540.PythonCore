import time,random
from tkinter import*
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()


canvas.create_rectangle(190,480,310,500,fill='black')

b=0

canvas.create_rectangle(240,460,260,480,fill='black')
shots=0 
canvas.create_text(420,100,text='кількість пострілів '+str(shots))
                  

def ball(event):
    global b,shots,yb
    if shots<10:
        canvas.delete(b)
        b=canvas.create_oval(240,460,260,480,fill='gray')
        yb=460
        canvas.create_text(420,100,text='кількість пострілів '+str(shots),fill='#F0F0ED')
        shots=shots+1
        canvas.create_text(420,100,text='кількість пострілів '+str(shots))
    else:
        canvas.create_text(50,50,text="Ядра закінчилися!")

canvas.bind_all('<space>',ball)

ship_image=PhotoImage(file='ship.gif')
s=canvas.create_image(500, 0,anchor=NW, image=ship_image)
pow_image=PhotoImage(file='pow.gif')
k=0
yb=460

canvas.create_text(420,140,text='кількість влучень '+str(k))
for z in range(10):
    canvas.create_text(420,120,text='кількість кораблів '+str(z),fill='#F0F0ED')
    canvas.create_text(420,120,text='кількість кораблів '+str(z+1))
    xs=500
    yb=460
    v=random.randint(2,5)
    for y in range(0,300):
        canvas.move(s,-v,0)
        canvas.move(b,0,-5)
        tk.update()
        time.sleep(0.02)
        xs=xs-v
        yb=yb-5
      
        if 140<xs<260 and 0<yb<30:
            p=canvas.create_image(230, 10,anchor=NW, image=pow_image)
            tk.update()
            time.sleep(2)
            canvas.delete(b)
            canvas.delete(p)
            k=k+1
            canvas.create_text(420,140,text='кількість влучень '+str(k-1),fill='#F0F0ED')
            canvas.create_text(420,140,text='кількість влучень '+str(k))
            break
    canvas.coords(s,500,0)
