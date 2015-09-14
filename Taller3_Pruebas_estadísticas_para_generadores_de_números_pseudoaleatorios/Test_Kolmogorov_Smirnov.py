# -*- coding: utf-8 -*-
"""@author: ELUX."""

import numpy as np
import matplotlib.pyplot as plt


def randuX(n):
    """Retorna una lista que contiene n valores aproximados a una distribución uniforme U(0,1).
    
    Esto a partir de un GENERADOR CONGRUENCIAL MIXTO... Xn = (170*Xn-1 + 1) mod 30323.
    """
    x0 = 7          #Este es el valor semilla elegido.
    valores = []
    for i in range(0,n):
        xi = (170*x0 + 1)%30323
        ui = xi/30323.0
        valores.append(ui)
        x0 = xi
    return valores
    
    
    
def test_de_kolmogorov_smirnov(secuencia=[]):
    """Imprime el resultado de aplicar el Test K-S sobre una secuencia de valores U[0,1]."""    
    N = len(secuencia)
    # Teoretical CDF for Uniform distribution F(x)
    u = [1.0] * N
    #print(u)
    
    # Plot empirical distribution f(x)
    count, bins, ignored = plt.hist(secuencia, 25, normed=True)
    plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
    plt.show()
    
    x1 = np.arange(1/float(N), 1+1/float(N) , 1/float(N))
    y1 = np.cumsum(np.sort(u)/np.max(np.cumsum(u)))
    
    x2 = np.sort(secuencia)
    y2 = np.cumsum(np.sort(secuencia)/np.max(np.cumsum(secuencia)))
    
    De=np.absolute(y2-y1)
    print("De = ",np.max(De))
    
    # Plotting
    plt.plot(x1,y1,label='Uniform')
    plt.step(x2,y2,label='Random')
    x3 = [x1[De.argmax()],x1[De.argmax()]]
    y3 = [np.min([y1[De.argmax()],y2[De.argmax()]]),np.max([y1[De.argmax()],y2[De.argmax()]])]
    plt.step(x3,y3,label='D')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Cumulative Probability P(X)')
    plt.ylim(0, 1.05)
    plt.show()
    
    # scipy function for K-S test
    from scipy import stats
    D,pvalue = stats.kstest(y2, 'uniform')
    print("D = ", D)
    print("p-value = ", pvalue)
    
    
    
def test_de_kolmogorov_smirnov_dos():
    """Imprime el resultado de aplicar el Test K-S sobre una secuencia de valores U[0,1].
    
       Generados aleatoriamente a partir de la librería numpy. 
    """ 
    N = 100
    # Teoretical CDF for Uniform distribution F(x)
    u = [1.0] * N
    #print(u)
    
    # Generate random numbers with Uniform distribution f(x)
    #np.random.seed(123456789)
    x = np.random.uniform(0,1,N)
    
    # Plot empirical distribution f(x)
    count, bins, ignored = plt.hist(x, 25, normed=True)
    plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
    plt.show()
    
    x1 = np.arange(1/float(N), 1+1/float(N) , 1/float(N))
    y1 = np.cumsum(np.sort(u)/np.max(np.cumsum(u)))
    
    x2 = np.sort(x)
    y2 = np.cumsum(np.sort(x)/np.max(np.cumsum(x)))
    
    De=np.absolute(y2-y1)
    #print(D)
    print("De = ",np.max(De))
    
    # Plotting
    plt.plot(x1,y1,label='Uniform')
    plt.step(x2,y2,label='Random')
    x3 = [x1[De.argmax()],x1[De.argmax()]]
    y3 = [np.min([y1[De.argmax()],y2[De.argmax()]]),np.max([y1[De.argmax()],y2[De.argmax()]])]
    plt.step(x3,y3,label='D')
    
    #plt.plot(x1,De,label='De')
    
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Cumulative Probability P(X)')
    #plt.title('arbitrary')
    #plt.xscale('log')
    #plt.yscale('log')
    
    #plt.xlim(0, np.max([np.max(whitney),np.max(redwell)])+0.05)
    plt.ylim(0, 1.05)
    plt.show()
    
    # scipy function for K-S test
    from scipy import stats
    D,pvalue = stats.kstest(y2, 'uniform')
    print("D = ", D)
    print("p-value = ", pvalue)
    
    

    
    