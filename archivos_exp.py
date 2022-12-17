import os 

#file = open('leyendo.txt', 'r')

#os.mkdir('modulo-3/archivos_txt') #crea una carpeta 
try: #intenta ejecutar un codigo 
    os.remove('escribiendo.txt')
    os.remove('escribiendo2.txt')
except: #Manda error si no puede ejecutarlo
    print("Los archivos no existen")
else: # Ejecuta un código en caso de que se pudiera hacer el try
    print("Se eliminó correctamente") 

finally: # Siempre se va a ejecutar 
    #Creamos arichivo
    file = open('modulo-3/archivos_txt/escribiendo2.txt', 'w')
    file.write("Adios \n")
    file.write("Hola \n")
    file.write("Como estas \n")
    
    file.close() #Cierra el archivo, para después no tener problemas para su uso 

    file1 = open('modulo-3/archivos_txt/escribiendo.txt', 'a')
    file1.write("Adios")

    file2 = open('modulo-3/archivos_txt/escribiendo2.txt', 'r')
    #El siguiente for imprime todas las lineas de nuestro archivo 
    for linea in file2.readlines(): 
        print(linea)