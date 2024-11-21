from django.shortcuts import render
from .models import ContactData
def contact(request):
    if request.method == 'GET':
        return render(request, "contact.html")
    else:
        fname1 = request.POST.get('fname')
        lname1 = request.POST.get('lname')
        email1 = request.POST.get('email')
        age1 = request.POST.get('age')
        contact1 = request.POST.get('contact')
        location1 = request.POST.get('location')
        ContactData(
            first_name = fname1,
            last_name = lname1,
            email = email1,
            age = age1,
            contact = contact1,
            location = location1,
        ).save()
        return render(request, "contact.html")
        
