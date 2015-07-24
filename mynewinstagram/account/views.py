from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def hello(request):
    print(User.objects.all());
    return HttpResponse('hey wassup!');

def getallusers(request):
    data = serializers.serialize('json', User.objects.all())
    return HttpResponse(data, content_type = 'application/json')
    


def follow(request):
    id1 = request.GET['id1'];
    id2 = request.GET['id2'];
    try:
        follower = Profile.objects.get(pk = id1)
    except:
        follower = Profile.objects.create(account = User.objects.get(pk = id1), city = City.objects.get(id = 1))
    follower.following.add(User.objects.get(id = id2));






    

