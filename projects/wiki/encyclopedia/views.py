from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from . import util
from .forms import SearchForm


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request):
    return HttpResponse("Hello, world. You're at the titles.")

def entry(request, entry_name):
    #html = "<html><body>%s</body></html>"
    return HttpResponse(util.get_entry(entry_name))

def results(request):
    return render(request, "encyclopedia/results.html", {
        "results": util.list_entries()
    })

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/results/')
        else:
            return HttpResponseRedirect('/')
    else:
        q = "Something went wrong. Try again"
        html = "<html><body>Hello, %s </body></html>" % q 
        return HttpResponse(html)