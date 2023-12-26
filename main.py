import requests
import json
import time

endpoints = [
    'https://graph.microsoft.com/v1.0/me/drive/root',
    'https://graph.microsoft.com/v1.0/me/drive',
    'https://graph.microsoft.com/v1.0/drive/root',
    'https://graph.microsoft.com/v1.0/users',
    'https://graph.microsoft.com/v1.0/me/messages',
    'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules',
    'https://graph.microsoft.com/v1.0/me/drive/root/children',
    'https://api.powerbi.com/v1.0/myorg/apps',
    'https://graph.microsoft.com/v1.0/me/mailFolders',
    'https://graph.microsoft.com/v1.0/me/outlook/masterCategories'
]

def get_access_token(refresh_token, client_id, client_secret):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': 'http://localhost:53682/'
    }
    html = requests.post('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=data, headers=headers)
    jsontxt = json.loads(html.text)
    refresh_token = jsontxt['refresh_token']
    access_token = jsontxt['access_token']
    return access_token

def main():
    access_token = get_access_token(refresh_token, client_id, client_secret)
    session = requests.Session()
    session.headers.update({
        'Authorization': access_token,
        'Content-Type': 'application/json'
    })
    num = 0
    for endpoint in endpoints:
        try:
            response = session.get(endpoint)
            if response.status_code == 200:
                num += 1
                print(f'{num}th Call successful')
        except requests.exceptions.RequestException as e:
            print(e)
            pass
    localtime = time.asctime(time.localtime(time.time()))
    print('The end of this run is :', localtime)

for _ in range(3):
    main()
