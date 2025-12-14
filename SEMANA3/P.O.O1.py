# Programa: Promedio Semanal del Clima (Versión POO)
# Autor: Estudiante de programación
# Propósito: Calcular el promedio semanal de temperaturas usando clases y métodos
# Paradigma: Programación Orientada a Objetos

class DiaClima:
    """
    Representa la información climática de un día.
    Usa encapsulamiento para proteger el atributo de temperatura.
    """
    def __init__(self, nombre, temperatura=0.0):
        self.__nombre = nombre
        self.__temperatura = temperatura

    @property
    def nombre(self):
        return self.__nombre

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if isinstance(valor, (int, float)):
            self.__temperatura = valor
        else:
            raise ValueError("La temperatura debe ser un número.")


class SemanaClima:
    """
    Contiene la información climática de toda una semana.
    Aplica principios de POO: composición (objetos DiaClima dentro de SemanaClima).
    """
    def __init__(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.__dias_clima = [DiaClima(dia) for dia in dias]

    def ingresar_datos(self):
        """
        Permite al usuario ingresar las temperaturas diarias.
        """
        print("Ingrese las temperaturas diarias en °C:")
        for dia in self.__dias_clima:
            while True:
                try:
                    temp = float(input(f"{dia.nombre}: "))
                    dia.temperatura = temp
                    break
                except ValueError:
                    print(" Valor inválido. Intente nuevamente.")

    def calcular_promedio(self):
        """
        Calcula el promedio semanal de temperatura.
        """
        total = sum(dia.temperatura for dia in self.__dias_clima)
        return total / len(self.__dias_clima)

    def mostrar_resultado(self):
        """
        Muestra el resultado final.
        """
        promedio = self.calcular_promedio()
        print(f"\n El promedio semanal de temperatura es: {promedio:.2f} °C")


# --- Ejecución principal ---
def main():
    print("=== Promedio Semanal del Clima (POO) ===")
    semana = SemanaClima()
    semana.ingresar_datos()
    semana.mostrar_resultado()


if __name__ == "__main__":
    main()
