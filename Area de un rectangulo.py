# Se establece la Clase Rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        # Constructor que inicializa la base y altura
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Realiza el calculo para saber el área del rectángulo
        return self.base * self.altura

# Programa principal
def main():
    print("=============================")
    print("CÁLCULO DE ÁREA UN RECTÁNGULO")
    print("=============================")
    # Entrada de los datos
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))
    # Crear objeto y mostrar el área
    rectangulo = Rectangulo(base, altura)
    print("El área del rectángulo es:", rectangulo.calcular_area(), "unidades cuadradas")

main()
