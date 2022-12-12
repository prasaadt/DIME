from django import forms

class FacultyForm(forms.Form):
    name=forms.CharField()
    salary=forms.IntegerField()

