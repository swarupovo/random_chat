# from django.shortcuts import render

# Create your views here.
import pymongo
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# from .models import userdata
from django.views.generic.base import View

from .forms import UserRegForm, LoginForm

@csrf_exempt
def index(request):
    if request.user.is_authenticated:
        return render(request, 'chat/index.html', {})
    else:
        return HttpResponseRedirect('/dashboard/')

@csrf_exempt
def room(request, room_name):
    if request.user.is_authenticated:
        print(type(str(request.user)))
        ip = "127.0.0.1"
        port = "27017"
        database = "my_area_local"
        conn = pymongo.MongoClient('mongodb://{}:{}/{}'.format(ip, port, database))
        db = conn[database]
        rc = db['room_chat']
        chat_room_find_status = rc.find({'chat_room': "chat_"+room_name})
        message_lst = []
        for each in chat_room_find_status:
            message_lst.append({"message": each['message'], "time": str(each['time'].day)+"."+str(each['time'].month)
                                +"."+str(each['time'].year)})
        if chat_room_find_status.count() > 1:
            print(message_lst)
            return render(request, 'chat/room.html', {
                'room_name_json': mark_safe(json.dumps(room_name)), "usr_name": mark_safe(json.dumps(str(request.user))),
                "message": message_lst, "t": " "

            })
        else:
            return render(request, 'chat/room.html', {
                'room_name_json': mark_safe(json.dumps(room_name)), "usr_name": mark_safe(json.dumps(str(request.user)))
            })


    else:
        return HttpResponseRedirect('/dashboard/')



@csrf_exempt
def login_form(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            loginform = LoginForm(request.POST)
            if loginform.is_valid():
                data = request.POST.copy()

                username = data.get('username')
                password = data.get('password')
                confirm_password = data.get('confirm_password')

                print(username)
                print(password)
                print(confirm_password)
                try:
                    u = User.objects.get(username=username)
                    print(u.password)
                    if u:
                        user = authenticate(username=username, password=password)
                        if user is not None:
                            print("in if block")
                            login(request, user)
                            print(user)
                            messages.success(request, "you are successfully login")
                            return HttpResponseRedirect('/chat/')
                        else:
                            messages.success(request, "you entered a wrong password ")

                    else:
                        messages.error(request, "you entered a wrong username")

                except Exception as E:
                    messages.error(request, "username is not valid")
            else:
                messages.error(request, loginform.errors)
            return render(request, "chat/login.html", {'login_form': LoginForm()})
        else:
            return render(request, "chat/login.html", {'login_form': LoginForm()})
    else:
        return HttpResponseRedirect('/chat/')
@csrf_exempt
def Reg_Form(request):
    formclass = UserRegForm
    login = LoginForm

    if request.method == "GET":
        print("in get block")
        return render(request,  "chat/registration.html", {'registration_form': formclass()})

    else:
        regform = formclass(request.POST)
        if regform.is_valid():
            data = request.POST.copy()
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            username = data.get('username')
            password = data.get('password')
            email_id = data.get('email_id')


            try:
                # s = User()
                data = User(first_name=firstname, last_name=lastname, username=username, email=email_id)
                data.set_password(password)
                data.save()
                messages.success(request, "form submited successfully")
                return render(request, "chat/login.html", {'login_form': login()})

            except Exception as E:
                messages.error(request, "somithing went wrong {}".format(E))
                return render(request, "chat/registration.html", {'registration_form': formclass()})

@csrf_exempt
def dashboard(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect('/chat/')
        else:
            return render(request, "chat/base.html", {})

@csrf_exempt
def logout_form(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/dashboard/')







        # driver dictionary
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
