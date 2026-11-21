from domotica.dispositivos import *
from domotica.hub import Hub
from domotica.interfaces import *
from domotica.common import DatoInvalido, Duplicado, NoEncontrado


def main():

    print("------ INICIO DEMO DOMOTICA ------")

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
                raise DatoInvalido(
                    f"Identificador inválido: {datos['id']}"
                )

            if datos["tipo"] == "sensor":
                dispositivo = SensorTemperatura(
                    datos["id"], datos["nombre"],
                    datos["fabricante"], datos["celsius"]
                )

            elif datos["tipo"] == "bombilla":
                dispositivo = BombillaInteligente(
                    datos["id"], datos["nombre"],
                    datos["fabricante"], datos["brillo"]
                )

            elif datos["tipo"] == "cerradura":
                dispositivo = CerraduraInteligente(
                    datos["id"], datos["nombre"],
                    datos["fabricante"]
                )

            hub.registrar(dispositivo)
            print(f"Registrado: {dispositivo}")

        except (DatoInvalido, Duplicado) as e:
            print(f"Error al registrar: {e}")

    try:
        duplicado = BombillaInteligente(
            "B001", "Otra bombilla", "Philips", 70
        )
        hub.registrar(duplicado)

    except Duplicado as e:
        print(e)

    print("------ DISPOSITIVOS REGISTRADOS ------")

    for dispositivo in hub.listar():
        print(dispositivo)

   
    print("\n===== CAPACIDADES =====")

    for dispositivo in hub.listar():
        capacidades = []

        if isinstance(dispositivo, Medible):
            capacidades.append("Medible")

        if isinstance(dispositivo, Conmutable):
            capacidades.append("Conmutable")

        if isinstance(dispositivo, Actualizable):
            capacidades.append("Actualizable")

        print(f"{dispositivo.get_id()}: {', '.join(capacidades)}")

  
    print("\n===== OPERACIONES DEL HUB =====")
    hub.operar_todos()

  
    print("\n===== ACCIONES ESPECÍFICAS =====")

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

    # 8. Operaciones con cerradura
    cerradura = hub.buscar("C001")

    print(f"\nEstado inicial de cerradura: {cerradura.get_bloqueada()}")

    cerradura.bloquear()
    print("Cerradura bloqueada")

    cerradura.desbloquear()
    print("Cerradura desbloqueada")

    # 9. Estadísticas
    print("\n===== ESTADÍSTICAS =====")

    estadisticas = hub.estadisticas()

    for tipo, cantidad in estadisticas.items():
        print(f"{tipo}: {cantidad}")

    print(f"Total de dispositivos: {len(hub.listar())}")

    # 10. Buscar dispositivo inexistente
    print("\n===== PRUEBA DE BÚSQUEDA =====")

    try:
        hub.buscar("X999")

    except NoEncontrado as e:
        print(e)


if __name__ == "__main__":
    main()



