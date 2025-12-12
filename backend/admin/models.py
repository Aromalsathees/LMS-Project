from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    

class Materials(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    pdf = models.FielField(upload_to='pdf/' ,blank=True , null=True)
    videos = models.ForeignKey(upload_to='videos/', blank=True , null=True)
    images = models.ImageField(upload_to='/images',blank=True , null=True)

    def __str__(self):
        return self.course
    