from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    Product_name = models.CharField(max_length=30)
    Product_desc = models.CharField(max_length=300)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default=" ")
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default=" ")

    def __str__(self):
        return self.Product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='')
    desc = models.CharField(max_length=300, default='')
    phone = models.CharField(max_length=10, default='')
    email = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name


class Order(models.Model):
    items_json = models.CharField(max_length=5000)
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='')
    address1 = models.CharField(max_length=30, default='')
    address2 = models.CharField(max_length=300, default='')
    phone = models.CharField(max_length=10, default='')
    email = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    state = models.CharField(max_length=30, default='')
    zipcode = models.CharField(max_length=30, default='')

    def __str__(self):
        return str(self.order_id)

