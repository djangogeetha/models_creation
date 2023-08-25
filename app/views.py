from django.shortcuts import render

# Create your views here.
from app.models import *

def display_Topic(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_Topic.html',d)


def display_Webpage(request):
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_Webpage.html',d)

def display_AccessRecord(request):
    QASRO=AccessRecord.objects.all()
    d={'QASRO':QASRO}
    return render(request,'display_AccessRecord.html',d)





def insert_Topic(request):
    Topic_name=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=Topic_name)[0]
    TO.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_Topic.html',d)



def insert_Webpage(request):
    tn=input('enter topic_name')
    na=input('enter name')
    ur=input('enter url')
     
    TO=Topic.objects.get(topic_name=tn) 

    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    WO.save()
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_Webpage.html',d)



def insert_AccessRecord(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get(topic_name=tn) 
    TO.save()
    pk=input('enter pk value')
    na=input('enter name')
    ur=input('enter url')
    WO=Webpage.objects.get(pk=pk)
    d=input('enter date')
    au=input('enter author')
    em=input('enter email')
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=au,email=em)[0]
    QASRO=AccessRecord.objects.all()
    d={'QASRO':QASRO}
    return render(request,'display_AccessRecord.html',d)


    


    

