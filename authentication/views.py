from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'authentication/home.html')


def about(request):
    return render(request, 'authentication/about.html')


def faq(request):
    return render(request, 'authentication/FAQ.html')


def contact_home(request):
    return render(request, 'authentication/home_vaccine.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        New message: {}
        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['covaccinesce@gmail.com'])
    return render(request, 'authentication/contact.html')





