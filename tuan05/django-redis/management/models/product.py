from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name =  models.CharField('Tên sản phẩm', max_length=255)
    price = models.FloatField('Giá')

    def __str__(self):
        return self.name
