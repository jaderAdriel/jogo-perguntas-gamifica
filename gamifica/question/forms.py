from question.models import Question
from django import forms


class RegisterQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["description", "image", "answear"]