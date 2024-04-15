from django.shortcuts import render
from django.urls import path
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from . import views
from accounts.models import Users
# Create your views here.

def index(request):
    ##전달할 정보 없을시 {}로 표시
    # if request.user.is_authenticated:   
    #     user=Users.objects.get(user_id=request.COOKIES.get('user_id'))
    #     pageContext={'user':user}
    #     return render(request,'homemain/index.html',pageContext)
    return render(request,'homemain/index.html',{})
def boardList(request):
     return HttpResponse("Invalid request method", status=405)