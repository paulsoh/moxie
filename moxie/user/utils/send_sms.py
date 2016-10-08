import requests
import os


CLIENT_ID = os.environ.get('OPEN_API_ID')
CLIENT_KEY = os.environ.get('OPEN_API_KEY')


API_BASE_URL = "http://api.openapi.io/ppurio/{API_VERSION}/message/sms/{CLIENT_ID}/".format(
    API_VERSION=1,
    CLIENT_ID=CLIENT_ID,
)


def send_sms(phonenumber, data):
    response = requests.post(
        API_BASE_URL,
        data={
            'send_phone': '01023024321',
            'dest_phone': phonenumber,
            'msg_body': "http://192.168.0.13:8000/auth/verify/phonenumber/"+data+"/",
        },
        headers={
            'x-waple-authorization': CLIENT_KEY,
        }
    )

    return response
