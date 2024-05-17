import requests
import json
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, MonthLocator
from datetime import datetime


base_url = "https://disease.sh/v3/covid-19/historical" #API API API API API API API API API API API API API API API API
def consulta_web(selector):
  pais=str(input("¿Que pais deseas consultar?: "))
  url = f"{base_url}/{pais}?lastdays=all&start_date=&end_date="
  respuesta= requests.get(url)
  datos= respuesta.json()
  if respuesta.status_code==200:
    print(datos["timeline"][selector])
  else:
    print("\nError al obtener los datos:", respuesta.status_code)

def consulta_Registros(selector):
   with open('ALL_DATA.json', 'r') as archivo:
    datos = json.load(archivo)
    registro_buscado= input("Ingrese el pais que quiera consultar: ")
    
   for pais in datos:
     if pais['country'] == registro_buscado:
        casos = pais['timeline'][selector]
        print(f"",selector,"en : ",registro_buscado)
        nombre_archivo = f"store_data_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(nombre_archivo, 'a') as archivo2:
             archivo2.write(f"PAIS: {registro_buscado}, SECCION: {selector}\n\n")
        for fecha, casos in casos.items():
            print(f"Fecha: {fecha}, Casos: {casos}")
            with open(nombre_archivo, 'a') as archivo2:
             archivo2.write(f"Fecha: {fecha}, Casos: {casos}\n")
        break
       
   
   
   #with open("archivo.txt", "w") as archivo:
    
      ##archivo.write("Hola, mundo!\n")


def Estadisticas():
 print("mxk")
 
def graficar_casos(registro_buscado, selector):
    with open('ALL_DATA.json', 'r') as archivo:
        datos = json.load(archivo)

        for pais in datos:
            if pais['country'] == registro_buscado:
                casos = pais['timeline'][selector]
                fechas = list(casos.keys())
                cantidad_casos = list(casos.values())

                fechas_datetime = [datetime.strptime(fecha, '%m/%d/%y') for fecha in fechas]

                plt.figure(figsize=(10, 6))
                plt.plot(fechas_datetime, cantidad_casos, marker='o', linestyle='-')
                plt.title(f'Cantidad de {selector} en {registro_buscado}')
                plt.xlabel('Fecha')
                plt.ylabel(f'{selector.capitalize()}')
                plt.xticks(rotation=45)
                plt.grid(True)
                
                # Formato de las fechas en el eje x
                plt.gca().xaxis.set_major_formatter(DateFormatter('%b %Y'))  # Formato mes/ año
                
                # Establecer el rango del eje x desde enero de 2020 hasta enero de 2024
                fecha_inicio = datetime(2020, 1, 1)
                fecha_fin = datetime(2024, 1, 1)
                plt.xlim(fecha_inicio, fecha_fin)
                
                # Formato de los números en el eje Y como enteros
                plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))
                
                plt.tight_layout()
                plt.show()
                break
        else:
            print("No se encontraron datos para el país especificado.")
            
            
def Borrar():
 print("mxk")
