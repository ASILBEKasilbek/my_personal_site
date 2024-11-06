# Generated by Django 4.2.16 on 2024-11-06 16:50

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
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.basemodel')),
                ('description', models.TextField()),
                ('total_projects', models.IntegerField(default=0)),
                ('total_users', models.IntegerField(default=0)),
                ('happy_customers', models.IntegerField()),
            ],
            bases=('app.basemodel',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.basemodel')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='posts/')),
                ('view_counts', models.IntegerField(default=0)),
            ],
            bases=('app.basemodel',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.basemodel')),
                ('full_name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='profile/')),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
            bases=('app.basemodel',),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.basemodel')),
                ('title', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            bases=('app.basemodel',),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.basemodel')),
                ('title', models.CharField(max_length=100)),
                ('percentage', models.IntegerField(default=0)),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=('app.basemodel',),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='blogs')),
                ('view_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.basemodel')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('link', models.URLField()),
                ('completed_at', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category')),
                ('used_tools', models.ManyToManyField(to='app.skill')),
            ],
            bases=('app.basemodel',),
        ),
    ]
