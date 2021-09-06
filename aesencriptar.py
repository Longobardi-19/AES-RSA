from Crypto.Cipher import AES
from Crypto import Random

def encriptar(mensaje):
    mensaje = mensaje
    key = "lallavesecreta12"
    #key1 = str.encode(key)

    iv = Random.new().read(AES.block_size)
    cifrado = AES.new(key.encode(), AES.MODE_CFB, iv)
    #msg = base64.b64encode(iv + cifrado.encrypt(str.encode(mensaje)))
    #Con la linea debajo toma cualquier caracter, si lo usan borrar el import base64
    msg = iv + cifrado.encrypt(mensaje.encode())
    f = open('textoencriptado.txt', 'wb')
    f.write(msg)
    f.close()
    print(msg)


encriptar("atacar al amanecer")
