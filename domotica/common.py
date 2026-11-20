class DatoInvalido(ValueError):
    pass


class Duplicado(Exception):
    pass


class NoEncontrado(Exception):
    pass


class Utils:
    @staticmethod
    def validar_id(texto: str) -> bool:
        if not isinstance(texto, str):
            raise DatoInvalido("El identificador debe ser un texto")

        texto_sin_espacios = texto.strip()

        if texto_sin_espacios == "":
            raise DatoInvalido("El identificador no puede estar vacío")

        if not texto_sin_espacios[0].isalpha():
            raise DatoInvalido("El identificador debe empezar por una letra")

        for caracter in texto_sin_espacios:
            if not caracter.isalnum() and caracter != "-":
                raise DatoInvalido("El identificador contiene caracteres no permitidos")

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

        id = f"{prefijo}{n:03d}"

        try:
            Utils.validar_id(id)
        except DatoInvalido:
            raise (f"ID generado inválida: {id}")

        return id

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
