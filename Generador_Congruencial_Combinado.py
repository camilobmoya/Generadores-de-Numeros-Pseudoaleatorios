import sys
while True:
        opcion = input("\nMENU: \n1. Para generar numeros pseudoaleatorios. \n2. Para SALIR.\n")
        if opcion == 1:
                print '\n******************GENERADOR CONGRUENCIAL COMBINADO******************'
                x0 = input("\n\nIngrese el valor semilla para el primer generador Xi = 171*Xi-1 MOD 30269\n  X0 = ")
                y0 = input("\n\nIngrese el valor semilla para el segundo generador Yi = 172*Xi-1 MOD 30307\n  Y0 = ")
                z0 = input("\n\nIngrese el valor semilla para el tercer generador Zi = 170*Xi-1 MOD 30323\n  Z0 = ")
                cantidad = input("\nIngrese la cantidad de numeros aleatorios a generar: ")
                print "\n"
                for i in range(0,cantidad):
                    xi = (171*x0)%30269
                    #print "X" + str(i) + " = " + str(xi)
                    yi = (172*y0)%30307
                    #print "Y" + str(i) + " = " + str(yi)
                    zi = (170*z0)%30323
                    #print "Z" + str(i) + " = " + str(zi)
                    ui = (xi/30269.0 + yi/30307.0 + zi/30323.0)%1 
                    print "U" + str(i) + " = " + str(ui)
                    x0 = xi
                    y0 = yi
                    z0 = zi

        elif opcion == 2:
                sys.exit()

        else:
                print 'Elija una opcion valida.\n'

