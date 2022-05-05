import numpy as np
import matplotlib.pyplot as plt

#__Parametros__##########################
#Nº de muestras de tiempo
N = 9      
#Nº de muestras de frecuencia
M = N 
#########################################

#__Ejes__################################
fstep = 1/M                             #
R = 2*M #rango                          #
                                        #
def flim(S):                            #
    return int(S/2)*fstep               #
def tlim(S):                            #
    return int(S/2)                     #
                                        #
t = np.linspace(-tlim(N), tlim(N-1), N) #
f = np.linspace(-flim(R), flim(R-1), R) #
c = np.linspace(-1, 1, 100*R)
#########################################

#__Cajon__###############################
#Ancho del Cajon
ancho = 5

u = lambda x: np.piecewise(x,x>=0,[1,0])#
u0 = u(t+int(ancho/2))                  #
u1 = u((int(ancho-1)/2)-t)              #
                                        #
Cajon = u0*u1/ancho                     #
#########################################

#__Seno__################################
f0 = 5/31                               
a0 = 1                                  
                                        #
Seno = a0 * np.sin(2*np.pi*f0*t)        #
#########################################

#__Coseno__##############################
f1 = 5/31                               
a1 = 1                                  
                                        #
Coseno = a1 * np.cos(2*np.pi*f1*t)      #
#########################################

#__Unos__################################
Unos = [1]*N                            #
#########################################

#__fft__#################################
def F(fun_t):                           #
    fftR = abs(np.fft.fft(fun_t,n=M))/M #
    return np.concatenate((fftR,fftR))  #
#########################################

#__Tren_de_deltas__######################
d = lambda z: np.piecewise(z,
                        abs(z%1)<=0.001,
                        [1,0])          #
                                        #
Del = d(c)                              #
DelCos = d(c+f1)+d(c-f1)                #
#########################################

#__FCajon__##############################
FC = np.sin(np.pi*N*c)/np.sin(np.pi*c)/N#
#########################################

#__Ploteo__##############################
#Funcion a plotear
Fun = Coseno
fig, ax = plt.subplots(2)               #
ax[0].plot(t, Fun, 'bo')                #
ax[1].plot(f, F(Fun), 'ro')             #
ax[1].plot(c, DelCos, '-')              #
ax[1].plot(c, FC, 'g-')                 #
ax[0].set_xlabel('Tiempo')              #
ax[0].set_ylabel('Amplitud')            #
ax[1].set_xlabel('Frecuencia')          #
ax[1].set_ylabel('Amplitud')            #
axLabels = np.linspace(-1, 1, 2*M+1)    #
ax[1].xaxis.set_ticks(axLabels)         #
ax[0].grid()                            #
ax[1].grid()                            #
plt.xticks(rotation=45)
plt.xlim(-1,1)                          #
plt.tight_layout()                      #
plt.show()                              #
#########################################
