from django.shortcuts import render


# Create your views here.

def index11(request):
    return render(request, 'fourth_task/hauptseite.html')


def index12(request):
    heizung = ['Vitopend ', 'Vitodens ', 'Vitogas  ']
    context = {'heizung': ['Vitopend ', 'Vitodens ', 'Vitogas  ']}
    return render(request, 'fourth_task/kesseln.html', context)


def index13(request):
    return render(request, 'fourth_task/korb.html')
