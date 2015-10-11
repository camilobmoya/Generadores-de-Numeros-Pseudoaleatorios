# -*- coding: utf-8 -*-
"""@author: CBM"""


def generar_num_pseudoaleatorios(n, x0, a, b, m):
    """Retorna una secuencia de n números pseudoaleatorios.
    
    A partir de cualquiera de los generadores midsquare, congruencial multiplicativo o mixto.
    x0 es el valor para la semilla, a, b y m los parámetros para los congruenciales.
    """
    secuencia = []
    if n==0:
        print 'generar_num_pseudoaleatorio_Error: Ingrese una cantidad n válida.'
    
    elif a==0 and b==0 and m!=0:
        print 'generar_num_pseudoaleatorio_Error: Ingrese un multiplicador a válido.'
        
    elif a==0 and b!=0 and m!=0:
        print 'generar_num_pseudoaleatorio_Error: Ingrese un multiplicador a válido.'

    elif a!=0 and b==0 and m==0:
        print 'generar_num_pseudoaleatorio_Error: Ingrese un módulo m válido.'

    elif a!=0 and b!=0 and m==0:
        print 'generar_num_pseudoaleatorio_Error: Ingrese un módulo m válido.'

    elif a==0 and b!=0 and m==0:
        print 'generar_num_pseudoaleatorio_Error: Ingrese un multiplicador a válido.'
        print 'generar_num_pseudoaleatorio_Error: Ingrese un módulo m válido.'   

    elif a==0 and b==0 and m==0: #Generador MidSquare.
        longitud_x0 = len(str(x0))
        
        if longitud_x0 %2 == 0:
            for i in range(0,n):
                numCuadrado = str(x0**2)
                if len(numCuadrado) < 2*longitud_x0:
                    cantidadDeCerosPorAgregar = 2*longitud_x0 - len(numCuadrado)
                    cadenaDeCeros = "" 
                    for ii in range(0,cantidadDeCerosPorAgregar):
                        cadenaDeCeros = '0' + cadenaDeCeros
                        numCuadrado = cadenaDeCeros + numCuadrado
                #print "Numero cuadrado" + str(i) + " = " + numCuadrado
                xi = numCuadrado[ int (0.5*longitud_x0) : int (0.5*longitud_x0 + longitud_x0) ]
                #print "X" + str(i) + " = " + xi
                ui = '0.'+ xi
                secuencia.append(ui)
                #print "U" + str(i) + " = " + ui
                x0 = int(xi)
            return secuencia

        else: 
            print 'MidSquareError: Debe ingresar un valor de semilla con un numero de cifras PAR. \n'
    
    else: #Generador Congruencial.
       for i in range(0,n):
            xi = (a*x0 + b) % m
            ui = xi/float(m)
            secuencia.append(ui)
            x0 = xi
       return secuencia
        