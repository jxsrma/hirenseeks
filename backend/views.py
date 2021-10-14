from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # import
from django.contrib.auth.hashers import make_password, check_password

@csrf_exempt
def login(request):
    if request.method == 'POST':
        # print(request.POST)
        # username = request.POST['username']
        # firstN = request.POST['first_name']
        # lastN = request.POST['last_name']
        # eMail = request.POST['email']
        # contact = request.POST['contact']
        # password = make_password(request.POST['password'])

        # userInfo = {
        #     'User Name' : username,
        #     'First Name' : firstN,
        #     'Last Name' : lastN,
        #     'E-Mail' : eMail,
        #     'Contact' : contact,
        #     'Encrypted Password' : password
        # }

        return JsonResponse(request.POST)
    else:
        print('Error')
        return "Error"