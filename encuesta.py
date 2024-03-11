class Encuesta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = []
        self.listados_respuestas = []

    def mostrar_encuesta(self):
        preguntas_info = [p.mostrar_enunciado_ayuda_alternativas() for p in self.preguntas]
        return f"Encuesta: {self.nombre}\nPreguntas:\n{', '.join(preguntas_info)}"

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, edad_minima, edad_maxima):
        super().__init__(nombre)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, regiones):
        super().__init__(nombre)
        self.regiones = regiones
