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
        id_ = request.POST.get('userID', '')
        pw_ = request.POST.get('userPW', '')
        print("id = " + id_ + " pw = " + pw_)
        login_result = authenticate(userID=id_, password=pw_)
        if login_result:
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
        username = request.POST['userName']
        userid = request.POST['userID']
        userpw = request.POST['userPW']
        userpw2 = request.POST['userPW2']
        useremail = request.POST['userEmail']
        userbigmajor = request.POST['bigMajor']
        usersmallmajor = request.POST['smallMajor']
        if userpw == userpw2:
            user = User.objects.create_user(username, useremail, userpw)
            user.userName = username
            user.userID = userid
            user.userBigMajor = userbigmajor
            user.userSmallMajor = usersmallmajor
            user.save()
        return render(request, 'login/login.html')
    return render(request, 'register/register.html')


def grades(request):
    return render(request, 'grades/grades.html')