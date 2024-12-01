from django.db import models


class ProductPhotos(models.Model):
    photo = models.ImageField(upload_to="images/products/", verbose_name="Фото товара")

    def __str__(self):
        only_name = self.photo.name.split("/")
        return only_name[-1]

    class Meta:
        verbose_name_plural = "Фотографии товаров"


class SupplierProfile(models.Model):
    name = models.CharField(max_length=256, verbose_name="Имя")
    password = models.CharField(max_length=50, verbose_name="Пароль")
    surname = models.CharField(max_length=256, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=11, verbose_name="Номер телефона без '+'")
    description = models.TextField(verbose_name="Описание поставщика")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Поставщики"


class Product(models.Model):
    name = models.CharField(max_length=350, verbose_name='Название товара')
    description = models.TextField(verbose_name="Описание товара")
    available = models.BooleanField(default=True, verbose_name="Отображение товара")
    price = models.IntegerField(verbose_name="Цена товара")
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.PROTECT, verbose_name='Поставщик')
    photos = models.ManyToManyField(ProductPhotos, verbose_name="Фотографии товара")
    # reviews

    def __str__(self):
        return self.supplier.name

    class Meta:
        verbose_name_plural = "Продукты"



class PurchasedProductsUsers(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(verbose_name="Количество купленного продукта")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата покупки")

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = "Купленные товары покупателя"


class UserProfile(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    password = models.CharField(max_length=55, verbose_name="Пароль")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=11, verbose_name="Номер телефона")
    purchased_products = models.ManyToManyField(PurchasedProductsUsers, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Покупатели"
