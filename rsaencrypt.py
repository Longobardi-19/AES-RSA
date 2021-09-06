from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

mensaje = "Xiaomi liderará el mercado de tecnología, se volverá Skynet-@lfa. Año 0 empieza ya!!"
key = RSA.importKey(open("llavepublica.pem", "r").read())

cifrado = PKCS1_OAEP.new(key)
cifrarmensaje = cifrado.encrypt(mensaje.encode())

f = open("textocifrado.txt", "wb")
f.write(cifrarmensaje)

f.close()