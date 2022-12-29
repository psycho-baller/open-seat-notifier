import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

# https://medium.com/@sachadehe/encrypt-decrypt-data-between-python-3-and-javascript-true-aes-algorithm-7c4e2fa3a9ff
def decrypt(password):
    """ Decrypt username and password """

    #CBC with Fix IV

    # data = password
    key = os.getenv('DECRYPT_KEY') #16 char for AES128

    #FIX IV
    iv =  'UWPMBFUOMDOADSJX'.encode('utf-8') #16 char for AES128

    def decrypt(enc,key,iv):
            enc = base64.b64decode(enc)
            cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
            return unpad(cipher.decrypt(enc),16)

    decrypted = decrypt(password,key,iv)
    return decrypted.decode("utf-8", "ignore")