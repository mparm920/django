from django.db import models

def Category(models.Model):
    name = models.CharField(max_length=20)

def Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)    
    category = models.ManyToManyField('Category', related_name='posts')

def Comment(models.Model):
    author = models.CharField(max_length=20)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)    
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
