from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse
from apps.sendemail.forms import RegistroForm
from django.core.mail import send_mail


def index(request):
    
    return render(request, 'index.html', {})

class Registro(CreateView):
        model = User
        template_name = 'register.html'
        form_class = RegistroForm 
        def get_success_url(self):
            return reverse('index') 
            
        send_mail('Subject here',
                'Here is the message.',
                'mayore@ebenezertechs.com',
                ['mayoraliexer@gmail.com'],
                fail_silently=False,
            )
        
       
def testing(request):
    
    return render(request, 'register.html', {})

def send(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        send_mail('Delta', 
        'Su registro ha sido exitoso', 
        'mayore@ebenezertechs.com',
        #['cc.puertadevida@gmail.com'],
        [mail], 
        fail_silently=False)
    return render(request, 'result.html', {})
