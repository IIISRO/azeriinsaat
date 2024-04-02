from django.contrib import admin
from django.urls import path
from core.views import (
    HomeView,
    AboutView,
    BlogsView,
    BlogDetailView,ProjectsView,ProjectDetailView,ServicesView,ClientsView,ContactView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('blog-detail/', BlogDetailView.as_view(), name='blog-detail'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path("project/<slug:slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path('services/', ServicesView.as_view(), name='services'),
    path('clients/', ClientsView.as_view(), name='clients'),
    path('contact/', ContactView.as_view(), name='contact'),
  
]