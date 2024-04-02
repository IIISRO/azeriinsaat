from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Projects(models.Model):
    cover_image=models.ImageField(upload_to='images')
    title=models.CharField(max_length=255)
    filter=models.CharField(max_length=255,null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def absolute_url(self):
        return reverse_lazy('project-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name='Project'
        verbose_name_plural='Projects'

class ProjectImage(models.Model):
    image=models.ImageField(upload_to='project_image')
    project=models.ForeignKey('Projects',on_delete=models.CASCADE)

    def __str__(self):
        return self.project.title 



class Contact(models.Model):
    full_name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=255)
    message=models.TextField()
    
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contact'
