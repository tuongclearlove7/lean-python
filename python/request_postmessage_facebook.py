import requests

try:
    Id = '117828560890633'
    post_url = 'https://graph.facebook.com/{}/feed'.format(Id)
    access_token = input("enter access token : ")
    mssg = 'My account has been taken over by hacker'
    payload = {"message":mssg,'access_token':access_token}
    r = requests.post(post_url,data=payload)
    print(r.text)
except:
    print("error")











