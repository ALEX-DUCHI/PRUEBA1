# Programa: Promedio Semanal del Clima (Versión Tradicional)
# Autor: Estudiante de programación
# Propósito: Calcular el promedio semanal de temperaturas ingresadas por el usuario
# Paradigma: Programación tradicional (funciones y estructuras básicas)

def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas de cada día de la semana.
    Retorna una lista con las temperaturas registradas.
    """
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []

    print("Ingrese las temperaturas diarias en °C:")
    for dia in dias:
        while True:
            try:
                temp = float(input(f"{dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("❌ Valor inválido. Ingrese un número válido.")
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio semanal de una lista de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


def mostrar_resultado(promedio):
    """
    Muestra el resultado formateado.
    """
    print(f"\n🌤️ El promedio semanal de temperatura es: {promedio:.2f} °C")


# --- Flujo principal del programa ---
def main():
    print("=== Promedio Semanal del Clima ===")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    mostrar_resultado(promedio)


# Ejecutar el programa
if __name__ == "__main__":
    main()
