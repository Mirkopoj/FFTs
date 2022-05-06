import numpy as np
import matplotlib.pyplot as plt

#__Parametros__##########################
#Nº de muestras de tiempo
N = 7
#Nº de muestras de frecuencia
M = 9
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
c = np.linspace(-1, 1, 200*R)
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
    fftR = abs(np.fft.fft(fun_t,n=M))   #
    return np.concatenate((fftR,fftR))  #
#########################################

#__Tren_de_deltas__######################
d = lambda z: np.piecewise(z,
                        abs(z%1)<=0.001,
                        [1,0])          #
                                        #
Del = (N-1)*d(c)                        #
DelCos = d(c+f1)+d(c-f1)                #
#########################################

#__SINC__################################
SINC = lambda w: np.sin(np.pi*N*w)/np.sin(np.pi*w)  
#########################################

#__TFCajon__#############################
FC = SINC(c)
#########################################

#__TFCos*Cajon__#########################
COSSINCS = 0
for i in range(2):
    COSSINCS += SINC(c-((5/31)+i*(21/31))) 
COSSINCS /= 2
#########################################

#__Ploteo__##############################
#Funcion a plotear
Fun = Unos
fig, ax = plt.subplots(2)               #
ax[0].plot(t, Fun, 'bo')                #
ax[1].plot(f, F(Fun), 'ro')             #
ax[1].plot(c, Del, 'b-')                #
ax[1].plot(c, abs(FC), 'g-')            #
ax[0].set_xlabel(
    'Muestras (en el tiempo)')          #
ax[0].set_ylabel('Amplitud')            #
ax[1].set_xlabel('Frecuencia')          #
ax[1].set_ylabel('Amplitud')            #
#axLabels = np.linspace(-1, 1, 64+1)    #
axLabels = np.linspace(-1, 1, 2*M+1)    #
ax[1].xaxis.set_ticks(axLabels)         #
ax[0].grid()                            #
ax[1].grid()                           #
plt.xticks(rotation=90)                 #
plt.xlim(-1,1)                          #
plt.tight_layout()                      #
plt.show()                              #
#########################################

