import sys
while True:
        opcion = input("\nMENU: \n1. Para generar numeros pseudoaleatorios. \n2. Para SALIR.\n")
        if opcion == 1:
                print '\n********************GENERADOR CONGRUENCIAL MIXTO********************'
                x0 = input("\n\nIngrese el valor semilla para el generador Xn = 5*Xn-1 + 3 MOD 16\n  X0 =   ")
                cantidad = input("Ingrese la cantidad de numeros aleatorios a generar: ")
                print "\n"
                for i in range(0,cantidad):
                    xi = (5*x0 + 3)%16
                    #print "X" + str(i) + " = " + str(xi)
                    ui = xi / 16.0
                    print "U" + str(i) + " = " + str(ui)
                    x0 = xi

        elif opcion == 2:
                sys.exit()

        else:
                print 'Elija una opcion valida.\n'
