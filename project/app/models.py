from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_name=models.CharField(max_length=50,null=True,blank=True)
    description=models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.dept_name   

class Emp(models.Model):
    emp_name=models.CharField(max_length=20)
    emp_email=models.EmailField()
    emp_contact=models.IntegerField()
    emp_password=models.CharField(max_length=20,default=12345)
    emp_department = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True, blank=True)
    
class Query(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Query = models.TextField()
    department = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='pending')
    admin_rep = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.Name

