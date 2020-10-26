from django.shortcuts import render

from . import util

app_name="wiki"

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    search = []
    if request.method == 'GET':
        entry = request.GET['q']
        for x in util.list_entries():
            if entry.upper() in x.upper():
                search.append(x)

        return render(request, "encyclopedia/index.html", {
                "entries": search
            })
    return render(request, "encyclopedia/notexist.html")


def select(request, name):
    if util.get_entry(name):
        return render(request, f"encyclopedia/{name.lower()}.html")
    else:
        return render(request, "encyclopedia/notexist.html")

def add(request):
    return render(request, "encyclopedia/newpage.html")