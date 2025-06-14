from django.http import HttpResponse
from django.shortcuts import render
from . models import *

# Create your views here.

def index(request):
    about = AboutSection.objects.all()
    skills = Skill.objects.all()
    educations = education.objects.all()   
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    service = Service.objects.all()
    sociallink = SocialLink.objects.all()
    contacts = Contact.objects.all()

    context = {
        'about': about,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
        'service': service,
        'sociallink': sociallink,
        'contacts': contacts
    }
    return render(request, 'index.html', context)


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Save the contact information to the database
#         Contact.objects.create(name=name, email=email, subject=subject, message=message)

#         return HttpResponse("Thank you for your message!")

#     return render(request, 'contact.html')

# ------------------------------------------------------------------

# If you want to handle the contact form submission via AJAX, you can use the following approach.
# For the AJAX approach, modify your view:
from django.http import JsonResponse

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the contact information to the database
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return JsonResponse({'success': True})
    else:
        form = Contact()
    return render(request, 'contact.html', {'form': form})

