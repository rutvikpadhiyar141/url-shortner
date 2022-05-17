from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from secrets import token_urlsafe
from .models import URL
# Create your views here.

def index(request):
    short = ''
    if request.method == 'POST':
        short = token_urlsafe(3)
        url = request.POST['original']
        while True:
            try:
                url_obj = URL.objects.create(original_url=url, short_url=short)
            except:
                continue
            if url_obj:
                messages.success(request, 'success')
                break
    return render(request, 'shortner/index.html', context={'short': request.get_host() + '/' + short})


def redirector(request, short):
    print(short)
    url_obj = get_object_or_404(URL, short_url=short)
    return redirect(url_obj.original_url)