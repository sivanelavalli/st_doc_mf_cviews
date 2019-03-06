# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from app.forms import StudentModelForm,DocumentsModelForm
from django.forms.models import inlineformset_factory
from .models import Student,Documents
def Save(request):
    if request.method=="POST":
        form2=StudentModelForm(request.POST,request.FILES)
        if form2.is_valid():
            newdata=form2.cleaned_data.copy()
            first_doc=newdata.pop("first_doc",None)
            second_doc=newdata.pop("second_doc",None)
            student=Student.objects.create(**newdata)
            if first_doc and second_doc:
                student.documents_set.create(firstdoc=first_doc,seconddoc=second_doc)
            return render(request, "app/index.html", {"form":form2})
        else:
            return render(request, "app/index.html", {"form":form2})
    else:
        form2 = StudentModelForm()
    return render(request, "app/index.html", {"form": form2})

class ViewAll(ListView):
    model = Student
    template_name = "app/viewall.html"


class ViewOne(DetailView):
    model = Student
    template_name = "app/viewone.html"