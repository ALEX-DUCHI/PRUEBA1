# Clase base: representa la idea general de un género musical (ABSTRACCIÓN)
class GeneroMusical:
    def __init__(self, nombre, ritmo):
        self._nombre = nombre       # atributo protegido (ENCAPSULACIÓN)
        self._ritmo = ritmo

    def describir(self):
        print(f"🎶 Género: {self._nombre} - Ritmo: {self._ritmo}")

    def sonar(self):
        print("🎵 Este género tiene su propio sonido característico.")


# Subclase Pasillo (HERENCIA)
class Pasillo(GeneroMusical):
    def __init__(self, nombre, ritmo, guitarra):
        super().__init__(nombre, ritmo)
        self.__guitarra = guitarra   # atributo privado (ENCAPSULACIÓN)

    def get_guitarra(self):
        return self.__guitarra

    def set_guitarra(self, nueva_guitarra):
        self.__guitarra = nueva_guitarra

    # Polimorfismo: redefine cómo suena el género
    def sonar(self):
        print(f"🎸 El {self._nombre} suena fuerte con guitarras {self.__guitarra}.")


# Subclase Bachata (HERENCIA)
class Bachata(GeneroMusical):
    def sonar(self):
        print(f"🎤 El {self._nombre} tiene un ritmo bailable y pegadizo.")


# Función que usa POLIMORFISMO: acepta cualquier género y lo hace sonar
def reproducir(genero):
    genero.describir()
    genero.sonar()


# Crear objetos
rock = Pasillo("Pasillos", "lento", "eléctricas")
pop = Bachata("Bachatas", "Medio")

# Probar comportamiento polimórfico
reproducir(rock)
reproducir(pop)

# Encapsulación: acceso controlado
print("\n🔒 Encapsulación:")
print("Tipo de guitarra:", rock.get_guitarra())
rock.set_guitarra("acústicas")
print("Nuevo tipo de guitarra:", rock.get_guitarra())
