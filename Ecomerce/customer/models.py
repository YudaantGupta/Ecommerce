from django.db import models

class A_Customer(models.Model):
    customerid = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50, default="Anish")
    date = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=50, default="")
    password = models .CharField(max_length=500, default="")
    contact = models.IntegerField(default=1111111111)
    building = models.CharField(max_length=100, default="untitled")
    street = models.CharField(max_length=200, default="untitled")
    landmark = models.CharField(max_length=200, default="untitled")
    city = models.CharField(max_length=50, default="untitled")
    state = models.CharField(max_length=50, default="untitled")
    pincode = models.IntegerField(default="0")
    wallet = models.FloatField(default="0", max_length=50)
    rewards = models.FloatField(default="50")

    def __str__(self):
        return self.customer_name  

class Item(models.Model):
    product = models.ForeignKey("supplier.Product", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    def price(self):
        y = (self.product.disc * self.product.price )/100
        return (self.product.price-y) * self.amount
    


    def __str__(self):
        return self.product.name

class Cart(models.Model):
    items = models.ManyToManyField("Item") 
    customer = models.OneToOneField("A_customer" , on_delete=models.CASCADE)

    def total(self):
        x = 0
        for i in self.items.all():
            x += i.price()
        return x



    # def __str__(self):
    #     return str(self.items.all())
    


# Create your models here.

