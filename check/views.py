from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
from .models import Query
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def query(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            q = Query(name=form.cleaned_data['name'], ipaddress=form.cleaned_data['ipaddress'],
                      phone=form.cleaned_data['phone'], mac=form.cleaned_data['mac'])
            q.save()
            return HttpResponseRedirect('thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm(initial={'ipaddress': get_client_ip(request)})

    return render(request, 'name.html', {'form': form})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def thanks(request):
    return HttpResponse("<h1>谢谢</h1>")


