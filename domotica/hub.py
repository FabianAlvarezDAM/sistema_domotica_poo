from .base import Dispositivo
from .interfaces import Medible, Conmutable
from .common import Duplicado, NoEncontrado


class Hub:
    _dispositivos: dict[str, Dispositivo]

    def __init__(self):
        self._dispositivos = {}

    def registrar(self, disp: Dispositivo):
        if disp.get_id() in self._dispositivos:
            raise Duplicado("El dispositivo ya está registrado")

        self._dispositivos[disp.get_id()] = disp

    def listar(self):
        return list(self._dispositivos.values())

    def operar_todos(self):
        for dispositivo in self._dispositivos.values():
            if isinstance(dispositivo, Medible):
                print(dispositivo.leer_valor())

            if isinstance(dispositivo, Conmutable):
                try:
                    dispositivo.encender()
                    print(f"{dispositivo.get_id()} está encendido")
                except ValueError as error:
                    print(f"Error en {dispositivo.get_id()}: {error}")

                try:
                    dispositivo.apagar()
                    print(f"{dispositivo.get_id()} está apagado")
                except ValueError as error:
                    print(f"Error en {dispositivo.get_id()}: {error}")

    def buscar(self, id: str) -> Dispositivo:
        if id not in self._dispositivos:
            raise NoEncontrado("No existe ese dispositivo")

        return self._dispositivos[id]

    def estadisticas(self) -> dict:
        resultado = {}

        for dispositivo in self._dispositivos.values():
            nombre_tipo = dispositivo.tipo()

            if nombre_tipo not in resultado:
                resultado[nombre_tipo] = 0

            resultado[nombre_tipo] += 1

        return resultado
