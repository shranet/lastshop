# Generated by Django 3.1.7 on 2021-03-29 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.category')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_uz', models.CharField(max_length=100)),
                ('subject_ru', models.CharField(max_length=100)),
                ('content_uz', models.TextField()),
                ('content_ru', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('status', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Maqola',
                'verbose_name_plural': 'Maqolalar',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=50)),
                ('content_uz', models.TextField()),
                ('content_ru', models.TextField()),
                ('anons_uz', models.CharField(max_length=50)),
                ('anons_ru', models.CharField(max_length=50)),
                ('price', models.BigIntegerField()),
                ('discount_percent', models.SmallIntegerField(default=0)),
                ('discount_start', models.DateTimeField(default=None, null=True)),
                ('discount_end', models.DateTimeField(default=None, null=True)),
                ('availability', models.IntegerField(default=0)),
                ('vendor_code', models.CharField(max_length=15)),
                ('photo0', models.ImageField(upload_to='')),
                ('photo1', models.ImageField(upload_to='')),
                ('photo2', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Mahsulot',
                'verbose_name_plural': 'Mahsulotlar',
            },
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('availability', models.IntegerField(default=0)),
                ('used', models.IntegerField(default=0)),
                ('discount', models.SmallIntegerField(default=10)),
            ],
            options={
                'verbose_name': 'Promo kod',
                'verbose_name_plural': 'Promo kodlar',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('key', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('value', models.TextField()),
            ],
            options={
                'verbose_name': 'Sozlar',
                'verbose_name_plural': 'Sozlashlar',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': "O'lchov birligi",
                'verbose_name_plural': "O'lchov birliklari",
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Izoh',
                'verbose_name_plural': 'Izohlar',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.SmallIntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mahsulot izohi',
                'verbose_name_plural': 'Mahsulot izohlari',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='availability_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.unit'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.category'),
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.postcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.post')),
            ],
            options={
                'verbose_name': 'Maqola izohi',
                'verbose_name_plural': 'Maqola izohlari',
            },
        ),
    ]