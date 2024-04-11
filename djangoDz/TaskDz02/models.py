from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name="taskdz02_user_set",
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='taskdz02_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
    

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    product_img = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.product_name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    data_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ №{self.id} клиета {self.User.name}"