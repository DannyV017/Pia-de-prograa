import modulo2
def Menu_interno():
  while True:
   try:
    opcion_Interna = int(input("\nMENU\n1-Casos de covid\n2-Muertes\n3-Personas vacunadas\nElige una opción: "))
    if opcion_Interna>=1 and opcion_Interna<=3:
     return opcion_Interna
   except ValueError:
    print("\nINGRESA UNA OPCION VALIDA\n")
def Menu_Principal():
 while True:
   try:
    opcion = int(input("\nMENU PRINCIPAL\n1-Consulta web\n2-Consulta de registros\n3-Estadisticas\n4-Graficas\n5-Borrar de todo\nElige una opcion: "))
    if opcion>=1 and opcion<=5:
     return opcion
   except ValueError or (opcion>=1 and opcion<=5):
    print("\nINGRESA UNA OPCION VALIDA")
 
def main():
  while True:
       opcion = Menu_Principal()
       opcion_interna = Menu_interno()
####################################################################################################################### 
       if opcion == 1:                         ###CONSULTA WEB###
         if opcion_interna==1:
           selector_General = 'cases'
           print ("\nConsulta web: Casos de covid\n")
           modulo2.consulta_web(selector_General)
         elif opcion_interna==2:
           selector_General= 'deaths'
           print("\nConsulta web: Muertes\n")
           modulo2.consulta_web(selector_General)
         elif opcion_interna==3:
           selector_General='recovered'
           print("\nConsulta Web: Personas vacunadas\n")
           modulo2.consulta_web(selector_General)
#######################################################################################################################
       elif opcion == 2:                        ###CONSULTA DE REGISTROS###
          if opcion_interna==1:
           selector_General='cases'
           print ("\nConsulta De Registros: Casos de covid")
           modulo2.consulta_Registros(selector_General)
          elif opcion_interna==2:
           selector_General='deaths'
           print("\nConsulta De Registros: Muertes")
           modulo2.consulta_Registros(selector_General)
          elif opcion_interna==3:
           modulo2.consulta_Registros(selector_General)
           print("\nConsulta De Registros: Personas vacunadas")
#######################################################################################################################
       elif opcion == 3:                        ###ESTADISTICAS###
          if opcion_interna==1:
           print ("\nEstadisticas: Casos de covid")
          elif opcion_interna==2:
           print("\nEstadisticas: Muertes")
          elif opcion_interna==3:
           print("\nEstadisticas: Personas vacunadas")
#######################################################################################################################
                            ###GRAFICAS###
       elif opcion == 4:  # GRAFICAS
            if opcion_interna==1:
                  selector_General='cases'
                  print("\nGraficas: Casos de COVID-19")
                  pais_buscado = input("Ingrese el país que quiera graficar: ")
                  modulo2.graficar_casos(pais_buscado, selector_General)
            elif opcion_interna==2:
                  selector_General= 'deaths'
                  selector_General = 'deaths'
                  print("\nGraficas: Muertes por COVID-19")
                  pais_buscado = input("Ingrese el país que quiera graficar: ")
                  modulo2.graficar_casos(pais_buscado, selector_General)
            elif opcion_interna==3:
                  selector_General = 'recovered'
                  print("\nGraficas: Personas recuperadas de COVID-19")
                  pais_buscado = input("Ingrese el país que quiera graficar: ")
                  modulo2.graficar_casos(pais_buscado, selector_General)
#######################################################################################################################
       elif opcion == 5:                        ###BORRAR###
          if opcion_interna==1: 
           print ("\nGraficas: Casos de covid")
          elif opcion_interna==2:
           print("\nGraficas: Muertes")
          elif opcion_interna==3:
           print("\nGraficas: Personas vacunadas")
#######################################################################################################################
       else:    
            print("\nOpcion Invalida\n")
     

if __name__ == '__main__':
    main()