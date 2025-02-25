from django.db import models


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


# Product model
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=6)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey("Collection", on_delete=models.PROTECT)
    promotion = models.ManyToManyField(
        Promotion,
    )


# Customer model
class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold"),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE
    )


# Order model
class Order(models.Model):
    PAYMENT_PENDING = "P"
    PAYMENT_COMPLETE = "C"
    PAYMENT_FAILED = "F"

    PAYMENT_CHOICES = [
        (PAYMENT_PENDING, "Pending"),
        (PAYMENT_COMPLETE, "Complete"),
        (PAYMENT_FAILED, "Failed"),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_CHOICES, default=PAYMENT_PENDING
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


# Address model
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True
    )

    zip = models.CharField(max_length=20, default="0000")


# collection model
class Collection(models.Model):
    title = models.CharField(max_length=255)


# order model
class OrderItem(models.Model):
    order = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=6)


# cart model
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


# cartitem model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
