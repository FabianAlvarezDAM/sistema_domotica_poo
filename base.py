from abc import ABC, abstractmethod


class Dispositivo(ABC):
    _id: str
    _nombre: str
    _fabricante: str

    def __init__(self, id, nombre, fabricante):
        self._id = id
        self._nombre = nombre
        self._fabricante = fabricante

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_fabricante(self):
        return self._fabricante

    def set_fabricante(self, fabricante):
        self._fabricante = fabricante

    def __str__(self):
        return f"[DISPOSITIVO] id : {self._id} || nombre: {self._nombre} || fabricante: {self._fabricante}"

    @abstractmethod
    def tipo():
        pass
