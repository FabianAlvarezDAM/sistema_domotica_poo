from domotica.base import Dispositivo
from domotica.common import Utils, DatoInvalido


class SensorTemperatura(Dispositivo):
    _celsius: float

    def __init__(self, id, nombre, fabricante, celsius):
        super().__init__(id, nombre, fabricante)
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, celsius):
        self._celsius = celsius

    def leer_valor(self):
        return self._celsius

    def tipo(self):
        return "SensorTemperatura"


class BombillaInteligente(Dispositivo):
    _brillo: int
    _encendida: bool
    _version_firmware: str

    def __init__(self, id, nombre, fabricante, brillo):
        super().__init__(id, nombre, fabricante)
        if brillo < 0 or brillo > 100:
            raise ValueError("El brillo ha de ser positivo y menor o igual a 100")
        self._brillo = brillo
        self._encendida = False
        self._version_firmware = "1.0.0"

    def get_brillo(self):
        return self._brillo

    def set_brillo(self, brillo):
        if brillo < 0 or brillo > 100:
            raise ValueError("El brillo ha de ser positivo y menor o igual a 100")
        self._brillo = brillo

    def get_encendida(self):
        return self._encendida

    def encender(self):
        if self._encendida:
            raise ValueError("La bombilla ya está encendida")
        self._encendida = True

    def apagar(self):
        if not self._encendida:
            raise ValueError("La bombilla ya está apagada")
        self._encendida = False

    def tipo(self):
        return "BombillaInteligente"

    def get_firmware(self):
        return self._version_firmware

    def actualizar_firmware(self, version: str):
        if not Utils.validar_version(version):
            raise DatoInvalido("La versión del firmare no es válida")

        self._version_firmware = version


class CerraduraInteligente(Dispositivo):
    _bloqueada: bool

    def __init__(self, id, nombre, fabricante):
        super().__init__(id, nombre, fabricante)
        self._bloqueada = False

    def get_bloqueada(self):
        return self._bloqueada

    def bloquear(self):
        if self._bloqueada:
            raise ValueError("La cerradura ya está bloqueada")
        self._bloqueada = True

    def desbloquear(self):
        if not self._bloqueada:
            raise ValueError("La cerradura ya está desbloqueada")

        self._bloqueada = False

    def encender(self):
        self.bloquear()

    def apagar(self):
        self.desbloquear()

    def tipo(self):
        return "CerraduraInteligente"
