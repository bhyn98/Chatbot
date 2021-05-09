from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import  csrf_exempt
from rest_framework.parsers import JSONParser

from ChatbotApp.models import Users
from ChatbotApp.serializers import Users_Serializer


def chatPage(request):
    return render(request, 'chatPage/chatPage.html')


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


def register(request):
    return render(request, 'register/register.html')


def grades(request):
    return render(request, 'grades/grades.html')


def user(request, pk):
    data = Users.objects.get(pk=pk)
    # 단건?

    if request.method == 'GET':
        serializer = Users_Serializer(data)
        return JsonResponse(serializer.data, safe=False)


    #elif request.method == 'PUT':
     #   data = JSONParser().parse(request)
    #    serializer = Std_users_Serializer(data=data)
   #     if serializer.is_valid():
  #          serializer.save()
 #           return JsonResponse(serializer.data, status=201)
#        return JsonResponse(serializer.errors, status=400)

#    elif request.method == 'DELETE':


def login(request):
    return render(request, 'login/login.html')