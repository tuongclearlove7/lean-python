# import facebook 

# image_url = "https://c.ndtvimg.com/2020-08/h5mk7js_cat-generic_625x300_28_August_20.jpg?im=Resize=(1230,900)"
# message = "hello world"
# link = "https://www.facebook.com/Bot-117828560890633"
# msg = message+"\n"+link
# token="EAAFSR7mzwjoBALMAyy6lRrnXvoq3akQ7h3X08stjPLT4NQcqiq6txFOYE00F8xAncgIadTUBT2ZC2xVD6y6bZCoMS6SnSnRfyOL5Oa0zr9DUT4IcLlKmpAo3jcfZCGNoE631KeOZBeEQrkjnYVxftmAN6ccBfAyx0sy23p7B5dxlnOHFHCyOgLHssFT2chw4ZCuUO2FkmBwZDZD"
# gra = facebook.GraphAPI(access_token=token)
# id = "117828560890633"
# x = gra.put_object(id, 'photos', message=msg, url=image_url)
# print(x)
# print("successfully")\

import facebook

groups = ['271754891192613']
msg = "My account has been taken over by hacker"
my_token = input("nhap token : ")
api = facebook.GraphAPI(access_token=my_token)

for i in groups:
    x= api.put_object(groups, 'feed', message=msg)
    print(x)
print("successfully")
















