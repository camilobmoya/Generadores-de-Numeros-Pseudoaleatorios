import sys
while True:
        opcion = input("\nMENU: \n1. Para generar numeros pseudoaleatorios. \n2. Para SALIR.\n")
        if opcion == 1:
                print '\n********************GENERADOR MIDSQUARE********************'
                x0 = input("\nIngrese el valor semilla del generador:  ")
                longitud_x0 = len(str(x0))

                if longitud_x0 %2 == 0:
                        cantidad = input("Ingrese la cantidad de numeros aleatorios a generar: ")
                        print "\n"
                        for i in range(0,cantidad):
                                numCuadrado = str(x0*x0)
                                if len(numCuadrado)< 2*longitud_x0:
                                        cantidadDeCerosPorAgregar = 2*longitud_x0 - len(numCuadrado)
                                        cadenaDeCeros = "" 
                                        for ii in range(0,cantidadDeCerosPorAgregar):
                                                cadenaDeCeros = '0' + cadenaDeCeros
                                        numCuadrado = cadenaDeCeros + numCuadrado
                                #print "Numero cuadrado" + str(i) + " = " + numCuadrado
                                xi = numCuadrado[ int (0.5*longitud_x0) : int (0.5*longitud_x0 + longitud_x0) ]
                                #print "X" + str(i) + " = " + xi
                                ui = '0.'+ xi
                                print "U" + str(i) + " = " + ui
                                x0 = int(xi)

                else: 
                        print 'Error: Debe ingresar un valor de semilla con un numero de cifras PAR. \n'

        elif opcion == 2:
                sys.exit()

        else:
                print 'Elija una opcion valida.\n'

	
	
	


