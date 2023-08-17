from tkinter import *
import ttkbootstrap as ttb
import win32api
import win32con
import time
import math

root=ttb.Window(themename='vapor')
root.geometry('500x500')
root.resizable(False,False)
root.title('Draw')

centro_x=0
centro_y=0


def registrar(event,label:ttb.Label):
    global centro_x,centro_y
    if event.keysym=='p':
        botao_centro.configure(state='normal')
        label.grid_forget()
        centro_x,centro_y=win32api.GetCursorPos()
        label_x.configure(text=f'{centro_x}')
        label_y.configure(text=f'{centro_y}')
        
def draw():
    raio=int(raio_tk.get())
    passos=int(passos_tk.get())    
    localizaocao_x=centro_x
    localizaocao_y=centro_y
    

    posicoes_x=[]
    posicoes_y=[]

    posicoes_x.append(localizaocao_x+(raio*math.cos(0*math.pi/180)))
    posicoes_y.append(localizaocao_y+(raio*math.sin(0*math.pi/180)))

    angulos=[(360/passos)*i for i in range(passos)]
    for angulo in angulos:
        posicoes_x.append(localizaocao_x+(raio*math.cos(angulo*math.pi/180)))
        posicoes_y.append(localizaocao_y+(raio*math.sin(angulo*math.pi/180)))

    posicoes_x.append(localizaocao_x + (raio * math.cos(0*math.pi/180)))
    posicoes_y.append(localizaocao_y + (raio * math.sin(0*math.pi/180)))
    posicoes_x.append(localizaocao_x + (raio * math.cos(1*math.pi/180)))
    posicoes_y.append(localizaocao_y + (raio * math.sin(1*math.pi/180)))


    win32api.SetCursorPos((int(posicoes_x[0]),int(posicoes_y[0])))
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(1)
    

    for i in range(0,len(posicoes_x)):
        win32api.SetCursorPos((int(posicoes_x[i]),int(posicoes_y[i])))
        time.sleep(0.01)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def centro():
    botao_centro.configure(state='disabled')
    label_atencao=ttb.Label(frame_principal,text="Clique na tecla 'p' para registrar a posição do mouse",bootstyle='danger')
    label_atencao.grid(row=5,column=0,columnspan=3)
    root.bind('<Key>',lambda event: registrar(event,label_atencao))
    
botao_centro=ttb.Button(root,text='Localizar Centro',command=centro)
botao_centro.pack(pady=20)

botao_desenhar=ttb.Button(root,text='Desenhar Círculo',command=draw)
botao_desenhar.pack(pady=20)

frame_principal=ttb.Frame(root)

ttb.Label(frame_principal,text='Posição X:').grid(row=0,column=0)
label_x=ttb.Label(frame_principal,text=f'{centro_x}')
label_x.grid(row=0,column=1,pady=20)

ttb.Label(frame_principal,text='Posição Y:').grid(row=1,column=0)
label_y=ttb.Label(frame_principal,text=f'{centro_x}')
label_y.grid(row=1,column=1,pady=20)

ttb.Label(frame_principal,text='Raio:',font=('Arial',14)).grid(row=3,column=0,pady=20)

raio_tk=ttb.Spinbox(frame_principal,from_=100,to=500,state='readonly')
raio_tk.grid(row=3,column=1,pady=20)

ttb.Label(frame_principal,text='Passos:',font=('Arial',14)).grid(row=4,column=0,pady=20)

passos_tk=ttb.Spinbox(frame_principal,from_=10,to=10000,state='readonly')
passos_tk.grid(row=4,column=1,pady=20,padx=10)

frame_principal.pack(padx=10,pady=20)

root.mainloop()