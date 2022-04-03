import base64

file_object = open("clearlove7_developer_tool.txt")
data = file_object.read()
base64_message = data
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
log_decode = message_bytes.decode('ascii')
print(log_decode)
key_encode = log_decode.encode('ascii')
byte64 = base64.b64encode(key_encode)
log_encode = byte64.decode('ascii')
print(log_encode)


























