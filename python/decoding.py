import base64 
base64_message = 'dHVvbmd5ZXV0aGFv'
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
data = message_bytes.decode('ascii')
print(data)



