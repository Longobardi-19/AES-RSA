from Crypto.Cipher import AES
from Crypto import Random

f = open("textoencriptado.txt", "rb")
mensaje = f.read()


def desencriptar(mensaje):
    mensaje = mensaje
    key = "lallavesecreta12"
    iv = Random.new().read(AES.block_size)
    cifrado = AES.new(key.encode(), AES.MODE_CFB, iv)
    msg = cifrado.decrypt(mensaje)
    print(msg)


desencriptar(mensaje)
