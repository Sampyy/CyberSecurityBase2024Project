from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import password_validation
from django.http import HttpResponse
from django.contrib.auth.models import User
import sqlite3
from .models import Account, Message


# Create your views here.

@login_required
def sendmessageview(request):
    sender = request.user.account
    receiver = User.objects.get(username=request.POST.get('to')).account
    message = request.POST.get('messagefield')
    '''  Injection < woops'); DROP TABLE pages_message; INSERT INTO auth_user_user_permissions VALUES ('1', '1', '1 >  
    msg = Message(content=message, sender=sender, receiver=receiver)
    msg.save()'''
    connection = sqlite3.connect('./db.sqlite3')
    cursor = connection.cursor()
    cursor.executescript("INSERT INTO pages_message (receiver_id, sender_id, content)  VALUES ('"+ str(receiver.user.id) +"', '" + str(sender.user.id) +"', '"+ message + "');")
    connection.commit()


    return redirect('/')


def messageview(request, id):
    message = Message.objects.get(id=id)
    ''' broken access control
    if( request.user.id != message.sender.user.id) & (request.user.id != message.receiver.user.id):
        return redirect(unauthorizedview)
    '''
    print(message)
    return render(request, 'pages/message.html', {'message': message})

def unauthorizedview(request):
    return render(request, 'pages/unauthorized.html')

def registerview(request):
    return render(request, 'pages/register.html')

def registeruserview(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    '''Identification and authentication failures
    if password_validation.validate_password(password=password):
        print('invalid password')
        return redirect('register/')
    '''
    
    ''' security misconfiguration
    user = User.objects.create_user(username=username, email=email, password=password)'''
    user = User.objects.create_superuser(username=username, email=email, password=password)
    account = Account(user_id=user.id)
    account.save()
    return redirect('/')

def recoverview(request):
    
    return render(request, 'pages/recover.html')

def sendrecover(request):
    '''insecure design 
    instead for example
    request.POST.get('email')
    if user.email == email:
        send_changerequest(email)
    
    not making a real confirmation + recovery system as it feels a bit out of scope here
    '''
    username = request.POST.get('username')
    password = request.POST.get('password')
    firstquestion = request.POST.get('firstquestion')
    secondquestion = request.POST.get('secondquestion')
    user = User.objects.get(username=username)
    account = Account.objects.get(user_id=user.id)
    if (account.firstquestion == firstquestion) & (account.secondquestion == secondquestion):
        user.set_password(password)
        user.save()
        return redirect('/')
    return redirect('/recover/')

@login_required
def index(request):
    accounts = Account.objects.exclude(user_id=request.user.id)
    messages = Message.objects.filter(receiver=Account.objects.get(user_id=request.user.id))
    return render(request, 'pages/index.html', {'accounts': accounts, 'messages': messages})
