from django.db import models
from accounts.models import Usuario
import uuid, os

def make_unique_pic_name(instance, filename):
    """
    Função para gerar um nome único para a imagem da pergunta.
    """
    extensao = filename.split('.')[-1]
    nome_unico = f"question_image_{uuid.uuid4().hex}.{extensao}"
    return os.path.join('question_image/', nome_unico)


# Create your models here.
class Question( models.Model ):

    owner = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='owner',
    )

    description = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    image = models.ImageField(
        upload_to=make_unique_pic_name,
        blank=True,
        null=True
    )




class Alternative( models.Model ):
    text = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    isAnswer = models.BooleanField(
        default=False,
        blank=False,
        null=False
    )

