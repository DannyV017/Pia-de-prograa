

def Menu_interno():
 while True:
  opcion_Interna = int(input("\nMENU\n1-Casos de covid\n2-Muertes\n3-Personas vacunadas\nElige una opción: "))
  if opcion_Interna>=1 and opcion_Interna<=3:
   return opcion_Interna
  else:
   print("Ingresa opcion valida")
def main():
    while True:
        opcion = input("\nMENU PRINCIPAL\n1-Consulta web\n2-Consulta de registros\n3-Estadisticas\n4-Graficas\n5-Borrar de todo\nElige una opcion: ")
        if opcion == "1":                         ###CONSULTA WEB###
         opcion_interna = Menu_interno()
         if opcion_interna==1:
           print ("Consulta web: Casos de covid")
         elif opcion_interna==2:
           print("Consulta web: Muertes")
         elif opcion_interna==3:
           print("Consulta Web: Personas vacunadas")
        elif opcion == "2":                        ###CONSULTA DE REGISTROS###
          if opcion_interna==1:
           print ("Consulta De Registros: Casos de covid")
          elif opcion_interna==2:
           print("Consulta De Registros: Muertes")
          elif opcion_interna==3:
           print("Consulta De Registros: Personas vacunadas")
        elif opcion == "3":                        ###ESTADISTICAS###
          if opcion_interna==1:
           print ("Estadisticas: Casos de covid")
          elif opcion_interna==2:
           print("Estadisticas: Muertes")
          elif opcion_interna==3:
           print("Estadisticas: Personas vacunadas")
        elif opcion == "4":                        ###GRAFICAS###
          if opcion_interna==1:
           print ("Graficas: Casos de covid")
          elif opcion_interna==2:
           print("Graficas: Muertes")
          elif opcion_interna==3:
           print("Graficas: Personas vacunadas")
        elif opcion == "5":                        ###BORRAR###
          if opcion_interna==1: 
           print ("Graficas: Casos de covid")
          elif opcion_interna==2:
           print("Graficas: Muertes")
          elif opcion_interna==3:
           print("Graficas: Personas vacunadas")
        else:
            print("\nOpcion Invalida\n")
if __name__ == '__main__':
    main()