from django.shortcuts import render

# Create your views here.
def home(request, year, month):
    name = "Bob"
    month = month.capitalize()
    
    return render(request, "home.html", {"name": name,"year":year, "month": month})
