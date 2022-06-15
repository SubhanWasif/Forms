


from .models import formsModel
from django import forms



class formsForm(forms.ModelForm):
    class Meta:
        model = formsModel
        fields = '__all__'
        