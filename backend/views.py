import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # import
from django.contrib.auth import authenticate, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User, auth
from .models import userData
from datetime import date

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        
        jsonData = json.loads(request.body)

        user_name = jsonData['username']
        first_N = jsonData['first_name']
        last_N = jsonData['last_name']
        e_Mail = jsonData['email']
        dofb = jsonData['dob']
        contact = jsonData['contact']
        # pass_word = make_password(jsonData['password'])
        pass_word = jsonData['password']

        if User.objects.filter(username = user_name).exists():
            print("Username Taken")
            return JsonResponse({
                "success": False,
                "error" : "User name Taken"
            })
        elif User.objects.filter(email = e_Mail).exists():
            print("Email already Exist")
            return JsonResponse({
                "success": False,
                "error" : "Email already Exist"
            })
        else:
            user = User.objects.create_user(
                password = pass_word,
                username = user_name,
                first_name = first_N,
                last_name = last_N,
                email = e_Mail
            )
            user.save()

            # signInData = userData(
            #     userName = user_name,
            #     password = pass_word,
            #     firstName = first_N,
            #     lastName = last_N,
            #     email = e_Mail,
            #     dob = dofb,
            #     contactNumber = contact,
            #     dateJoined = date.today()
            #     )
            # signInData.save();

            userInfo = {
                'User Name' : user_name,
                'First Name' : first_N,
                'Last Name' : last_N,
                'E-Mail' : e_Mail,
                'Date of Birth' : dofb,
                'Contact' : contact,
                'Encrypted Password' : pass_word
            }
            print(userInfo)
            print("Data Saved")
            return JsonResponse(userInfo)
    else:
        print('Error')
        return JsonResponse({
                "success": False,
                "error" : "Unknown error"
            })
@csrf_exempt
def login(request):
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        user = authenticate(username = jsonData['userName'],password = jsonData['password'])
        if user is not None:
            requests.session['user'] = jsonData['userName']
            return JsonResponse({
            "Success" : True,
            "Error" : "Login Success"
        })
        else:    
            return JsonResponse({
            "Success" : False,
            "Error" : "Username or Password Wrong"
        })
    else:
        return JsonResponse({
            "Success" : False,
            "Error" : "No Request"
        })
@csrf_exempt
def user(request):
    return JsonResponse({
        "User" : request.session.get('user')
    })
@csrf_exempt
def logouts(request):
    logout(request)
    return JsonResponse({
        "User" : "None"
    })