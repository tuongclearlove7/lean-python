import requests
import pandas
import json


def Page_token():
    url = "http://graph.facebook.com/me/accounts"
    response = requests.get(url,headers={
            'Authorization':'Bearer' +'EAAFSR7mzwjoBAB5EvHOn0v2ZBYBiJP00MD0e6kSGhDsLiUmdIdkaASGTt2ZCr7y1Rq62JtXHvRPNLwXkgpRMgq2nVwHOxr4AyXfT1j8rioi8TfX7vpafDnbCZBetLO1K1apM5dWWWgbjalsFgg6m37QImkEMd0aWdn3xcZAwC0bdJpqa2tmy',
            'Content-Type':'application/json'
        }
    )
    response_data = json.loads(response.text)
   
    return response_data
print(Page_token())















