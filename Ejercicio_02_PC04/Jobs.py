# Jobs.py
import requests

def obtener_tipo_cambio():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        fecha = data.get("fecha")
        valor_cambio = float(data.get("valor", 0))

        return fecha, valor_cambio

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el tipo de cambio: {e}")
        return None, None

def actualizar_tipo_cambio():
    fecha, valor_cambio = obtener_tipo_cambio()

    if fecha is not None and valor_cambio is not None:
        print(f"Tipo de cambio actualizado: Fecha: {fecha}, Valor: {valor_cambio}")
    else:
        print("No se pudo obtener el tipo de cambio.")
