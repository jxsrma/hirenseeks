import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # import
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User, auth
from .models import userData
from datetime import date

@csrf_exempt
def login(request):
    if request.method == 'POST':
        
        jsonData = json.loads(request.body)

        user_name = jsonData['username']
        first_N = jsonData['first_name']
        last_N = jsonData['last_name']
        e_Mail = jsonData['email']
        dofb = jsonData['dob']
        contact = jsonData['contact']
        pass_word = make_password(jsonData['password'])

        # demoData = Demosubs(a_name = artname, a_email = email, t_name = trackname, t_url = trackurl, t_dis = infotext )
        # demoData.save()
        # signUpData = userData()
        if userData.objects.filter(userName = user_name).exists():
            print("Username Taken")
        # else:
        #     signInData = userData(
        #         userName = user_name,
        #         password = pass_word,
        #         firstName = first_N,
        #         lastName = last_N,
        #         email = e_Mail,
        #         dob = dofb,
        #         contactNumber = contact,
        #         dateJoined = date.today()
        #         )
        #     signInData.save();

            user = User.objects.create_user(
                password = pass_word,
                username = user_name,
                first_name = first_N,
                last_name = last_N,
                email = e_Mail
            )
            user.save()

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
        return "Error"