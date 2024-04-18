from django.db import models
from django.contrib.auth.models import User

import uuid
import os

def make_unique_pic_name(instance, filename):
    """
    Função para gerar um nome único para a imagem de perfil do usuário.
    """
    extensao = filename.split('.')[-1]
    nome_unico = f"profile_pic_{uuid.uuid4().hex}.{extensao}"
    return os.path.join('profile_pic/', nome_unico)


class Usuario(User):
  
    name = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )

    profile_pic = models.ImageField(
        upload_to=make_unique_pic_name,
        blank=True,
        null=True
    )
