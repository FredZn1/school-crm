from django.db import models
from django.shortcuts import reverse
from groups.models import Group


class Student(models.Model):
    image = models.ImageField(upload_to='students_images/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='student_members', null=True, blank=True)
    date_of_birth = models.DateField()
    telephone_number = models.CharField(max_length=13)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_detail_url(self):
        return reverse('students:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('students:update', args=[self.pk])