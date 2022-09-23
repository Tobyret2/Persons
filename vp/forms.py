from django.forms import ModelForm

from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('family_name','name','age','sex')