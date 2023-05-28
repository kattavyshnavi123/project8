from django.db import models

# Create your models here.

class DEPT(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=100)
    LOC=models.CharField(max_length=100)
    def __str__(self):
        return self.DNAME

class EMP(models.Model):
    DEPTNO=models.ForeignKey(DEPT,on_delete=models.CASCADE)
    EMPNO=models.IntegerField()
    EMPNAME=models.CharField(max_length=100)
    JOB=models.CharField(max_length=100)
    MGR=models.IntegerField()
    HIREDATE=models.DateField()
    SAL=models.IntegerField()
    COMM=models.IntegerField()
    DEPTNO=models.IntegerField()
    def __str__(self):
        return self.EMPNAME

