from django.db import models
from subjects.models import Subject
from django.shortcuts import reverse


class Teacher(models.Model):
    image = models.ImageField(upload_to='teachers_images/')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, related_name='teacher_subject')
    telephone_number = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    work_expert = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_detail_url(self):
        return reverse('teachers:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('teachers:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:delete', args=[self.pk])