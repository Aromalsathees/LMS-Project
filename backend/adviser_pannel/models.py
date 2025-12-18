from django.db import models
from users .models import *
# Create your models here.

class Courses(models.Model):
    STATUS_CHOICES = [
        ('draf','DRAFT'),
        ('pending','PENDIND'),
        ('approved','APPROVED'),
    ]

    created_teacher_name = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    course_status = models.CharField(max_length=20 , choices = STATUS_CHOICES , default ='pending')

    def __str__(self):
        return self.name
    

class Materials(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='pdf/' ,blank=True , null=True)
    videos = models.FileField(upload_to='videos/', blank=True , null=True)
    images = models.ImageField(upload_to='/images',blank=True , null=True)

    def __str__(self):
        return self.course

# class Assignments(models.Model):
#     user_student_name = models.ForeignKey()