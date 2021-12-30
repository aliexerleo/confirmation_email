from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
        ]

        labels = {
                'username': 'Username',
                'first_name': 'first name',
                'last_name': 'last name',
                'email': 'email',

        }
               
        