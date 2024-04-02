from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Projects
from slugify import slugify

@receiver(post_save, sender=Projects)
def create_slug_project(sender, instance, created, **kwargs):
    if created:
        if not instance.slug:
            instance.slug = slugify(instance.title)
            instance.save()