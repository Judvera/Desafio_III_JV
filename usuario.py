class Usuario:
    def __init__(self, correo, edad, region):
        self.correo = correo
        self.edad = edad
        self.region = region

    def contestar_encuesta(self, encuesta, respuestas):
        listado_respuestas = ListadoRespuestas(self, respuestas)
        encuesta.listados_respuestas.append(listado_respuestas)

class ListadoRespuestas:
    def __init__(self, usuario, respuestas):
        self.usuario = usuario
        self.respuestas = respuestas
