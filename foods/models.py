from django.db import models

from accounts.models import User

# Create your models here.

class FoodCategory(models.Model):
    name = models.CharField(max_length=200)


    class Meta:
        db_table = 'categories'


class Food(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    cover_photo = models.ImageField(upload_to='foods')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'foods'


class FoodPhoto(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='foods')

    class Meta:
        db_table = 'food_photos'



class Cart(models.Model):
    cart_id = models.CharField(max_length=300)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'carts'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cart_items'


class Order(models.Model):
    order_id = models.CharField(max_length=300)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'orders'
        managed = True
        verbose_name = 'order'
        verbose_name_plural = 'orders'


