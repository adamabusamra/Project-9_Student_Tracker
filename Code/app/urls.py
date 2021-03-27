# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [

    # The home page
    path('', views.charts, name='home'),

    # The student routes
    path('students', views.student),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('students-clear-all', views.students_clear),
  
    # The Data_sources routes
    path('data_sources', views.data_source),
    path('data_source/show', views.data_source_show),
    path('data_source/edit/<int:id>', views.data_source_edit),
    path('data_source/update/<int:id>', views.data_source_update),
    path('data_source/delete/<int:id>', views.data_source_destroy),

    #Activity log
    path('activities', views.activity_log_show),
    path('jobs-clear-all', views.activity_log_clear_all),

    # Upload Route
    path('upload', views.simple_upload),

    # path('test', views.testRelation),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),


]
