import numpy as np
import matplotlib.pyplot as plt

#__Parametros__##########################
#Nº de muestras 
N = 8      
#########################################

#__Ejes__################################
fstep = 1/N                             #
                                        #
def flim(S):                            #
    return int(S/2)*fstep               #
def tlim(S):                            #
    return int(S/2)                     #
                                        #
t = np.linspace(-tlim(N), tlim(N-1), N) #
f = np.linspace(-flim(N), flim(N-1), N) #
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
f0 = 15/8                               #
a0 = 1                                  #
                                        #
Seno = a0 * np.sin(2*np.pi*f0*t)        #
#########################################

#__Unos__###############################
#Ancho de los unos
ancho = 5
                                        #
Unos = [1]*ancho                        #
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
Fun = Unos 
fig, ax = plt.subplots(2)               #
ax[0].plot(t, Fun, '.-')                #
ax[1].plot(f, F(Fun), '.-')             #
ax[0].set_xlabel('Tiempo')
ax[0].set_ylabel('Amplitud')
ax[1].set_xlabel('Frecuencia')
ax[1].set_ylabel('Amplitud')
axLabels = np.linspace(-0.5, 0.5, N)
ax[1].xaxis.set_ticks(axLabels)
ax[1].tick_params(labelrotation=45,axis='x')
ax[1].grid()
plt.xlim(-0.5,0.5)
plt.tight_layout()
plt.show()                              #
#########################################
