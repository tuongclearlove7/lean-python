import base64
num = 1
string1 = "u"
num1 = 0
string2 = "n"
num2 = 9
string3 = "y"
num3 = 3
string4 = "u"
num4 = 1
string5 = "h"
num5 = 4
num6 = 0
num7 = 1



lists = [1,"u",0,"n",9,"y",3,"u",1,"h",4,0,1]
arr_num = [1,0,9,3,1,4,0,1]
log_bytes = bytes(arr_num)
#print("num : ",log_bytes)

string = "tuongyeuthao1"
#string với mã hóa 'utf-8'
log_bytes_string = bytes(string, 'utf-32')
#print(log_bytes_string)

arr = []
arr.append(log_bytes_string)
print(arr)