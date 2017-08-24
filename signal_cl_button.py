from tkinter import *
import sys
import numpy as np
import sys
import matplotlib.pyplot as plt



def Start():
	global count
	print("start")
	# plt.close()
	count = 0
	print('Window N ', count)
	plt.plot(t[0:window_size], x[0:window_size])
	plt.title('Window N ' + str(count))
	plt.show(block=False)

def Si():
	global count
	print("si")
	count = count + 1
	print('Window N ', count)
	train.append(1)
	plt.close()
	if count < windows:
		plt.plot(t[count*window_size:(count+1)*window_size], x[count*window_size:(count+1)*window_size])
		plt.title('Window N ' + str(count))
		plt.show(block=False)
	else:
		plt.close()
		Quit()
	

def No():
	global count
	print("no")
	count = count + 1
	print('Window N ', count)
	train.append(0)
	plt.close()
	if count < windows:
		plt.plot(t[count*window_size:(count+1)*window_size], x[count*window_size:(count+1)*window_size])
		plt.title('Window N ' + str(count))
		plt.show(block=False)
	else:
		plt.close()
		Quit()

def Quit():
	global count
	print("quit")
	plt.close()
	root.destroy()
	

dt = 0.01
n = 1000
fs = 1.0/dt
f = 1.3
window_size = 100
t = np.array([i*dt for i in range(n)])
x = np.array([np.cos(2*np.pi*f*i*dt) for i in range(n)])
# plt.ion()
train = []

print('asignacion++++++++++++++++++')
windows = int(n/window_size)
print('Number of windows to analyze: ', windows)

global root
root = Tk()
root.title('canv')
root.config(bg="white")
w,h=root.maxsize()
print("%dx%d"%(w,h))
root.geometry("%dx%d"%(450,150))

# Etiqueta de Si
botonn=Button(root,text="Si",font=('arial', 22, 'bold'),command=Si)
botonn['bg']='black'
botonn['fg']='orange'
botonn.place(x=20,y=40)

# Etiqueta de No
botonn=Button(root,text="No",font=('arial', 22, 'bold'),command=No)
botonn['bg']='dark blue'
botonn['fg']='orange'
botonn.place(x=90,y=40)

# Etiqueta de Start
botonn=Button(root,text="Start",font=('arial', 22, 'bold'),command=Start)
botonn['bg']='white'
botonn['fg']='black'
botonn.place(x=190,y=40)

# Etiqueta de Quit
botonn=Button(root,text="Quit",font=('arial', 22, 'bold'),command=Quit)
botonn['bg']='black'
botonn['fg']='white'
botonn.place(x=300,y=40)

root.mainloop()


print('!!!!!')
print(train)
print(len(train))
fig, ax = plt.subplots(nrows=1, ncols=1)
ax.set_xticks(np.arange(0, n*dt, window_size*dt))
ax.plot(t, x)
plt.grid()
plt.show()

print('!!!!!')

