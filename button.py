from tkinter import *
import sys
import numpy as np
import sys

def Si():
    print("hola")

def No():
    print("chao")
    

    
    


global root
root = Tk()
root.title('canv')
root.config(bg="white")
w,h=root.maxsize()
print("%dx%d"%(w,h))
root.geometry("%dx%d"%(500,500))


# Etiqueta de Si
botonn=Button(root,text="Si",font=('arial', 22, 'bold'),command=Si)
botonn['bg']='black'
botonn['fg']='orange'
botonn.place(x=20,y=40)

# Etiqueta de Si
botonn=Button(root,text="No",font=('arial', 22, 'bold'),command=No)
botonn['bg']='dark blue'
botonn['fg']='orange'
botonn.place(x=80,y=40)


#Etiqueta de Si
#et_Si = Button(root,font=('ubuntu', 22, 'bold'), bg='light blue', fg='black',text="Si",command=Si)
#et_Si['bg']='green'
#et_Si.place(x=280,y=180)

root.mainloop()

print('!!!!!')