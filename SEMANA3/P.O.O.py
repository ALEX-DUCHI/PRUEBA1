class ClimaSemanal:
    def __init__(self):
        self._temperaturas = []
        self._dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def ingresar_datos(self):
        """Método para ingresar las temperaturas diarias."""
        print("Ingrese las temperaturas de la semana:")
        for dia in self._dias:
            while True:
                try:
                    temp = float(input(f"{dia}: "))
                    self._temperaturas.append(temp)
                    break
                except ValueError:
                    print("⚠️ Valor inválido. Intente nuevamente.")

    def calcular_promedio(self):
        """Calcula y devuelve el promedio semanal."""
        if not self._temperaturas:
            raise ValueError("No hay datos de temperatura ingresados.")
        return sum(self._temperaturas) / len(self._temperaturas)

    def mostrar_promedio(self):
        """Muestra el resultado."""
        promedio = self.calcular_promedio()
        print(f"\n🌤 Promedio semanal de temperatura: {promedio:.2f}°C")

# Ejecución del programa
if __name__ == "__main__":
    print("=== Programa POO: Promedio semanal del clima ===")
    clima = ClimaSemanal()
    clima.ingresar_datos()
    clima.mostrar_promedio()
