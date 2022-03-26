import base64
key = "12343211234321"
key_encode = key.encode('ascii')
byte64 = base64.b64encode(key_encode)
log_decode = byte64.decode('ascii')
print(log_decode)





