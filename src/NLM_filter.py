#filtro NLM 
import numpy as np
import cv2
import math

def FiltroNLM(imagen,sigma):
    
#     t: radio ventana de b�squeda
#     f: radio ventana de similitud
#     h: grado de filtrado
#     LA IMAGEN QUE SE INGRESA DEBE ESTAR EN GRAYSCALE Y NORMALIZADA CON:
            #cv2.normalize(imagen.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX) 
#     Implementation of the Non local filter proposed for A. Buades, B. Coll and J.M. Morel in
#     "A non-local algorithm for image denoising"

    t = 7    #/7
    f = 9   #/5
    h = 1.5*sigma
    
    #tamaño de la imagen
    [m,n] = imagen.shape 
    
    #memoria para el output
    NLM = np.zeros((m,n))
    UNLM = np.zeros((m,n))
    
    #Replicate the boundaries of the input image
    input2 = np.pad(imagen, (f, f), 'symmetric') #para abarcar los pixeles de los bordes
    
    # Used kernel
    kernel = make_kernel(f)             
    kernel = kernel / sum(sum(kernel))  
    
    
    h=h*h
    
    for i in range(1,m+1):      #recorre todas las filas                      
        for j in range(1,n+1):      #recorre todas las columnas
            
            i1 = i+ f
            j1 = j+ f
                
            W1= input2[i1-f-1:i1+f , j1-f-1:j1+f]  

            wmax=0 
            average=0
            sweight=0
         
            rmin = max(i1-t,f+1)
            rmax = min(i1+t,m+f)
            smin = max(j1-t,f+1)
            smax = min(j1+t,n+f)
            
            for r in range(rmin,rmax+1,1):                          
                for s in range(smin,smax+1,1):                      
                                               
                    if (r==i1 and s==j1):
                        continue

                    W2= input2[r-f-1:r+f , s-f-1:s+f]                
                    d = sum(sum(kernel*(W1-W2)*(W1-W2)))
                    w = math.exp(-d/h)   
                    
                    if w>wmax:                
                        wmax=w                   

                    sweight = sweight + w
                    average = average + w*input2[r,s]
                    

            average = average + wmax*input2[i1,j1]
            sweight = sweight + wmax
            
            if sweight > 0:
                NLM[i-1,j-1] = average / sweight               
            else:
                NLM[i,j] = imagen[i,j]
                
    UNLM = np.sqrt(NLM**2 - 2*sigma*sigma).real                    
    Residuo = imagen - UNLM
    
    return NLM,UNLM,Residuo
