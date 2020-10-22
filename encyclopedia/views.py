from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.method == 'GET':
        entry = request.GET['q']
        for x in util.list_entries():
            if entry.upper() in x.upper():
                return render(request, "encyclopedia/search.html", {
                    "entry": x
                })
                break
        return render(request, "encyclopedia/notexist.html")


def select(request, name):
    if util.get_entry(name):
        return render(request, f"encyclopedia/{name.lower()}.html")
    else:
        return render(request, "encyclopedia/notexist.html")