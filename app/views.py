from django.shortcuts import render
from app.models import *
from app.forms import *
# Create your views here.
from django.http import HttpResponse
def user_registration(request):
    d={'tfo':TopicForm(),'wfo':WebpageForm(),'afo':AccessrecordsForm()}
    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessrecordsForm(request.POST)
        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            NSTO=tfd.save(commit=False)
            NSTO.save()

            NSWO=wfd.save(commit=False)
            NSWO.topic_name=NSTO
            NSWO.save()

            NSAO=afd.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()
            return HttpResponse('data is submitted successfully')
        else:
            return HttpResponse('data is not valid')

    return render(request,'user_registration.html',d)