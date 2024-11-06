from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(BaseModel):
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="profile/")
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.full_name


class Skill(BaseModel):
    title = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.title


class About(BaseModel):

    description = models.TextField()
    total_projects = models.IntegerField(default=0)
    total_users = models.IntegerField(default=0)
    happy_customers = models.IntegerField()

    def __str__(self) -> str:
        return str(self.id)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts/")
    view_counts = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title


class Service(BaseModel):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Portfolio(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio/")
    link = models.URLField()
    used_tools = models.ManyToManyField(Skill)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    completed_at = models.DateField()

    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True
    )
    image=models.ImageField(upload_to='blogs',null=True)
    view_count=models.IntegerField(default=0)
    def __str__(self):
        return self.title
