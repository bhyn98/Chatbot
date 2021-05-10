from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ChatbotApp.models import Users
from ChatbotApp.serializers import Users_Serializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        query_set = Users.objects.all()
        serializer = Users_Serializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Users_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user(request, pk):
    obj = Users.objects.get(pk=pk)
    # 단건?조회?

    if request.method == 'GET':
        serializer = Users_Serializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Users_Serializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    # elif request.method == 'DELETE':
    #     obj.delete()
    #     return HttpResponse(status=204)
    #


def users_Serializer(data):
    pass


@csrf_exempt
def login(request):
    if request.method == 'POST':
        print("request log" + str(request.body))
        id = request.POST.get('userID', '')
        pw = request.POST.get('userPW', '')
        print("id = " + id + " pw = " + pw)
        login_result = authenticate(username=id, password=pw)
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
        if userpw == userpw2:
            user = User.objects.create_user(userid, userpw, useremail)
            user.save()
        return render(request, 'login/login.html')
    return render(request, 'register/register.html')


def grades(request):
    return render(request, 'grades/grades.html')


