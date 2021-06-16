from django.shortcuts import render
#from django.http import HttpResponse
import hashlib
#from .md5 import MD5


def home(request):
    return render(request, 'home.html')


def button(request):
    imp = request.POST.get('pinput')
    md5_hash = hashlib.md5(imp.encode())
    data = md5_hash.hexdigest
    print(md5_hash)
    return render(request, 'home.html', {'data': data})
