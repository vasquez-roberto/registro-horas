import csv
import os
from datetime import datetime
from zoneinfo import ZoneInfo

CSV_FILE = "registros.csv" # nombre del archivo
TIMEZONE = "America/Monterrey" # zona horaria


def registrar_hora():
    ahora = datetime.now(ZoneInfo(TIMEZONE)) # obtiene la fecha y hora actual

    archivo_existe = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as archivo: # abre el CSV
        writer = csv.writer(archivo)

        if not archivo_existe:
            writer.writerow(["fecha", "hora"])

        writer.writerow([
            ahora.strftime("%Y-%m-%d"),
            ahora.strftime("%H:%M:%S")
        ])

    print("================================")
    print("   REGISTRO AGREGADO")
    print("================================")
    print(f"Fecha: {ahora.strftime('%Y-%m-%d')}")
    print(f"Hora:  {ahora.strftime('%H:%M:%S')}")


if __name__ == "__main__":
    registrar_hora()
    
# docker run --rm -it -v "${PWD}:/app" registro-horas
# git status
# git add registros.csv
# git status
# git commit -m "Agregar nuevo registro"
# git push