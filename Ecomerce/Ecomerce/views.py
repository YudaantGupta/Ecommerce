from django.shortcuts import redirect, render
from django.http import HttpResponse

def start_website(request):
    # return HttpResponse("hehehehehe")
    return redirect('/customer/')