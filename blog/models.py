from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
DEFAULT_STATUS = 'draft'

STATUS_CHOICES = [
    ('draft', 'Taslak'),
    ('published', 'Yayınlandı'),
    ('deleted', 'Silindi'),
]

class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Yazar')
    thumb  = models.ImageField(upload_to='blog/', verbose_name='küçük resim')
    title = models.CharField(max_length=200, verbose_name='Başlık')
    description =  models.CharField(max_length=500, verbose_name='Kısa Açıklama')
    content = RichTextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DEFAULT_STATUS)
    slug  = models.SlugField(unique=True,null=True, blank=True,max_length=200)

    class Meta:
        ordering = ['-create_date']
        verbose_name  = "Gönderi"
        verbose_name_plural = "Gönderiler"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Blog, self).save(*args, **kwargs)
    
