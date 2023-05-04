from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['topic_name']

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','email','url']

class AccessrecordsForm(forms.ModelForm):
    class Meta:
        model=Accessrecords
        fields=['date']



