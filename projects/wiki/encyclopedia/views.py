from django.shortcuts import render
from django.http import HttpResponse

from . import util
import datetime


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request):
    return HttpResponse("Hello, world. You're at the titles.")

def entry(request, entry_name):
    #html = "<html><body>%s</body></html>"
    return HttpResponse(util.get_entry(entry_name))