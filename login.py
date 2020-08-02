# import requests
#
#
# class user_session():
#     def login(requests):
#         if requests.POST == "POST":
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(request, username=username, password=password)
#             if user is not None:
#                 auth.login(request, user)
#                 return redirect('home')
#             else:
#                 return render(request, 'login.html', {'error':'username or password is not correct.'})
#         else :
#             return render(request, 'login.html')
#
#     def log_out():
#         auth.logout(request)
#         return redirect('home')
#
#
# user = user_session()
# user.login(requests)
# user.log_out()
