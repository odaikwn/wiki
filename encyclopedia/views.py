from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.method == 'POST':
        entry = request.POST['q']
        try:
            return render(request, f"encyclopedia/{entry}.html")
        except:
            return render(request, "encyclopedia/notexist.html")


def select(request, name):
    try:
        return render(request, f"encyclopedia/{name.lower()}.html")
    except:
        return render(request, "encyclopedia/notexist.html")