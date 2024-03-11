class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda
        self.pregunta = None  

    def mostrar_contenido_ayuda(self):
        return f"Contenido: {self.contenido}, Ayuda: {self.ayuda or 'No disponible'}"
