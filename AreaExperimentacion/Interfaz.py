import tkinter as tk
from tkinter.constants import X

ventana = tk.Tk()
ventana.title("VENTANA TITULO")
ventana.geometry("400x200")

def restar():
    
    v1=txt.get()
    v2=txt2.get()
    if(v1=="" or v2==""):
        return
    n1=int(v1)
    n2=int(v2)
    lbl3.delete(0,"end")
    lbl3.insert(0,str((n1-n2)))
    


lbl = tk.Label(ventana,text="primer numero",bg="yellow")
lbl.place(x=10,y=10,width=130,height=30)
txt = tk.Entry(ventana,bg="pink")
txt.place(x=150,y=10,width=100,height=30)

lbl2 = tk.Label(ventana,text="segundo numero",bg="yellow")
lbl2.place(x=10,y=50,width=130,height=30)
txt2 = tk.Entry(ventana,bg="pink")
txt2.place(x=150,y=50,width=100,height=30)

lbl3=tk.Entry(ventana,bg="cyan")
lbl3.place(x=10,y=90,width=100,height=30)

btn = tk.Button(ventana,text="calcular",command=restar)
btn.place(x=270,y=50,width=100,height=30)




ventana.mainloop()