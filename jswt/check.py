import jwt
key="some_encrypted_key"
encoded = jwt.encode({'email':'rak','userid':'01'},key,algorithm='HS256')
print(encoded)
encoded=encoded+"o"
try:
    decoded = jwt.decode(encoded,key,algorithms="HS256")
    print(decoded)
except Exception as e:
    print(e)