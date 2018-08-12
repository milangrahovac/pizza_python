# posts/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

PIZZA_NAMES = (
    ('Pepperoni', 'Pepperoni'),
    ('Margherita', 'Margherita'),
    ('Capricciosa', 'Capricciosa'),
)


PIZZA_SIZES = (
    ('30cm', '30cm'),
    ('50cm', '50cm'),
)

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    pizza_id = models.IntegerField()
    # pizza_name = models.CharField(max_length=128, choices=PIZZA_NAMES)

    pizza_size = models.CharField(max_length=128, choices=PIZZA_SIZES)
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=128)
    customer_address = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return self.id