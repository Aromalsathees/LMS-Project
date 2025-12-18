from django.db import models
from users .models import *
from adviser_pannel .models import *


# Create your models here.
class Manage_users(models.Model):
    STATUS_CHOISES = [
        ('activate','ACTIVATE'),
        ('deactivate','DEACTIVATE')
    ]

    ROLE_CHOICES = [
        ('student','STUDENT'),
        ('teacher','TEACHER')
    ]

    user_name = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    user_status = models.CharField(max_length = 10 ,choices=STATUS_CHOISES, default='DEACTIVATE')
    assign_roles = models.CharField(max_length = 10 ,choices=ROLE_CHOICES , default = 'STUDENT')

    def __str__(self):
        return self.user_name


class Course_control(models.Model):
    COURSE_CHOISES = [
        ('approve','APPROVE'),
         ('reject','REJECT')
    ]   
    courses = models.ForeignKey(Courses ,on_delete=models.CASCADE)
    course_approve = models.CharField(max_length=10 , choices = COURSE_CHOISES , default='REJECT' )


class Course_Enrolled_students(models.Model):
    student_name = models.ForeignKey(Manage_users , on_delete=models.CASCADE)
    course_selected = models.ForeignKey(Courses , on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name.user_name.username
    