from Crypto.PublicKey import RSA

llave = RSA.generate(2048)

f = open("llaveprivada.pem", "wb")
f.write(llave.exportKey('PEM'))
f.close()

f = open("llavepublica.pem", "wb")
f.write(llave.publickey().exportKey('PEM'))
f.close()
