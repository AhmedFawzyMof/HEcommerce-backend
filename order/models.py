from django.db import models
from django.contrib.auth.models import User
from product.models import *
import uuid

class OrderStatus(models.TextChoices):
    PROGRESS = u'in progress ↻'
    SHIPPING = u'in shipping 📦'
    COMPLETE = u'complete ☑️'

class ArOrderStatus(models.TextChoices):
    PROGRESS = u'جار مراجعة ↻ '
    SHIPPING = u'في الشحن 📦 '
    COMPLETE = u'مكتمل ☑️ '

class Order(models.Model):
    id              = models.UUIDField(primary_key=True,unique=True, default=uuid.uuid4, editable=False)
    user            = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    email           = models.CharField(max_length=100)
    address         = models.TextField()
    phone           = models.CharField(max_length=100)
    phone2          = models.CharField(max_length=100)
    paypal          = models.BooleanField(null=True, blank=True)
    ispaid          = models.BooleanField(null=True,blank=True,default=False)
    Delivered       = models.BooleanField(null=True,blank=True,default=False)
    order_total     = models.IntegerField()
    order_status    = models.CharField(max_length=100,null=True, choices=OrderStatus.choices,default=OrderStatus.PROGRESS)
    order_status_Ar = models.CharField(max_length=100,null=True, choices=ArOrderStatus.choices,default=ArOrderStatus.PROGRESS)
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['-created_at']
    
    def __str__(self):
        return self.email

class OrderItem(models.Model):
    order    = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price    = models.IntegerField()
    size     = models.CharField(max_length=100, blank=True,null=True)
    color    = models.CharField(max_length=100, blank=True,null=True)
    quantity = models.IntegerField()
#  for str id
    def __str__(self):
        
        return f'({self.order.id}) ({self.product.name}) ({self.order.user.email})'

class Contact(models.Model):
    user    = models.ForeignKey(User, related_name="contacts", on_delete=models.CASCADE,blank=True,null=True)
    phone   = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.user.username

class FeedBack(models.Model):
    user    = models.ForeignKey(User, related_name="feedbacks", on_delete=models.CASCADE,blank=True,null=True)
    title   = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.user.username

