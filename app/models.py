from django.db import models
from datetime import datetime 

Filter_Type = (
    ('filter-docker', 'filter-docker'),
    ('filter-asp', 'filter-asp'),
    ('filter-python', 'filter-python')
)

Type_Name = (
    ('Docker','Docker'),
    ('AspNetCore','AspNetCore'),
    ('Python','Python')
)

class Navbar(models.Model):
    Name = models.CharField(max_length=100)
    Profil_img = models.ImageField()
    twitter_url = models.URLField(max_length=200)
    instagram_url = models.URLField(max_length=200)
    youtube_url = models.URLField(max_length=200)
    linkedin_url = models.URLField(max_length=200)

    def __str__(self):
        return self.Name

class Contact(models.Model):
    Name = models.CharField(max_length=10)
    Destrication = models.CharField(max_length=250)
    Location = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Call = models.CharField(max_length=20)
    Maps_Link = models.URLField(max_length=250)

    def __str__(self):
        return self.Name

class Blog(models.Model):
    Blog_Name = models.CharField(max_length=50)
    Name_Type = models.CharField(choices=Type_Name, max_length=15)
    Type_Filter = models.CharField(choices=Filter_Type, max_length=15)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    Blog_img = models.ImageField(upload_to='blog')
    body = models.TextField()
    
    def __str__(self):
        return self.Blog_Name