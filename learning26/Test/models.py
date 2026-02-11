from django.db import models

# Create your models here.
#user model 
class User(models.Model):
    ROLE_CHOICES = (
        ('Buyer', 'Buyer'),
        ('Seller', 'Seller'),
        ('Admin', 'Admin'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    mobile_no = models.CharField(max_length=15)
    address = models.TextField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
   
class Meta:
     db_table="user"
     def __str__(self):
          return self.name
     
class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=20)     
class Meta:
     db_table="product"
     def __str__(self):
        return self.item_name

class Auction(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    min_bid_increment = models.DecimalField(max_digits=10, decimal_places=2)
    auction_status = models.CharField(max_length=20)
class Meta:
    db_table="Auction"    
    def __str__(self):
        return self.product.item_name
    
class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)
class Meta:
    db_table="Bid"    
    def __str__(self):
        return self.bid_amount

class Payment(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=30)
    payment_status = models.CharField(max_length=20)
    payment_date = models.DateTimeField()
class Meta:
    db_table="payment"    

    def __str__(self):
        return self.amount  
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    notification_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
class Meta:
    db_table="Notificaton"    

    def __str__(self):
        return self.status    