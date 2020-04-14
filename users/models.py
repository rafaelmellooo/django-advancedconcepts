import os

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    avatar = models.ImageField(upload_to='users', blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    @property
    def avatar_url(self):
        return settings.MEDIA_URL + str(self.avatar)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, str(self.avatar)))
        super(User, self).delete(*args, **kwargs)


# SIGNALS

@receiver(pre_save, sender=User)
def set_slug_on_pre_save(sender, instance, **kwargs):
    if not instance.slug:
        slug = slugify(instance.first_name + ' ' + instance.last_name)
        count_slug = User.objects.filter(slug__startswith=slug).count()
        slug = slug if count_slug == 0 else '%s-%d' % (slug, count_slug)

        instance.slug = slug
