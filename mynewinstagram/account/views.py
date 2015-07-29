from django.shortcuts import render, Http404,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
import datetime
from .models import Country
from .forms import NameForm, ContactForm, CountryForm
# Create your views here.
def hello(request):
    print(User.objects.all());
    return HttpResponse('hey wassup!');

def create_update_country(request, id = None):
    if (request.method == 'GET'):
        if id != None:
            country = get_object_or_404(Country, pk = id)
            f = CountryForm(instance = country);
        else:
            f = CountryForm();
        return render(request, 'account/createcountry.html', { 'form': f, 'id' : id });
    elif (request.method == 'POST'):
        if  id!=None:
            country = get_object_or_404(Country, pk = id)
            f = CountryForm(request.POST, instance = country);
        else:
            f= CountryForm(request.POST)
        print(f)
        if (f.is_valid()):
            country = f.save();
            return redirect('country-edit', id = country.id)
        else:
            return render(request, 'account/createcountry.html', { 'form': f, 'id' : id });





def sendmessage(request):
    if request.method == 'GET':
        f = ContactForm();
        return render(request, 'account/sendmessage.html',{'nForm' : f})
    elif request.method == 'POST':
        f = ContactForm(request.POST);
        if (f.is_valid()):
            return redirect('home', id = 2)
        else:
            return render(request, 'account/sendmessage.html', {'nForm' : f})
    else:
        raise Http404('Method Not Supported!')

        



def newhome(request, id):
    try:
        user = User.objects.get(pk = id)
    except User.DoesNotExist:
        raise Http404("User doesn't exitst")
    f = NameForm();
    return render(request, 'base/index.html',{'u' : user, 'nForm' : f})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

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






    

