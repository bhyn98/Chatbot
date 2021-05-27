from django.contrib import auth
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ChatbotApp.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


@csrf_exempt
def login(request):
    if request.method == 'POST':
        print("request log" + str(request.body))
        id_ = request.POST['userID_']
        pw_ = request.POST['userPW_']
        print("id = " + id_ + " pw = " + pw_)
        login_result = auth.authenticate(username=id_, password=pw_)
        if login_result is not None:
            print("로그인 성공")
            return render(request, 'chatPage/chatPage.html')
        else:
            print("로그인 실패")
            return render(request, 'login/login.html')
    return render(request, 'login/login.html')


def chatPage(request):
    return render(request, 'chatPage/chatPage.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('userName','')
        userid = request.POST.get('userID','')
        userpw = request.POST.get('userPW','')
        userpw2 = request.POST.get('userPW2','')
        useremail = request.POST.get('userEmail','')
        userbigmajor = request.POST.get('bigMajor','')
        usersmallmajor = request.POST.get('smallMajor','')
        if userpw == userpw2:
            user = User.objects.create_user(userid, useremail, userpw)
            #create_user 여기는 건들지 마셈
            user.userID = username
            user.userBigMajor = userbigmajor
            user.userSmallMajor = usersmallmajor
            user.save()
        return render(request, 'login/login.html')
    return render(request, 'register/register.html')


def grades(request):
    return render(request, 'grades/grades.html')