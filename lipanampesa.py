import requests
import keys
from datetime import datetime
import base64



def gen_formated_timestamp():
    unformatted_date = datetime.now()
    formated_date = unformatted_date.strftime('%Y%m%d%H%M%S')
    return formated_date


def gen_encoded_password(formated_date):
    encoded = "174379bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919" + formated_date
    encoded_string = base64.b64encode(encoded.encode())
    passwrd = encoded_string.decode('utf-8')
    return passwrd


time_stp = gen_formated_timestamp()

passwd = gen_encoded_password(time_stp)

import requests
from requests.auth import HTTPBasicAuth
def gen_access_token(): 
    consumer_key = "vGaq5fq4X3NNbsGAftkRmgjyy9N2h3Gp"
    consumer_secret =  "pZAno0CMSEUIyh8E"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    myaccess_token = r.json()['access_token']
    return myaccess_token

def lipa_na_mpesa():
    access_token = gen_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode":"174379",
        "Password": passwd,
        "Timestamp": time_stp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA":"254724675145",
        "PartyB": "174379",
        "PhoneNumber": '254724675145',
        "CallBackURL": "http://bejawelfare.pythonanywhere.com/lnm",
        "AccountReference": "4000",
        "TransactionDesc": "School fees"
        }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)


# lipa_na_mpesa()