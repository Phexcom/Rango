from django.db import models
<<<<<<< HEAD
from django.template.defaultfilters import slugify
=======
>>>>>>> 63a1fa0a6df2fc4b4c25f6b5b508329561fc4e9d


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
<<<<<<< HEAD
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, *kwargs)

=======
    
>>>>>>> 63a1fa0a6df2fc4b4c25f6b5b508329561fc4e9d
    class Meta:
         verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
