from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.method == 'POST':
        entry = request.POST['q']
        if entry.upper() in util.list_entries():
            return render(request, f"encyclopedia/{entry.lower()}.html")
        else:
            return render(request, "encyclopedia/notexist.html")


def select(request, name):
    if name in util.list_entries():
        return render(request, f"encyclopedia/{name.lower()}.html")
    else:
        return render(request, "encyclopedia/notexist.html")