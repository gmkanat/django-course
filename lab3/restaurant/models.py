from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.name


class MenuCategory(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "MenuCategories"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    price = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name


class Order(models.Model):
    client_name = models.CharField(max_length=255)
    date_ordered = models.DateField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish, related_name="orders")

    def __str__(self):
        return f"{self.client_name} - {self.date_ordered} - {self.restaurant.name}"
