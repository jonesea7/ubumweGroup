from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify


CATEGORY_CHOICES = (
    ('PR', 'President'),
    ('VP', 'Vice President'),
    ('CO', 'Comptable'),
    ('UM', 'Umwanditsi'),
    ('JY', 'Umujyanama'),
    ('MB', 'Normal Member'),
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Contribution(models.Model):
    amount = models.IntegerField()
    asigayemo = models.IntegerField(blank=True, default=0)
    date_contributed = models.DateTimeField()

    def __str__(self):
        return f"Yo kuri {self.date_contributed}"

# nguzanyo {{ member.first_name }} yafashe                   <td>{{ contribution.asigayemo}} Frw</td>

class Loan(models.Model):
    amount = models.IntegerField()
    date_borrowed = models.DateTimeField()
    abishingizi = models.ManyToManyField("Member")
    yarishyuwe = models.BooleanField(default=False)

    def __str__(self):
        return f"Inguzanyo yo kuri {self.date_borrowed}"


class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(default='+12125552368')
    inshuro = models.IntegerField(default=1)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default='MB')
    contributions = models.ManyToManyField(Contribution)
    loans = models.ManyToManyField(Loan)
    member_image = models.ImageField(blank=True, default='default.png')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('ubumwe_app:member', kwargs={
                'slug': self.slug
            })

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super(Member, self).save(*args, **kwargs)

    def get_total_saved(self):
        total = 0
        for contrib in self.contributions.all():
            total += contrib.amount
        return total

    def get_total_borrowed(self):
        total = 0
        for loan in self.loans.all():
            total += loan.amount
        return total


#
# # original item in the database
# class Item(models.Model):
#     title = models.CharField(max_length=100)
#     price = models.FloatField(default=0.00)
#     discount_price = models.FloatField(blank=True, null=True)
#     category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
#     label = models.CharField(choices=LABEL_CHOICES, max_length=1)
#     description = models.TextField()
#     item_image = models.ImageField(blank=True, default='default.png')
#     slug = models.SlugField()
#
#     def get_absolute_url(self):
#         return reverse('ubumwe_app:product', kwargs={
#             'slug': self.slug
#         })
#
#     def get_add_to_cart_url(self):
#         return reverse('ubumwe_app:add_to_cart', kwargs={
#             'slug': self.slug
#         })
#
#     def get_remove_from_cart_url(self):
#         return reverse('ubumwe_app:remove_from_cart', kwargs={
#             'slug': self.slug
#         })
#
#     def __str__(self):
#         return self.title
#
#
# # For items that the use has added to cart
# class OrderItem(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#
#     def __str__(self):
#         return f"{self .quantity} of {self.item.title}"
#
#     def get_total_item_price(self):
#         return self.quantity * self.item.price
#
#     def get_total_discount_item_price(self):
#         return self.quantity * self.item.discount_price
#
#     def get_amount_saved_on_order(self):
#         return self.get_total_item_price() - self.get_total_discount_item_price()
#
#     def get_final_price(self):
#         if self.item.discount_price:
#             return self.get_total_discount_item_price()
#         return self.get_total_item_price()
#
#
# # A collection of order items for the user
# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     items = models.ManyToManyField(OrderItem)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)
#     billing_address = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)
#
#     def __str__(self):
#         return self.user.username
#
#     def get_total(self):
#         total = 0
#         for order_item in self.items.all():
#             total += order_item.get_final_price()
#         return total
#
#
# class BillingAddress(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#
#     street_address = models.CharField(max_length=100)
#     apartment_address = models.CharField(max_length=100)
#     country = CountryField(multiple=False)
#     zip_code = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.user.username
