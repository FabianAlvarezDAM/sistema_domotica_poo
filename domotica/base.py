from abc import ABC, abstractmethod
from .common import Utils, DatoInvalido


class Dispositivo(ABC):
    _id: str
    _nombre: str
    _fabricante: str

    def __init__(self, id, nombre, fabricante):
        self.set_id(id)
        self.set_nombre(nombre)
        self.set_fabricante(fabricante)

    def get_id(self):
        return self._id

    def set_id(self, id: str):
        if not Utils.validar_id(id):
            raise DatoInvalido(f"ID inválido")
        
        self._id = id

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre: str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise DatoInvalido("El nombre no puede estar vacío")
        
        self._nombre = nombre.strip()

    def get_fabricante(self):
        return self._fabricante

    def set_fabricante(self, fabricante: str):
        if not isinstance(fabricante, str) or fabricante.strip() == "":
            raise DatoInvalido("El fabricante no puede estar vacío")
        
        self._fabricante = fabricante.strip()

    def __str__(self):
        return f"[DISPOSITIVO] id : {self._id} || nombre: {self._nombre} || fabricante: {self._fabricante} || tipo: {self.tipo()}"

    @abstractmethod
    def tipo(self) -> str:
        pass
