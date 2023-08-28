from django.db import models


class Category(models.Model):
    """ A model representing a category """

    title = models.CharField(
        max_length=100,
        blank=False
    )
    description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    """ A model representing a Subcategory related to Category  """

    category = models.ForeignKey(
        Category,
        related_name='subcategory',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=100,
        verbose_name="type of category",
        blank=False
    )
    description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.title


class Product(models.Model):
    """ A model representing a product related to Subcategory   """

    subcategory = models.ForeignKey(
        Subcategory,
        related_name='products',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=200,
        db_index=True
    )
    description = models.TextField(
        blank=True
    )
    price = models.IntegerField()
    available = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    image = models.ImageField(
        upload_to='product_images/',
        default='product_images/product-default.png',
        blank=True,
        null=True
    )
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title
