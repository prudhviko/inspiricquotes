from django.db import models

class Quote(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='quotes/', null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', related_name='quotes')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

