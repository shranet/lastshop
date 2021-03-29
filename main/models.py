from django.db import models
from django.utils.translation import get_language
from lastshop.helpers import upload_file_name


class TranslateHelperMixin:
    def __getattr__(self, item):
        if item in self.translate_fields:
            lang = get_language()
            return getattr(self, '{}_{}'.format(item, lang))
        
        return super(TranslateHelperMixin, self).__getattr__(item)


class Review(models.Model):
    user = models.ForeignKey('client.User', on_delete=models.RESTRICT)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'


class Category(models.Model, TranslateHelperMixin):
    parent = models.ForeignKey('Category', on_delete=models.RESTRICT, null=True, default=None, blank=True)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    on_sidebar = models.BooleanField(default=False, verbose_name='Bosh sahifada chiqsinmi?')
    on_sidebar_order = models.IntegerField(default=0)

    translate_fields = ['name']

    @property
    def children(self):
        return Category.objects.filter(parent=self).all()

    class Meta:
        index_together = (
            ('on_sidebar', 'on_sidebar_order')
        )
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.name_uz


class Unit(models.Model):
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    class Meta:
        verbose_name = "O'lchov birligi"
        verbose_name_plural = "O'lchov birliklari"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    availability_unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    content_uz = models.TextField()
    content_ru = models.TextField()
    anons_uz = models.CharField(max_length=50)
    anons_ru = models.CharField(max_length=50)
    price = models.BigIntegerField()
    discount_percent = models.SmallIntegerField(default=0)
    discount_start = models.DateTimeField(default=None, null=True)
    discount_end = models.DateTimeField(default=None, null=True)
    availability = models.IntegerField(default=0)
    vendor_code = models.CharField(max_length=15)
    photo0 = models.ImageField()
    photo1 = models.ImageField()
    photo2 = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'


class ProductReview(models.Model):
    user = models.ForeignKey('client.User', on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    star = models.SmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Mahsulot izohi'
        verbose_name_plural = 'Mahsulot izohlari'


class PromoCode(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    availability = models.IntegerField(default=0)
    used = models.IntegerField(default=0)
    discount = models.SmallIntegerField(default=10)

    class Meta:
        verbose_name = 'Promo kod'
        verbose_name_plural = 'Promo kodlar'


class Setting(models.Model):
    key = models.CharField(max_length=20, primary_key=True)
    value = models.TextField()

    class Meta:
        verbose_name = 'Sozlar'
        verbose_name_plural = 'Sozlashlar'


class Post(models.Model, TranslateHelperMixin):
    STATUSES = (
        (1, 'Faol'),
        (0, 'Nofaol')
    )

    upload_folder = "post"

    user = models.ForeignKey('client.User', on_delete=models.RESTRICT, default=None)
    subject_uz = models.CharField(max_length=100)
    subject_ru = models.CharField(max_length=100)
    content_uz = models.TextField()
    content_ru = models.TextField()
    photo = models.ImageField(upload_to=upload_file_name)
    status = models.SmallIntegerField(choices=STATUSES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    translate_fields = ['subject', 'content']

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


class PostComment(models.Model):
    parent = models.ForeignKey('PostComment', on_delete=models.RESTRICT, null=True, default=None)
    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Maqola izohi'
        verbose_name_plural = 'Maqola izohlari'
