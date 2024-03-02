from django.db import models
from ckeditor.fields import RichTextField
import requests

# website general settings start
GITHUB_ACCESS_TOKEN = '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'

DEFAULT_STATUS = 'draft'

STATUS_CHOICES = [
    ('draft', 'Taslak'),
    ('published', 'Yayınlandı'),
    ('deleted', 'Silindi'),
]

CHOICES = [
    (False, 'Pasif'),
    (True, 'Aktif'),
]

class Website_settings(models.Model):
    title = models.CharField(max_length=200, verbose_name='Site Başlığı')
    description = models.TextField(verbose_name='Site Açıklaması')
    keywords = models.TextField(verbose_name='Site Anahtar Kelimeleri')
    icon = models.ImageField(upload_to='images/', verbose_name='Site Faviconu')
    mail = models.CharField(max_length=100, verbose_name='mail ( contact sayfasında doldurulan form bu maile gelecek )')
    maintenance = models.BooleanField(default=False, choices=CHOICES, verbose_name='Bakim modu')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')

    class Meta:
        verbose_name = 'Site Ayarları'
        verbose_name_plural = 'Site Ayarları'

    def __str__(self):
        return self.title
# website general settings end

# homepage start
class Homepage(models.Model):
    title = models.CharField(max_length=200, verbose_name='Profil Başlığı')
    description = models.TextField(verbose_name='Profil Açıklaması')
    image = models.ImageField(upload_to='images/', verbose_name='Profil Resmi')
    socialmedia = models.ManyToManyField('Socialmedia', verbose_name='Sosyal Medya Hesapları')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')

    class Meta:
        verbose_name = 'Anasayfa'
        verbose_name_plural = 'Anasayfa'

    def __str__(self):
        return self.title
    
class Socialmedia (models.Model):
    title = models.CharField(max_length=200, verbose_name='Sosyal Medya Adı')
    color =  models.CharField(max_length=50, verbose_name='Renk')
    icon = models.CharField(max_length=200, verbose_name='Sosyal Medya İkonu')
    link = models.URLField(max_length=200, verbose_name='Sosyal Medya Linki')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')

    class Meta:
        verbose_name = 'Sosyal Medya'
        verbose_name_plural = 'Sosyal Medya'

    def __str__(self):
        return self.title
# homepage end

# about start
    
class About(models.Model):
    title = models.CharField(max_length=200, verbose_name='Hakkımda Başlığı')
    name = models.CharField(max_length=200, verbose_name='Ad Soyad')
    job = models.CharField(max_length=200, verbose_name='Meslek')
    content = RichTextField(verbose_name='içerik')
    skills = models.ManyToManyField('Skills', verbose_name='Yetenekler')
    education = models.ManyToManyField('Education', verbose_name='Eğitimler')
    experience = models.ManyToManyField('experience', verbose_name='Deneyimler')

    class Meta:
        verbose_name = 'Hakkımda'
        verbose_name_plural = 'Hakkımda'

    def __str__(self):
        return self.title
    

class Skills(models.Model):
    skill_name = models.CharField(max_length=200, verbose_name='Yetenek Adı')
    skill_value = models.IntegerField(verbose_name='Yetenek Değeri (0-100)')

    class Meta:
        verbose_name = 'Yetenek'
        verbose_name_plural = 'Yetenekler'

    def __str__(self):
        return self.skill_name
    
class Education(models.Model):
    school_name = models.CharField(max_length=200, verbose_name='Okul Adı')
    department = models.CharField(max_length=200, verbose_name='Bölüm')
    start_date = models.PositiveIntegerField(verbose_name='Başlangıç Tarihi')
    end_date = models.PositiveIntegerField(verbose_name='Bitiş Tarihi')

    class Meta:
        verbose_name = 'Eğitim'
        verbose_name_plural = 'Eğitimler'
        
    def __str__(self):
        return self.school_name
    
class Experience(models.Model):
    company_name = models.CharField(max_length=200, verbose_name='Şirket Adı')
    job = models.CharField(max_length=200, verbose_name='Meslek')
    start_date = models.PositiveIntegerField(verbose_name='Başlangıç Tarihi')
    end_date = models.PositiveIntegerField(verbose_name='Bitiş Tarihi')

    class Meta:
        verbose_name = 'Deneyim'
        verbose_name_plural = 'Deneyimler'
        
    def __str__(self):
        return self.company_name

# about end
    
# works start

class Works(models.Model):
    name = models.CharField(max_length=200, verbose_name='Proje Adı')
    link = models.CharField(max_length=1000, verbose_name='Proje Linki')
    image = models.ImageField(upload_to='works/', verbose_name='Proje Görseli')
    
    class Meta:
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'

    def __str__(self):
        return self.name
    
# contact start
    
class ContactForm(models.Model):
    name = models.CharField(max_length=50, verbose_name='İsim')
    mail = models.CharField(max_length=50, verbose_name='E-posta')
    subject = models.CharField(max_length=100, verbose_name='Konu')
    message = models.CharField(max_length=1000, verbose_name='mesaj')

    class Meta:
        verbose_name = 'Gelen Mesaj'
        verbose_name_plural = 'Gelen Mesajlar'

    def __str__(self):
        return self.name