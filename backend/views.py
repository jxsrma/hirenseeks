from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # import
@csrf_exempt  # add this token before defining function

# Create your views here.
def demo(request):

    if request.method == 'POST':
        artname = request.POST['artname']
        email = request.POST['email']
        trackname = request.POST['trackname']
        trackurl = request.POST['trackurl']
        infotext = request.POST['infotext']
        print('success')

        demoData = Demosubs(a_name = artname, a_email = email, t_name = trackname, t_url = trackurl, t_dis = infotext )
        demoData.save()
        return render(request,'demo.html')

    else:    
        return render(request,'demo.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        return JsonResponse({'name':name})
    else:
        print('Error')
        return "Error"