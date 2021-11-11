import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt  # import
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
        pass_word = jsonData['password']

        if User.objects.filter(username=user_name).exists():
            print("Username Taken")
            return JsonResponse({
                "success": False,
                "error": "User name Taken"
            })
        elif User.objects.filter(email=e_Mail).exists():
            print("Email already Exist")
            return JsonResponse({
                "success": False,
                "error": "Email already Exist"
            })
        else:
            user = User.objects.create_user(
                password=pass_word,
                username=user_name,
                first_name=first_N,
                last_name=last_N,
                email=e_Mail
            )
            user.save()

            signInData = userData(
                userName=user_name,
                firstName=first_N,
                lastName=last_N,
                email=e_Mail,
                dob=dofb,
                contactNumber=contact,
                dateJoined=date.today()
            )
            signInData.save()

            userInfo = {
                'User Name': user_name,
                'First Name': first_N,
                'Last Name': last_N,
                'E-Mail': e_Mail,
                'Date of Birth': dofb,
                'Contact': contact,
                'Encrypted Password': pass_word,
                'success': True
            }
            print(userInfo)
            print("Data Saved")
            return JsonResponse(userInfo)
    else:
        print('Error')
        return JsonResponse({
            "success": False,
            "error": "Unknown error"
        })


@csrf_exempt
def login(request):
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        if "userName" in jsonData.keys():

            user = authenticate(
                username=jsonData['userName'],
                password=jsonData['password']
            )

            if user is not None:
                request.session['user'] = jsonData['userName']
                return JsonResponse({
                    "success": True,
                    "error": "Login Success",
                })
            else:
                return JsonResponse({
                    "success": False,
                    "error": "Username or Password Wrong"
                })
        elif "email" in jsonData.keys():
            try:
                userInfoByEmail = User.objects.get(email=jsonData['email'])
            except:
                return JsonResponse({"Error": "No User Found"})

            print(userInfoByEmail.username)
            user = authenticate(
                username=userInfoByEmail.username,
                password=jsonData['password']
            )

            if user is not None:
                request.session['user'] = userInfoByEmail.username
                return JsonResponse({
                    "success": True,
                    "error": "Login Success",
                })
            else:
                return JsonResponse({
                    "success": False,
                    "error": "Email or Password Wrong"
                })
        else:
            try:
                userInfoByCont = userData.objects.get(
                    contactNumber=jsonData['contactNumber'])
            except:
                return JsonResponse({"Error": "Cont No User Found"})
            user = authenticate(
                username=userInfoByCont.userName,
                password=jsonData['password'])
            if user is not None:
                request.session['user'] = userInfoByCont.userName
                return JsonResponse({
                    "success": True,
                    "error": "Login Success"
                })
            else:
                return JsonResponse({
                    "success": False,
                    "error": "Contact Number or Password Wrong"
                })

    else:
        return JsonResponse({
            "success": False,
            "error": "No Request"
        })


@csrf_exempt
def user(request):
    return JsonResponse({
        "User": request.session.get('user')
    })


@csrf_exempt
def logouts(request):
    logout(request)
    return JsonResponse({
        "User": "None"
    })


@csrf_exempt
def userProfile(request, userID):
    try:
        print(userID)
        userInformation = userData.objects.get(userName=userID)
        return JsonResponse({
            "success": True,
            "Data":{
                'userName': userInformation.userName,
                'firstName': userInformation.firstName,
                'lastName': userInformation.lastName,
                'email': userInformation.email,
                'dob': userInformation.dob,
                'contactNumber': userInformation.contactNumber,
                'address': userInformation.address,
                'city': userInformation.city,
                'state': userInformation.state,
                'bio': userInformation.bio,
                'skills': userInformation.skills,
                'projects': userInformation.projects,
                'linkGithub': userInformation.linkGithub,
                'linkLinkedIn': userInformation.linkLinkedIn,
                'linkExtra': userInformation.linkExtra,
            }
        })
    except Exception as e:
        print(e)
        return JsonResponse({
            "success": False,
            "error": "User not found"
        })
