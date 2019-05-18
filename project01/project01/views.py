from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .forms import ContactForm 

def home_page(request):
    return render(request, "home_page.html")


def about_page(request):
    context = {
      "title":"about page",
      "content": "welocme to the about page"
    }
    
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
      "title":"contact page!",
      "content": "welocme to the contact page",
      "form": contact_form
      
    }
    if contact_form.is_valid():
      print(contact_form.cleaned_data)
      if request.is_ajax():
        return JsonResponse({"message": "Thank You"})

    return render(request, "contact/view.html", context)

