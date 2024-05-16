import requests
import json
import datetime

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

def Graficas():
 print("mxk")

def Borrar():
 print("mxk")
