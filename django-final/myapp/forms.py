from django import forms
from .models import Input, LGAs

class InputForm(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    lga = forms.ChoiceField(choices=LGAs, required=True,
                              widget=forms.Select(attrs = attrs))
    class Meta:

        model = Input
        fields = ['lga']
