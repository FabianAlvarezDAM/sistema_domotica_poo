from typing import Protocol, runtime_checkable

@runtime_checkable
class Medible(Protocol):
    def leer_valor(self) -> float:
        pass

@runtime_checkable
class Conmutable(Protocol):
    def encender(self)  -> None:
        pass

    def apagar(self) -> None:
        pass

@runtime_checkable
class Actualizable(Protocol):
    def actualizar_firmware(self, version : str) -> None:
        pass