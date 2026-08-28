import csv
import os
from datetime import datetime
from zoneinfo import ZoneInfo

CSV_FILE = "registros.csv"
TIMEZONE = "America/Monterrey"


def registrar_hora():
    ahora = datetime.now(ZoneInfo(TIMEZONE))

    archivo_existe = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as archivo:
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