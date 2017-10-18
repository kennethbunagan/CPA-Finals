from django.db import models
from django.core.urlresolvers import reverse

#blueprints to store data

#Will be the primary key
class Product(models.Model):
    productname = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('foods:detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.productname

class ProductDetails(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE) #when Food is deleted, delete its FoodDetails
    price = models.IntegerField()
    weight = models.CharField(max_length=250)

    def __str__(self):
        return 'PHP' + str(self.price) + self.weight