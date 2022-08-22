from django.contrib import admin
from .models import FoodCategory, Food, Cart, CartItem, FoodPhoto, Order

# Register your models here.
class AdminFoodcategory(admin.ModelAdmin):
    list_display = ('id', 'name')


class AdminFood(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'price', 'date_added')


class AdminFoodPhoto(admin.ModelAdmin):
    list_display = ('id', 'food', 'photo')


class AdminCart(admin.ModelAdmin):
    list_display = ('id', 'cart_id', 'user', 'date_added',)


class AdminCartItem(admin.ModelAdmin):
    list_display = ('id', 'cart', 'food', 'quantity', 'total_amount')


class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'cart', 'user', 'date_created', 'status')





admin.site.register(FoodCategory, AdminFoodcategory)
admin.site.register(Food, AdminFood)
admin.site.register(FoodPhoto, AdminFoodPhoto)
admin.site.register(Cart, AdminCart)
admin.site.register(CartItem, AdminCartItem)
admin.site.register(Order, AdminOrder)




