from django.contrib.auth.forms import UserCreationForm
from accounts.models import Usuario

class RegisterUsuarioForm( UserCreationForm ):
    class Meta:
        model = Usuario
        fields = ["name", "email", "username", "profile_pic", "password1", "password2"]