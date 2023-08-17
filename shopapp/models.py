from django.db import models
class product_tbl(models.Model):
    name=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    m_year=models.CharField(max_length=30)
    colour=models.CharField(max_length=30)
    brand=models.CharField(max_length=30)
    class meta:
        db_tale='product_tbl'
class staff_tbl(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    salary=models.IntegerField()
    class meta:
        db_table='staff_tbl'


# Create your models here.
