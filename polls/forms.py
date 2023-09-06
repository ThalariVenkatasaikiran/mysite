from django import forms
from .models import CustomerDetails

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = '__all__'

from django import forms

from django.core.exceptions import ValidationError
from .models import Email


class QuestionForm(forms.Form):
    question_text = forms.CharField(label="Question", max_length=200, help_text="Enter the question with ? at the end")

    class Meta:
        fields = '__all__'

    def clean_question_text(self):
        question = self.cleaned_data["question_text"]
        if not question.strip().endswith("?"):
            raise ValidationError("Question should ends with '?'")
        return


# https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/#modelform
class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'


class DummyEmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'

class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)