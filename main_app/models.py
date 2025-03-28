from django.db import models

class Py_objects(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок метода')
    name = models.CharField(max_length=25, verbose_name='Название метода')
    description = models.TextField(verbose_name='Название')
    example_code_image = models.ImageField(upload_to='py_objects_images/', verbose_name='Пример кода метода')