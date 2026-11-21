from domotica.dispositivos import (
    SensorTemperatura,
    BombillaInteligente,
    CerraduraInteligente,
)
from domotica.hub import Hub
from domotica.interfaces import Medible, Conmutable, Actualizable
from domotica.common import Utils, DatoInvalido, Duplicado, NoEncontrado


def main():

    print("------ INICIO DEMO DOMOTICA ------")

    print()

    hub = Hub()

    dispositivos = [
        {
            "tipo": "sensor",
            "id": "S001",
            "nombre": "Sensor salón",
            "fabricante": "Samsung",
            "celsius": 22.5,
        },
        {
            "tipo": "sensor",
            "id": "S002",
            "nombre": "Sensor cocina",
            "fabricante": "Xiaomi",
            "celsius": 24.0,
        },
        {
            "tipo": "bombilla",
            "id": "B001",
            "nombre": "Luz salón",
            "fabricante": "Philips",
            "brillo": 50,
        },
        {
            "tipo": "bombilla",
            "id": "B002",
            "nombre": "Luz cocina",
            "fabricante": "Xiaomi",
            "brillo": 80,
        },
        {
            "tipo": "cerradura",
            "id": "C001",
            "nombre": "Puerta principal",
            "fabricante": "Nuki",
        },
        {
            "tipo": "cerradura",
            "id": "C002",
            "nombre": "Puerta garaje",
            "fabricante": "Nuki",
        },
        {
            "tipo": "bombilla",
            "id": "B00_",
            "nombre": "Luz inválida",
            "fabricante": "Philips",
            "brillo": 60,
        },
    ]

    for datos in dispositivos:
        try:
            if not Utils.validar_id(datos["id"]):
                raise DatoInvalido(f"Identificador inválido: {datos['id']}")

            if datos["tipo"] == "sensor":
                dispositivo = SensorTemperatura(
                    datos["id"], datos["nombre"], datos["fabricante"], datos["celsius"]
                )

            elif datos["tipo"] == "bombilla":
                dispositivo = BombillaInteligente(
                    datos["id"], datos["nombre"], datos["fabricante"], datos["brillo"]
                )

            elif datos["tipo"] == "cerradura":
                dispositivo = CerraduraInteligente(
                    datos["id"], datos["nombre"], datos["fabricante"]
                )

            hub.registrar(dispositivo)
            print(f"Registrado: {dispositivo}")

        except (DatoInvalido, Duplicado) as e:
            print(f"Error al registrar: {e}")

    try:
        duplicado = BombillaInteligente("B001", "Otra bombilla", "Philips", 70)
        hub.registrar(duplicado)

    except Duplicado as e:
        print(e)

    print()
    print("------ DISPOSITIVOS REGISTRADOS ------")
    print()

    for dispositivo in hub.listar():
        print(dispositivo)

    print()
    print("------ CAPACIDADES ------")
    print()

    medibles = 0
    conmutables = 0
    actualizables = 0

    for dispositivo in hub.listar():
        capacidades = []

        if isinstance(dispositivo, Medible):
            capacidades.append("Medible")
            medibles += 1

        if isinstance(dispositivo, Conmutable):
            capacidades.append("Conmutable")
            conmutables += 1

        if isinstance(dispositivo, Actualizable):
            capacidades.append("Actualizable")
            actualizables += 1

        print(f"{dispositivo.get_id()}: {', '.join(capacidades)}")

    print()
    print("------ RESUMEN CAPACIDADES ------")
    print()
    print(f"Medibles: {medibles}")
    print(f"Conmutables: {conmutables}")
    print(f"Actualizables: {actualizables}")
    print()

    print("------ OPERACIONES DEL HUB ------")
    print()

    cerradura = hub.buscar("C001")
    print(f"Estado inicial : {'bloqueada' if cerradura.get_bloqueada() else 'desbloqueada'}")

    hub.operar_todos()

    print(f"Estado tras operar el Hub: {'bloqueada' if cerradura.get_bloqueada() else 'desbloqueada'}")

    print()
    print("------ ACCIONES ESPECÍFICAS ------")
    print()

    bombilla = hub.buscar("B001")

    bombilla.set_brillo(90)
    print(f"Nuevo brillo: {bombilla.get_brillo()}")

    try:
        if Utils.validar_version("1.2.3"):
            bombilla.actualizar_firmware("1.2.3")
            print("Firmware actualizado correctamente")

        bombilla.actualizar_firmware("1.0")

    except DatoInvalido as e:
        print(f"Error de firmware: {e}")

    cerradura.bloquear()
    print("Cerradura bloqueada")

    cerradura.desbloquear()
    print("Cerradura desbloqueada")
    print()

    print("------ ESTADÍSTICAS ------")
    print()

    estadisticas = hub.estadisticas()

    for tipo, cantidad in estadisticas.items():
        print(f"{tipo}: {cantidad}")

    print(f"Total de dispositivos: {len(hub.listar())}")

    print()
    print("------ PRUEBA DE BÚSQUEDA ------")
    print()

    try:
        hub.buscar("X999")

    except NoEncontrado as e:
        print(e)

    print()
    print("------ PRUEBA DE VALIDACIÓN ------")
    print()

    id_invalido = "A_01"
    print(f"Validar {id_invalido}: {Utils.validar_id(id_invalido)}")

    print()
    print("------ FIN DE LA DEMO ------")


if __name__ == "__main__":
    main()
