import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

#key shall be a byte array
key = b'STOPREADMOVESTOP'

# A byte array with size of 16 byte.
iv = b"SSSSSSSSSSSSSSSS"

def enc(text):
    cipher = AES.new(key,AES.MODE_CBC,IV=iv)
    ct_bytes = cipher.encrypt(pad(data,16))
    ct=ct_bytes.hex()
    return ct

def dec(text):
    cipher = AES.new(key,AES.MODE_CBC,IV=iv)
    ct = bytes.fromhex(text)
    ct_bytes = unpad(cipher.decrypt(ct),16)
    return ct_bytes.decode('utf-8')