class DatoInvalido(ValueError):
    """Se lanza cuando un dato no cumple con las reglas previstas."""

    pass


class Duplicado(Exception):
    """Se lanza cuando un identificador ya está registrado"""

    pass


class NoEncontrado(Exception):
    """Se lanza cuando no existe un identificador."""

    pass


class Utils:
    @staticmethod
    def validar_id(texto: str) -> bool:
        if not isinstance(texto, str):
            return False

        texto_sin_espacios = texto.strip()

        if texto_sin_espacios == "":
            return False

        if not texto_sin_espacios[0].isalpha():
            return False

        for caracter in texto_sin_espacios:
            if not caracter.isalnum() and caracter != "-":
                return False

        return True

    @staticmethod
    def fabricar_id(prefijo: str, n: int) -> str:
        if not isinstance(prefijo, str) or prefijo.strip() == "":
            raise DatoInvalido("El prefijo debe ser un texto o no estar vacío")

        prefijo = prefijo.upper()

        if not isinstance(n, int):
            raise DatoInvalido("El número debe ser un entero")

        if not 0 < n:
            raise DatoInvalido("El número debe ser positivo")

        id_candidato = f"{prefijo}{n:03d}"

        if Utils.validar_id(id_candidato) == False:
            raise DatoInvalido(f"ID generado inválido: {id_candidato}")

        return id_candidato

    @staticmethod
    def validar_version(version: str) -> bool:
        if not isinstance(version, str):
            return False

        partes = version.split(".")

        if len(partes) != 3:
            return False

        for parte in partes:
            if not parte.isdigit():
                return False

        return True
