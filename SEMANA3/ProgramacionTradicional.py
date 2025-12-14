def ingresar_temperaturas():
    "Solicita al usuario las temperaturas de los 7 días de la semana."
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for dia in dias:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print(" Valor inválido. Por favor, ingrese un número.")
    return temperaturas

def calcular_promedio(temperaturas):
    "Calcula el promedio semanal de una lista de temperaturas."
    return sum(temperaturas) / len(temperaturas)

def mostrar_resultado(promedio):
    "Muestra el promedio semanal de temperatura."
    print(f"\n El promedio semanal de temperatura es: {promedio:.2f}°C")

def main():
    print("Calcular el promedio semanal del clima ")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    mostrar_resultado(promedio)

if __name__ == "__main__":
    main()
