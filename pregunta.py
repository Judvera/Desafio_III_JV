class Pregunta:
    def __init__(self, enunciado, ayuda=None, requerida=False):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = []
        self.encuesta = None  

    def mostrar_enunciado_ayuda_alternativas(self):
        alternativas_info = [a.mostrar_contenido_ayuda() for a in self.alternativas]
        return f"Enunciado: {self.enunciado}, Ayuda: {self.ayuda or 'No disponible'}, Alternativas: {', '.join(alternativas_info)}"
