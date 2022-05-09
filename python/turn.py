import base64
key = "tuongyeuthao"
key_encode = key.encode('ascii')
byte64 = base64.b64encode(key_encode)
log_encode = byte64.decode('ascii')
print(log_encode)





