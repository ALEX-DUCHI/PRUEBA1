# ==========================================================
# 🧠 ABSTRACCIÓN
# ==========================================================
# Creamos una clase abstracta que define la estructura base de cualquier persona en la escuela.
# No todas las personas se comportan igual (alumnos, profesores), pero comparten rasgos comunes.

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad):
        self._nombre = nombre    # atributo protegido
        self._edad = edad        # atributo protegido

    def mostrar_datos(self):
        print(f"Nombre: {self._nombre} | Edad: {self._edad}")

    @abstractmethod
    def presentarse(self):
        pass


# ==========================================================
# 🔒 ENCAPSULACIÓN
# ==========================================================
# Los atributos privados no se pueden modificar directamente, se accede con getters y setters.

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.__nota_promedio = 0.0  # atributo privado
        self.grado = grado

    def get_nota_promedio(self):
        return self.__nota_promedio

    def set_nota_promedio(self, nueva_nota):
        if 0 <= nueva_nota <= 10:
            self.__nota_promedio = nueva_nota
        else:
            print("⚠️ Nota inválida. Debe estar entre 0 y 10.")

    # ==========================================================
    # 🧬 HERENCIA + 🎭 POLIMORFISMO
    # ==========================================================
    def presentarse(self):
        print(f"👦 Soy {self._nombre}, estudiante de {self.grado} grado.")

    def estudiar(self):
        print(f"{self._nombre} está estudiando para mejorar su nota...")


class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def presentarse(self):
        print(f"👩‍🏫 Hola, soy el profesor {self._nombre} y enseño {self.materia}.")

    def calificar(self, estudiante, nota):
        print(f"{self._nombre} está calificando a {estudiante._nombre}...")
        estudiante.set_nota_promedio(nota)


# ==========================================================
# 🎭 POLIMORFISMO
# ==========================================================
# Una misma función puede recibir diferentes tipos de objetos (Profesor o Estudiante)
# y ejecuta el método correspondiente dependiendo del tipo real del objeto.

def dia_en_la_escuela(persona):
    persona.mostrar_datos()
    persona.presentarse()
    if isinstance(persona, Estudiante):
        persona.estudiar()
    elif isinstance(persona, Profesor):
        print(f"{persona._nombre} prepara su clase de {persona.materia}.")


# ==========================================================
# 🚀 EJECUCIÓN DEL PROGRAMA
# ==========================================================

est1 = Estudiante("Luna", 15, "3°")
est2 = Estudiante("Diego", 16, "4°")
prof1 = Profesor("Marina", 35, "Matemáticas")

# Actividades diarias (polimorfismo)
print("\n🏫 Un día en la escuela:")
dia_en_la_escuela(est1)
dia_en_la_escuela(prof1)

# El profesor califica a los estudiantes
print("\n📝 Calificaciones:")
prof1.calificar(est1, 9)
prof1.calificar(est2, 11)  # nota inválida

# Comprobamos encapsulación (acceso controlado)
print("\n🔒 Verificando encapsulación:")
print(f"Nota de {est1._nombre}: {est1.get_nota_promedio()}")
est1.set_nota_promedio(8)
print(f"Nota ajustada de {est1._nombre}: {est1.get_nota_promedio()}")
