name = "tuong"
age = 19
address = "Da nang city"
nickname = "clearlove7"
str_format = "{}\n{}".format(name,nickname)
print(str_format)
# print {name} {nickname}

print( "name: {0} , old: {1}, address: {2}".format(name,age,address))
# name: tuongi , age: 19, address: Da nang city


str1= "Name:[{:8s}], old:{:4d}".format("Ya", 18)
str2= "Name:[{0:8s}], old:{1:4d}".format("Yama", 18)
str3= "Name:[{name:8s}], old:{old:4d}".format(name="Yamad", old=18)

print(str1)
print(str2)
print(str3)

print("str1 = [{:10s}]".format("Lemon"))
#> str1 = [Lemon     ]

print("number = [{:5d}]".format(123))
#> number=[  123]

print("str1={:s}, str2={}".format("Lemon", "Apple"))

print("số dương={:+d}, số âm={:+d}".format(72, -72))
#>> số dương=+72, số âm=-72

print("số dương={:-d}, số âm={:-d}".format(72, -72))
#>> số dương=72, số âm=-72

print("số dương={: d}, số âm={: d}".format(72, -72))
#>> số dương= 72, số âm=-72