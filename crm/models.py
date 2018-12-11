from django.db import models
from django.utils import timezone
from shop.models import Category
from django.urls import reverse


# Create your models here.
class Customer(models.Model):
    cust_name = models.CharField(max_length=50)
    organization = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bldgroom = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    account_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)


class Service(models.Model):

    category = models.ForeignKey(Category,
                                 related_name='services',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)#, default='name of the book'
    author = models.CharField(max_length=200)#, default='author name'
    slug = models.SlugField(max_length=200, db_index=True, default='isqa-0000')
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    edition = models.CharField(max_length=5)#, default='1st'
    isbn = models.CharField(max_length=14)#, default='000000000000'
    price = models.DecimalField(max_digits=10, decimal_places=2)#, default=''
    sellername = models.CharField(max_length=200)#, default='Seller name'
    selleremail = models.CharField(max_length=200)#, default='Seller email'
    sellerphone = models.CharField(max_length=200)#, default='Seller phone number'
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.category)

    def get_absolute_url(self):
            return reverse('crm:book_detail',
                           args=[self.id, self.slug])


class Product(models.Model):
    cust_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='products')
    product = models.CharField(max_length=100)
    p_description = models.TextField()
    quantity = models.IntegerField()
    pickup_time = models.DateTimeField(
        default=timezone.now)
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)

