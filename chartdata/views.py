from django.shortcuts import render,redirect
from.models import*
from django.db.models import Sum,Q,Count
from django.http import JsonResponse

import json

from django.contrib.auth.forms import UserCreationForm

from.models import*

from .forms import UsercreateForm

from django.contrib import messages

# Create your views here.

def base(request):
        
    return render(request,'base.html')


def chart(request):
    labels =[]
    data = []

    '''
    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])

    return JsonResponse(data={
        'labels':labels,
        'data':data,
    })
    '''

    queryset= City.objects.order_by('-population')[:5]

    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request,'chart.html')

def highchart(request):

    dataset = Passengers.objects.values('ticket_class').annotate(survived_count=Count('ticket_class',filter=Q(survived=True)), 
            not_survived_count=Count('ticket_class',filter=Q(survived=False))).order_by('ticket_class')

    categories = list()
    survived_series = list()
    not_survived_series = list()
    
    for entry in dataset:
        categories.append('%s Class' % entry['ticket_class'])
        survived_series.append(entry['survived_count'])
        not_survived_series.append(entry['not_survived_count'])

    context={
        'dataset':dataset,
        'categories':json.dumps(categories),
        'survived_series':json.dumps(survived_series),
        'not_survived_series':json.dumps(not_survived_series),
    }
    return render(request,'highchart.html',context)

def update_profile(request,pk):
    user= User.objects.get(id=pk)
    user.profile.bio = "i am proffesional web developer"
    user.save()
    context={
        'user':user,
    }
    return render(request,'update_profile.html',context)

def signIn(request):
    if request.method == 'POST':
       form =UserCreationForm(request.POST or None)

       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request,'your account has been created')
           return redirect('/')
    else:
        form = UserCreationForm()

    context ={
        'form':form,
    }               
    return render(request,'signIn.html',context)
