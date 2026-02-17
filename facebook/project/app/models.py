from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=50,null=True,blank=True)
    dept_Description=models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.dept_name