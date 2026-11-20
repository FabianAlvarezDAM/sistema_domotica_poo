from base import Dispositivo
from dispositivos import BombillaInteligente
from interfaces import *


class Hub:
    _dispositivos: dict[str, Dispositivo]

    def __init__(self):
        self._dispositivos = {}

    def registrar(self, disp: Dispositivo):
        if disp.get_id() in self._dispositivos:
            raise ValueError("El dispsoitivo ya registrado")

        self._dispositivos[disp.get_id()] = disp

    def listar(self):
            return list(self._dispositivos.values())

    def operar_todos(self):
        for dispositivo in self._dispositivos.values():
            if isinstance(dispositivo, Medible):
                print(dispositivo.leer_valor())

            if isinstance(dispositivo, Conmutable):
                if isinstance(dispositivo, BombillaInteligente):
                    if dispositivo.get_encendida():
                        dispositivo.apagar()
                    else:
                        dispositivo.encender()


