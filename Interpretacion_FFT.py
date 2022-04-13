import numpy as np
import matplotlib.pyplot as plt

#__Parametros__##########################
#Nº de muestras por periodo 
N = 1024      
#Periodo de la señal       
T = 15  
#########################################

#__Ejes__################################
tstep = T/N                             #
fstep = 1/T                             #
                                        #
def flim(S):                            #
    return int(S/2)*fstep               #
def tlim(S):                            #
    return int(S/2)*tstep               #
                                        #
t = np.linspace(-tlim(N), tlim(N-1), N) #
f = np.linspace(-flim(N), flim(N-1), N) #
#########################################

#__Cajon__###############################
#Ancho del Cajon
ancho = 5

u = lambda x: np.piecewise(x,x>=0,[1,0])#
u0 = u(t+(ancho/2))                     #
u1 = u(((ancho-1)/2)-t)                 #
                                        #
Cajon = u0*u1/ancho                     #
#########################################

#__Seno__################################
f0 = 1/T                                #
a0 = 1                                  #
                                        #
Seno = a0 * np.sin(2*np.pi*f0*t)        #
#########################################

#__fft__#################################
def F(fun_t):                           #
    fftR = 2*abs(np.fft.fft(fun_t))/N   #
    fft0 = fftR[int((N+1)/2):]          #
    fft1 = fftR[:int((N+1)/2)]          #
    return np.concatenate((fft0,fft1))  #
#########################################

#__Ploteo__##############################
#Funcion a plotear
Fun = Cajon 
fig, ax = plt.subplots(2)               #
ax[0].plot(t, Fun, '.-')                #
ax[1].plot(f, F(Fun), '.-')             #
plt.show()                              #
#########################################
