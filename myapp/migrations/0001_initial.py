# Generated by Django 4.1.2 on 2024-04-03 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=100, verbose_name='Category Name')),
                ('catimage', models.ImageField(upload_to='categoryImg', verbose_name='Category Image')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('resolved', 'Resolved')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('shape', models.CharField(max_length=100)),
                ('usage', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=50)),
                ('material_type', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('quantity', models.FloatField()),
                ('image', models.ImageField(upload_to='productImg')),
                ('status', models.CharField(choices=[('available', 'Available'), ('not available', 'Not Available')], max_length=50)),
                ('catid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category', verbose_name='Category Id')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.color')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('password', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('uimg', models.ImageField(upload_to='profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('budget', models.FloatField()),
                ('message', models.TextField()),
                ('inquirystatus', models.CharField(choices=[('pending', 'Pending'), ('resolved', 'Resolved')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='extraImg')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
    ]
