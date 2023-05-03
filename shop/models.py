from django.db import models

# Create your models here.
class Product(models.Model):
    product_id= models.AutoField
    product_name= models.CharField(max_length=80)
    category= models.CharField(max_length=50, default="")
    subcategory= models.CharField(max_length=50, default="")
    price= models.IntegerField(default="")
    product_desc= models.CharField(max_length=1000)  
    pub_date= models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self) -> str:
        return self.product_name

class Contact(models.Model):
    msg_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=80)
    email= models.CharField(max_length=50, default="")
    phone_number = models.CharField(max_length=500, default="")

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=900)
    address=models.CharField(max_length=112)
    city=models.CharField(max_length=122)
    state=models.CharField(max_length=112)
    zip_code=models.CharField(max_length=112)
    phone=models.CharField(max_length=112)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=50000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "...."