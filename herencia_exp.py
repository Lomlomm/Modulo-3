'''
Existe una clase padre que pasa todas sus propiedades a una clase hijo (atributos y métodos) 
'''

class Automovil: 
    def __init__(self, num_puertas, num_llantas, acelaracion) -> None:
        self.num_puertas =  num_puertas
        self.num_llantas = num_llantas
        self.aceleracion = acelaracion 
    def avanzar(self): 
        if carro1.__class__.__name__ == 'Carro':
            print("El carro está avanzando")
        else: 
            print("El automovil está avanzando")

    def frenar(self): 
        print("El automovil está frenando")
    def acelerar(self): 
        print("El automovil está acelerando")

class Carro(Automovil):
    def __init__(self, num_puertas, num_llantas, acelaracion, cilindros, marca, modelo, asientos) -> None:
        super().__init__(num_puertas, num_llantas, acelaracion)
        self.cilindros = cilindros
        self.marca = marca
        self.modelo = modelo
        self.asientos = asientos
         
    def radio(self): 
        print("Se está reproduciendo la radio")

class Moto: 
    pass

class Bici: 
    pass

class Camioneta: 
    pass 


carro1 = Carro(4, 4, 300, 6, 'Honda', '2001', 3)
carro1.avanzar()
print(f"El carro tiene un total de {carro1.asientos} asientos")
carro1.radio()