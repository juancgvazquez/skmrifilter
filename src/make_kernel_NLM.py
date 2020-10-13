#funcion kernel 
import numpy as np

def make_kernel(f):              

"""
crea la ventana móvil local de tamaño 2f+1
"""
    kernel=np.zeros((2*f+1,2*f+1))  
    for d in range(1,f+1):    
        value= 1 / (2*d+1)**2  
        for i in range(-d,d+1):
            for j in range(-d,d+1):
                kernel[f+1-i-1,f+1-j-1]= kernel[f+1-i-1,f+1-j-1] + value 
     
    kernel = kernel / f
    return kernel
