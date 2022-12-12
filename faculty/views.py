from django.shortcuts import render
from django.http import HttpResponse
from faculty import forms

# Create your views here.
def falogin(request):
    return render(request,'falogin.html')

def facultyinputview(request):
    form=forms.FacultyForm()
    if request.method=='POST':
        form=forms.FacultyForm(request.POST)
        if form.is_valid():
            print('Form validation success and printing data')
            print('Name:',form.cleaned_data[''])
    my_dict={'form':form}
    return render(request,'facform.html')