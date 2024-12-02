from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.

def sign_up_by_html(request):
    users = ['Tom', 'Max', 'Mike']
    info = {}
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
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

        print(f"username:  {username}")
        print(f"password:  {password}")
        print(f"repeat_password:  {repeat_password}")
        print(f"age:  {age}")

    return render(request, 'fifth_task/registration_page.html', info)


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
    return render(request, 'fifth_task/registration_page.html', context=context)
