# from tkinter import *
import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy import interpolate

def mag_fft(x, fs):
	fftx = np.fft.fft(x)
	fftx = np.abs(fftx)/len(fftx)
	fftx = 2*fftx[0:int(len(fftx)/2)]
	tr = len(x)/fs
	df = 1.0/tr
	f = np.array([i*df for i in range(len(fftx))])
	magX = fftx
	return magX, f, df

def sifting_iteration(t, x):
	s_number = 5
	tolerance = 10
	error = 5000
	max_iter = 505
	min_iter = 500
	cont = 0
	s_iter = 10
	while (error > tolerance or s_iter < s_number):
		print('++++++++iteration ', cont)
		h1, extrema_x = sifting2(t, x)
		if cont > min_iter:
			error_extrema = extrema(h1)-extrema_x
			error_xzeros = xzeros(h1)-xzeros(x)		
			error = error_extrema + error_xzeros
			print(error)
			# if error < tolerance:
				# s_iter = s_iter + 1
			# else:
				# s_iter = 0
			# print('Conseq. it = ', s_iter)
		x = h1
		cont = cont + 1
		if cont > max_iter:
			break
	return h1

def extrema(x):
	n = len(x)
	n_extrema = 0
	for i in range(n-2):
		if (x[i+1] < x[i] and x[i+2] > x[i+1]):
			n_extrema = n_extrema + 1
	for i in range(n-2):
		if (x[i+1] > x[i] and x[i+2] < x[i+1]):
			n_extrema = n_extrema + 1

	return n_extrema

def xzeros(x):
	n = len(x)
	n_xzeros = 0
	for i in range(n-1):
		if (x[i] > 0 and x[i+1] < 0):
			n_xzeros = n_xzeros + 1
	for i in range(n-1):
		if (x[i] < 0 and x[i+1] > 0):
			n_xzeros = n_xzeros + 1

	return n_xzeros
	
def env_down(t, x):
	n = len(x)
	x_down = []
	t_down = []
	x_down.append(x[0])
	t_down.append(t[0])
	for i in range(n-2):
		if (x[i+1] < x[i] and x[i+2] > x[i+1]):
			x_down.append(x[i+1])
			t_down.append(t[i+1])
	x_down.append(x[n-1])
	t_down.append(t[n-1])
	x_down = np.array(x_down)
	t_down = np.array(t_down)

	return t_down, x_down


def env_up(t, x):
	n = len(x)
	x_up = []
	t_up = []
	x_up.append(x[0])
	t_up.append(t[0])
	for i in range(n-2):
		if (x[i+1] > x[i] and x[i+2] < x[i+1]):
			x_up.append(x[i+1])
			t_up.append(t[i+1])
	x_up.append(x[n-1])
	t_up.append(t[n-1])
	x_up = np.array(x_up)
	t_up = np.array(t_up)
	
	return t_up, x_up

def sifting(t, x):
	t_up, x_up = env_up(t, x)
	t_down, x_down = env_down(t, x)

	tck = interpolate.splrep(t_up, x_up)
	x_up = interpolate.splev(t, tck)
	tck = interpolate.splrep(t_down, x_down)
	x_down = interpolate.splev(t, tck)

	x_mean = (x_up + x_down)/2
	h = x - x_mean
	return h

def sifting2(t, x):
	t_up, x_up = env_up(t, x)
	t_down, x_down = env_down(t, x)
	extrema_x = len(x_up) + len(x_down)
	
	tck = interpolate.splrep(t_up, x_up)
	x_up = interpolate.splev(t, tck)
	tck = interpolate.splrep(t_down, x_down)
	x_down = interpolate.splev(t, tck)

	x_mean = (x_up + x_down)/2
	h = x - x_mean
	return h, extrema_x
#++++++++++++++++++++++++++++DEFINITION
filename = 	'h1_V1_9_n1500_M80_AE_Signal_20160928_144737.txt'
h1 = np.loadtxt(filename)

# filename = 	'ok_v3_n1500_m80.txt'
# xrawok = np.loadtxt(filename)

# filename = 	'h1.txt'
# h1 = np.loadtxt(filename)

# filename = 	'h1ok.txt'
# h1ok = np.loadtxt(filename)

x = h1


fs = 1000000.0
dt = 1/fs
n = len(x)
t = np.array([i*dt for i in range(n)])

#++++++++++++++++++++++++++++ENVELOPES AND MEAN




# h2 = sifting_iteration(t, x)
# np.savetxt('h2.txt', h2)
# h1 = sifting(t, x)
# print(extrema(h1)-extrema(x))
# print(xzeros(h1)-xzeros(x))

# h11 = sifting(t, h1)
# print(extrema(h11)-extrema(h1))
# print(xzeros(h11)-xzeros(h1))

# h12 = sifting(t, h11)
# print(extrema(h12)-extrema(h11))
# print(xzeros(h12)-xzeros(h11))

# h13 = sifting(t, h12)
# print(extrema(h13)-extrema(h12))
# print(xzeros(h13)-xzeros(h12))

# fig, ax = plt.subplots(1, 1)
# ax.plot(t, x, color='black')
# ax.plot(t, x_up, color='red')
# ax.plot(t, x_down, color='green')
# ax.plot(t, x_mean, '-')
# plt.show()
# fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
# ax.plot(t, x)
# ax[1].plot(t, h2)
plt.show()

from scipy.signal import hilbert

fs = 1000000.

hx = hilbert(h1)
pha = np.angle(hx)
pha = np.unwrap(pha)
pha = np.array([pha[i+1] - pha[i] for i in range(len(pha)-1)])
pha = pha / dt
pha = pha / (2*np.pi)

amp = np.absolute(hx)

fig1, ax = plt.subplots(nrows=3, ncols=1, sharex=True)
ax[0].plot(pha)
ax[1].plot(amp)
ax[2].plot(h1)



# fig2, ax = plt.subplots(nrows=2, ncols=2, sharex=True)
# fft_amp, f, df = mag_fft(amp, fs)
# fft_h1, f, df = mag_fft(h1, fs)

# ax[0][0].plot(h1)
# ax[0][1].plot(amp)
# ax[1][0].plot(fft_h1)
# ax[1][1].plot(fft_amp)



fig3, ax = plt.subplots(nrows=2, ncols=2)
fourier_h1 = np.fft.fft(h1)
fourier_amp = np.fft.fft(amp)

# autocorr_amp_def = np.correlate(amp, amp, mode='same')
# autocorr_h1 = np.real(np.fft.ifft(fourier_h1*np.conjugate(fourier_h1)))
autocorr_amp = np.real(np.fft.ifft(fourier_amp*np.conjugate(fourier_amp)))
fft_autocorr_amp, f, df = mag_fft(autocorr_amp, fs)

print(len(autocorr_amp))
print(len(h1))
# print(len(autocorr_def))
# np.interp(np.linspace(0, len(autocorr_amp)-1, len(autocorr_amp)/2), [i for i in range(len(autocorr_amp))], autocorr_amp)

ax[0][0].plot(amp)
ax[0][1].plot(amp)
ax[1][0].plot(autocorr_amp[0:len(autocorr_amp)/2])
ax[1][1].plot(fft_autocorr_amp)




# hx = hilbert(h1ok)
# pha = np.angle(hx)
# pha = np.unwrap(pha)
# pha = np.array([pha[i+1] - pha[i] for i in range(len(pha)-1)])
# pha = pha / dt

# amp = np.absolute(hx)

# fig2, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
# ax[0].plot(pha)
# ax[1].plot(amp)




plt.show()


#++++++++++++++++++++++++++++++++COMMENTS

