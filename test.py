import requests
from django.http import HttpResponse
from django.shortcuts import render

def test():
    r = requests.get('http://192.168.238.129/index/')

    print(r.text)

def __init__(self):
    print('in_self')
    self.username = self

def chk_session():
    p_username = 'jfluke'
    p_password = '1234'
    p_email = 'jfluke1414@gmail.com'
    encrypted_password = '1234'

    # sha1 = hashlib.new('sha1')
    # sha1.update(p_password.encode('UTF-8'))
    # encrypted_password = sha1.hexdigest()

    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    s_data = {
        'is_user': True,
        'username': p_username,
        'password': encrypted_password,
        'email': p_email,
        'headers': header
    }
    s = requests.session()
    requests.session.__init__(p_username)

    # url = 'http://192.168.238.129/'
    # r = s.post(url=url, headers=header)
    # print(r.status_code)
    # print(r.text)

    return s_data
    # session.post('login.py', s_data)


def response_test():
    r = requests.get('http://192.168.238.129')
    print(r.text)

chk_session()
response_test()
