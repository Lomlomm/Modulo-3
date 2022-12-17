'''
Ejercicio: Crear una clase padre llamada 'Persona' con los atributos nombre, apellido y edad 
De la clase persona, crear dos clases hijas llamadas 'Tutor' y 'Estudiante'
La clase tutor deberá tener dos atributos propios que serán 'nombre_hijo', 'ocupacion'
La clase estudiante deberá tener los siguientes atributos añadidos: 
-nombre del padre
-calificacion 
-grupo
-faltas
-aprobo 
y los siguientes métodos: 
- aprobatorio_cal - va a asignar true a aprobo si su calificacion es mayor o igual a 6
- aprobatorio_faltas - va a asignar false a aprobo si sus faltas son mayores a 10
'''


class Persona: 
    def __init__(self, nombre, apellido, edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Tutor(Persona): 
    def __init__(self, nombre, apellido, edad, nombre_hijo, ocupacion) -> None:
        super().__init__(nombre, apellido, edad)
        self.hijo = nombre_hijo
        self.ocupacion = ocupacion
    
class Estudiante(Persona): 
    def __init__(self, nombre, apellido, edad, tutor, calificacion, grupo, faltas) -> None:
        super().__init__(nombre, apellido, edad)
        self.tutor = tutor.__dict__
        self.calificacion = calificacion 
        self.grupo = grupo
        self.faltas = faltas
        self.aprobo = False

    def aprobatorio_cal(self):
        if self.calificacion >= 6: 
            self.aprobo = True
        else: 
            self.aprobo = False
    
    def aprobatorio_faltas(self): 
        if self.faltas > 10: 
            self.aprobo = False


tutor1 = Tutor('Enrique', 'Arellano', 57, 'Vanessa', 'Telefonista')
estudiante1 = Estudiante('Vanessa', 'Arellano', 21, tutor1, 10, 'B', 11)
estudiante1.aprobatorio_cal()
estudiante1.aprobatorio_faltas()


tutor2 = Tutor('Marissa', 'Serna', 55, 'Daniel', 'Escritora')
estudiante2 = Estudiante('Daniel', 'Arellano', 21, tutor1, 10, 'A', 2)
estudiante2.aprobatorio_cal()
estudiante2.aprobatorio_faltas()

total_tutores = []
total_estudiantes = []

total_tutores.append(tutor1.__dict__)
total_tutores.append(tutor2.__dict__)
total_estudiantes.append(estudiante1.__dict__)
total_estudiantes.append(estudiante2.__dict__)

print(total_estudiantes)