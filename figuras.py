class Figura():
    def __init__(self):
        pass
    def calcular_area(self):
        pass
    def calcular_perim(self):
        pass
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado*2
	def calcular_perim(self):
		return self.lado*4
        

cuadrado = Cuadrado(4)
print(cuadrado.calcular_area())
print(cuadrado.calcular_perim())