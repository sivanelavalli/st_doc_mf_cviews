from django import forms
from . models import Student,Documents
from django.forms import ValidationError
import re
class StudentModelForm(forms.ModelForm):
    first_doc=forms.ImageField()
    second_doc=forms.ImageField()
    class Meta:
        model=Student
        fields=['firstname','lastname','email','phoneno','address','first_doc','second_doc']

    def clean_firstname(self):
        firstname=self.cleaned_data["firstname"]
        newname=firstname.upper()
        if firstname is not newname:
            raise ValidationError("Enter CAPITALS Only....")
        return newname

    def clean_lastname(self):
        lastname=self.cleaned_data["lastname"]
        lname=lastname.upper()
        if lastname is not lname:
            raise ValidationError("CAPITALS Only...")
        return lname

    def clean_email(self):
        email=self.cleaned_data["email"]
        if not email.endswith('.com'):
            raise  ValidationError("Enter .com emails only")
        return email

class DocumentsModelForm(forms.ModelForm):
    class Meta:
        model=Documents
        exclude=('student',)

    def clean_student(self):
        student=self.cleaned_data["student"]

