import json
import yaml
import requests



class Login:

    def __init__(self, host, username, password, **kwargs):
        headers = {'content-type': 'application/json', 'x-api-version': '300'}
        payload = {'username': username, 'password': password}

        response = requests.post(
            "https://{}/rest/global/login-sessions".format(host),
            verify=False,
            headers=headers,
            data=json.dumps(payload)
        )
        credential = response.json()
        headers['auth'] = credential['auth_token']

        self.__headers = headers
        self.__verify = kwargs.pop('verify', False)

    def new_session(self):
        session = requests.Session()
        session.headers = self.__headers
        session.verify = self.__verify
        return session


s = Login(host='15.114.114.194', username='administrator', password='hpvse123').new_session()
for i in range(1, 81):
    p = {
        "name": "group-sub-{}".format(i),
        "type": "static",
        "parentUri": "/rest/global/groups/7fbe43c4-52a4-453c-80a2-38183dc39949"
    }
    r = s.post('https://15.114.114.194/rest/global/groups/', json=p)
    print(r.status_code, r.json())
s.close()
