from django.shortcuts import render

# Create your views here.
def home(request):
    title = "my title"
    context = {
        "template_title": title,
    }
    return render(request, "home.html", context)