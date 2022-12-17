import herencia as h
import os

tutores = open("modulo-3/archivos_txt/tutores.txt", "a") #w
estudiantes = open("modulo-3/archivos_txt/estudiantes.txt", "a") #w
try: 
    os.mkdir("modulo-3/Carpeta Nueva")
except: 
    print("La carperta ya existe")
    
for tutor in h.total_tutores: 
    tutores.write("{ \n")
    for elemento in tutor: 
        tutores.write(f"    {str(elemento)} : {str(tutor[elemento])} \n")
    tutores.write("} \n")



for estudiante in h.total_estudiantes: 
    estudiantes.write("{ \n")
    for elemento in estudiante: 
        estudiantes.write(f"    {str(elemento)} : {str(estudiante[elemento])} \n")
    estudiantes.write("} \n")

tutores.close()
estudiantes.close()

tutores = open("modulo-3/archivos_txt/tutores.txt", "r") #w
estudiantes = open("modulo-3/archivos_txt/estudiantes.txt", "r") #w

#readline() - sólo regresa una linea
#readlines() - regresa una lista con las lineas de mi archivo
for linea in tutores.readlines(): 
    print(linea)
for linea in estudiantes.readlines(): 
    print(linea)

