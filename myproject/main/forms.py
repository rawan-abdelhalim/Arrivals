from django import forms

class InternForm(forms.ModelForm):
    class meta:
        model = Intern
        exclude = []