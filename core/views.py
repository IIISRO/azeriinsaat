from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.mail import send_mail
from typing import Any
from django.contrib import messages
from django.views.generic.edit import FormView
from django.conf import settings
import json
from .models import *
from .forms import ContactForm,HomeContactForm

class HomeView(FormView,ListView):
    template_name = 'index.html'
    model=Contact
    form_class=HomeContactForm
    success_url=reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["projects"]=Projects.objects.all()[:4]
        return context
    
    def form_valid(self, form):
        
        messages.success(
            self.request, 'Your message has been sent successfully')
        
        full_name = form.cleaned_data['full_name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        phone= form.cleaned_data['phone']
        
        text = f'Ad Soyad: {full_name} \nElektron poçt ünvanı: {email} \nMobil nömrə: {phone} \nMüraciət mətni: {message}'
        send_mail(
            'Yeni müştəri müraciəti',
            text,
            settings.EMAIL_HOST_USER,
            ['azeriinshaat.tqsh@mail.ru'],
        )
        self.object = form.save()

        return super().form_valid(form)
    

   

class AboutView(TemplateView):
    template_name = 'about.html'

class BlogsView(TemplateView):
    template_name = 'blogs.html'


class BlogDetailView(TemplateView):
    template_name = 'blog-detail.html'
    

class ProjectsView(ListView):
    model = Projects
    template_name = "projects.html"
    context_object_name='projects'


class ProjectDetailView(DetailView):
    model = Projects
    template_name = "project-detail.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Projects, slug = self.kwargs.get('slug'))
        context["recent_blog"] = Projects.objects.all()[:3]
        context["img"] = ProjectImage.objects.filter(project=project.id)   
        return context

class ServicesView(TemplateView):
    template_name = 'services.html'


class ClientsView(TemplateView):
    template_name = 'clients.html'


class ContactView(CreateView):
    model=Contact
    form_class=ContactForm
    template_name="contact.html"
    success_url=reverse_lazy("contact")
    def form_valid(self, form):
        
        messages.success(
            self.request, 'Your message has been sent successfully')
        
        full_name = form.cleaned_data['full_name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        phone= form.cleaned_data['phone']
        
        text = f'Ad Soyad: {full_name} \nElektron poçt ünvanı: {email} \nMobil nömrə: {phone} \nMüraciət mətni: {message}'
        send_mail(
            'Yeni müştəri müraciəti',
            text,
            settings.EMAIL_HOST_USER,
            ['azeriinshaat.tqsh@mail.ru'],
        )
        self.object = form.save()

        return super().form_valid(form)
    