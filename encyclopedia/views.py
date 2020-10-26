from django.shortcuts import render
from markdown2 import Markdown
from . import util
from django.http import HttpResponse

app_name="wiki"

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.method == 'GET':
        search = []
        entry = request.GET['q']
        for x in util.list_entries():
            if entry.upper() in x.upper():
                search.append(x)
    if search:            
        return render(request, "encyclopedia/index.html", {
            "entries": search
            })
    else:
        return render(request, "encyclopedia/notexist.html", {
            "content": "Page Not Found"
        })


def select(request, name):
    try:
        markdowner = Markdown()
        output = markdowner.convert(util.get_entry(name))
        return render(request, "encyclopedia/title.html", {
            "title": name, "content": output
        })
    except:
        return render(request, "encyclopedia/notexist.html")


def add(request):
    return render(request, "encyclopedia/newpage.html")

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

    if title in util.list_entries():
        return render(request, "encyclopedia/notexist.html", {
            "content": "Encyclopedia Already Exist"
        })
    else:
        util.save_entry(title, content)

        markdowner = Markdown()
        output = markdowner.convert(util.get_entry(title))
        return render(request, "encyclopedia/title.html", {
            "title": title, "content": output
        })
