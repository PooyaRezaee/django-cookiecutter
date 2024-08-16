from django.db import models
{% if cookiecutter.use_ckeditor == "y" %}
from django_ckeditor_5.fields import CKEditor5Field
{% endif %}
from django.db.models.signals import post_delete
from django.dispatch import receiver


class TestData(models.Model):
    random_number = models.IntegerField()
    {% if cookiecutter.use_ckeditor == "y" %}
    content = CKEditor5Field()
    {% endif %}
    thumbnail = models.ImageField(upload_to="test/thumb", null=True)

{% if cookiecutter.use_cloud_storage == "y" %}
@receiver(post_delete, sender=TestData)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.thumbnail and instance.thumbnail.name:
        instance.thumbnail.delete(save=False)
{% endif %}