# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import StudentForm
from .forms import DataSourceForm
from .models import Student
from .models import ActivityLog
from .models import Data_source
from tablib import Dataset
from time import time


@login_required(login_url="/login/")
def index(request):

    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))

##
# Student Crud
##


@login_required(login_url="/login/")
def student(request):
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("it_background") == "on":
            it_background = 1

        else:
            it_background = 0

        new_student = Student(name=request.POST.get("name"), email=request.POST.get("email"), number=request.POST.get("number"), linkedin=request.POST.get("linkedin"), address=request.POST.get("address"), github=request.POST.get("github"), gender=request.POST.get("gender"), education_level=request.POST.get("education_level"),  it_background=it_background, data_source_id=request.POST.get("data_source"))
        new_student.save()
        return redirect("/show")
    data_sources = Data_source.objects.all()
    return render(request, "create-student.html", {"data_sources": data_sources})


@login_required(login_url="/login/")
def show(request):
    students = Student.objects.all()
    return render(request, "students-table.html", {'students': students})


@login_required(login_url="/login/")
def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})


@login_required(login_url="/login/")
def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'student': student})


@login_required(login_url="/login/")
def destroy(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/show")

@login_required(login_url="/login/")
def students_clear(request):
    Student.objects.all().delete()
    return redirect("/show")


###
# Upload File
###

@login_required(login_url="/login/")
def simple_upload(request):
    if request.method == 'POST':
        #Define time to calculate execution time
        start_time = time()
        
        dataset = Dataset()
        file = request.FILES['myfile']
        if file.name.endswith('.xlsx'):
            imported_data = dataset.load(file.read(), format='xlsx')
        elif file.name.endswith('.xls'):
            imported_data = dataset.load(file.read(), format='xls')
        elif file.name.endswith('.csv'):
            imported_data = dataset.load(
                file.read().decode('utf-8'), format='csv')
        else:
            return render(request, 'create-student.html', {"error": "Accpeted file extentions : (xlsx),(xls),(csv)","data_sources": Data_source.objects.all()})
        number_of_records = 0
        for data in imported_data:
            number_of_records+=1
            if data[7] == "yes":
                it_background = 1
            elif data[7] == "no":
                it_background = 0

            value = Student(name=data[0], number=data[1], email=data[2], linkedin=data[3], github=data[4],
                            gender=data[5], education_level=data[6], it_background=it_background, address=data[8],data_source_id=request.POST.get("data_source"))
            value.save()

        #save to activity log
        data_source = value.data_source.name
        execution_time = ((time() - start_time))
        job = ActivityLog(file_name=file.name,execution_time_in_seconds=execution_time,data_source_name=data_source,number_of_records=number_of_records)
        job.save()

        return redirect("/show")



###
# Data source CRUD
###

@login_required(login_url="/login/")
def data_source(request):
    if request.method == "POST":
        new_data_source = Data_source(name=request.POST.get("name"))
        new_data_source.save()
        return redirect("/data_source/show")
    return render(request, "create-data-source.html")


@login_required(login_url="/login/")
def data_source_show(request):
    data_sources = Data_source.objects.all()
    return render(request, "data_source-table.html", {'data_sources': data_sources})


@login_required(login_url="/login/")
def data_source_edit(request, id):
    data_source = Data_source.objects.get(id=id)
    return render(request, 'data_source-edit.html', {'data_source': data_source})


@login_required(login_url="/login/")
def data_source_update(request, id):
    data_source = Data_source.objects.get(id=id)
    form = DataSourceForm(request.POST, instance=data_source)
    if form.is_valid():
        form.save()
        return redirect("/data_source/show")
    return render(request, 'data_source-edit.html', {'data_source': data_source})


@login_required(login_url="/login/")
def data_source_destroy(request, id):
    data_source = Data_source.objects.get(id=id)
    data_source.delete()
    return redirect("/data_source/show")

# def testRelation(request):
#     student = Student.objects.get(id=103)
#     return HttpResponse(student.data_source)    



##
# Activity log show
##
@login_required(login_url="/login/")
def activity_log_show(request):
    jobs = ActivityLog.objects.all()
    return render(request, "activity-log.html", {'jobs': jobs})

@login_required(login_url="/login/")
def activity_log_clear_all(request):
    ActivityLog.objects.all().delete()
    return redirect("/activities")


##
# Charts
##

@login_required(login_url="/login/")
def charts(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'student': students})

