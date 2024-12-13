from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


# Create your views here.

def index11(request):
    return render(request, 'one_task/hauptseite.html')


def index12(request):
    kesseln = Kessel.objects.all()
    context = {'kesseln': kesseln}
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
        for buyer in buyers:
            if buyer.name == username:
                context['error'] = 'Пользователь уже существует'
        if repeat_password != password:
            context['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            context['error'] = 'Вы должны быть старше 18'
        else:
            Buyer.objects.create(name=username, age=age, balance=0.00)
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
    # users = ['Tom', 'Max', 'Mike']
    buyers = Buyer.objects.all()
    info: dict[str, any] = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            for buyer in buyers:
                if buyer.name == username:
                    info['error'] = 'Пользователь уже существует'
            if repeat_password != password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, age=age, balance=0.00)
                # users.append(username)
                info['username'] = username
                info['password'] = password
                info['repeat_password'] = repeat_password
                info['age'] = age
    else:
        form = UserRegister()
    context = {'form': form}
    context.update(info)
    print(context)
    # print(users)
    return render(request, 'one_task/registration_page.html', context=context)


def news(request):
    news = News.objects.all()
    paginator = Paginator(news, 5)
    page_number = request.Get.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'one_task/news.html', {'page_obj': page_obj, 'news': news})
