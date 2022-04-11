file_object = open("password.txt")
data = file_object.read()
print(data)
k = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x%2!=0, k)))
n = k
n.append(data)
print(n)





