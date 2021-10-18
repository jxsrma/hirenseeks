import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # import
from django.contrib.auth.hashers import make_password, check_password

@csrf_exempt
def login(request):
    if request.method == 'POST':
        
        jsonData = json.loads(request.body)

        username = jsonData['username']
        firstN = jsonData['first_name']
        lastN = jsonData['last_name']
        eMail = jsonData['email']
        contact = jsonData['contact']
        password = make_password(jsonData['password'])

        userInfo = {
            'User Name' : username,
            'First Name' : firstN,
            'Last Name' : lastN,
            'E-Mail' : eMail,
            'Contact' : contact,
            'Encrypted Password' : password
        }
        print(userInfo)
        
        

        return JsonResponse(userInfo)
    else:
        print('Error')
        return "Error"