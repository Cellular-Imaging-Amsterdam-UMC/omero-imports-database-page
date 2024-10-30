#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('imports/', views.imports_database_page, name='imports_database_page'),
    path('workflows/', views.workflows_database_page, name='workflows_database_page'),
]
