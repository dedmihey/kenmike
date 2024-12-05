from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


# Create your views here.

def index11(request):
    return render(request, 'one_task/hauptseite.html')


def index12(request):
    heizung = ['Vitopend ', 'Vitodens ', 'Vitogas  ']
    context = {'heizung': ['Vitopend ', 'Vitodens ', 'Vitogas  ']}
    return render(request, 'one_task/kesseln.html', context)


def index13(request):
    return render(request, 'one_task/korb.html')


def sign_up_by_html(request):
    # users = ['Tom', 'Max', 'Mike']
    buyers = Buyer.objects.all()
    context = {}
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username in users:
            context['error'] = 'Пользователь уже существует'
        elif repeat_password != password:
            context['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            context['error'] = 'Вы должны быть старше 18'
        else:
            # users.append(username)
            context['username'] = username
            context['password'] = password
            context['repeat_password'] = repeat_password
            context['age'] = age

        print(f"username:  {username}")
        print(f"password:  {password}")
        print(f"repeat_password:  {repeat_password}")
        print(f"age:  {age}")

    return render(request, 'one_task/registration_page.html', context)


def sign_up_by_django(request):
    users = ['Tom', 'Max', 'Mike']
    info: dict[str, any] = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif repeat_password != password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                users.append(username)
                info['username'] = username
                info['password'] = password
                info['repeat_password'] = repeat_password
                info['age'] = age
    else:
        form = UserRegister()
    context = {'form': form}
    context.update(info)
    print(context)
    print(users)
    return render(request, 'one_task/registration_page.html', context=context)
