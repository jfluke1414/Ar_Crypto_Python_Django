from django.shortcuts import render

import requests, hashlib
from . import db_search

def chk_session():
    p_username = 'jfluke'
    p_password = '1234'
    p_email = 'jfluke1414@gmail.com'

    sha1 = hashlib.new('sha1')
    sha1.update(p_password)
    encrypted_password = sha1.hexdigest()
    print(encrypted_password)
    s = requests.session()
    s_data = {
        'is_user': True,
        'username': p_username,
        'password': encrypted_password,
        'email': p_email,
    }
    return s_data
    # session.post('login.py', s_data)

def home_view(request):
    # chk_session()

    data = db_search.get_user_info()

    return render(request, "home.html", {'data':data})

def estimated_view(request):
    return render(request, "estimated.html")

def tables_view(request):
    print(request)
    return render(request, "tables.html")

def index_view(request):
    # r = request.get('http://192.168.238.129/index/')
    #
    # print(r.text)
    return render(request, 'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('username')
        email = request.POST.get('email')