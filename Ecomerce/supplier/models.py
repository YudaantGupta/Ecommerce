from django.db import models

# Create your models here.
class Product(models.Model):
    category_choices = (
        ("Ele","Electronics"),
        ("Clo","Clothes"),
        ("Foo","Food"),
        ("Unc","Unclassified")
    )
    name = models.CharField(max_length=50 , default="untitled")
    price = models.IntegerField(default=0)
    category = models.CharField(max_length = 50, default = "Unc" , choices = category_choices)
    amount = models.IntegerField(default=0)
    disc=models.FloatField(default=0)
    date= models.DateField(auto_now_add=True)
    description= models.CharField(max_length=1000)
    image = models.ImageField(upload_to="image/product" , default = "image/default/Unknown.jpeg")
    inStock=models.BooleanField(default=True)

    def __str__(self):
        return self.name
