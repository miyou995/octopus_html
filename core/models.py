from django.db import models
# Create your models here.
from tinymce import models as tinymce_models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)

class Category(models.Model):
    name  = models.CharField(verbose_name=_('Nom du DAS'), max_length=100)
    title  = models.CharField(verbose_name=_('Petit text'), max_length=100, blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    icon  = models.ImageField(upload_to='images/categories', null=True, blank=True)
    
    class Meta:
        verbose_name ="Catégorie"
    
    def __str__(self):
        return self.name

class Solution(models.Model):
    name        = models.CharField(verbose_name=_('sous catégorie'), max_length=100)
    title       = models.TextField(verbose_name=_('Petit text'),blank=True, null=True)
    description = tinymce_models.HTMLField(verbose_name='Déscription du produit', blank=True, null=True)
    icon        = models.ImageField(upload_to='images/categories', null=True, blank=True)
    def __str__(self):
        return self.name

class Service(models.Model):
    name  = models.CharField(verbose_name=_('Nom du Service'), max_length=100)
    slug = models.SlugField()
    title  = models.CharField(verbose_name=_('Petit text'), max_length=300)
    image = models.FileField( upload_to="images/services/", blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_("DAS categorie"), on_delete=models.CASCADE)
    description = tinymce_models.HTMLField(verbose_name='Déscription du produit', blank=True, null=True)
    icon  = models.CharField(verbose_name=_('nom de l icon du site https://feathericons.com/'), max_length=100)
    priority  = models.IntegerField(verbose_name=_('ordre / priorité'))

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("core:service-detail", kwargs={"slug": self.slug})
    
# class Article(models.Model):
#     pass                    

class ContactForm(models.Model):
    name        = models.CharField(verbose_name=_('Nom complet'), max_length=100)
    phone       = models.CharField(verbose_name=_("Téléphone") , max_length=25)
    email       = models.EmailField(verbose_name=_("Email"), null=True, blank = True)
    subject     = models.CharField(verbose_name=_("Sujet"), max_length=50, blank=True)
    message     = models.TextField(verbose_name=_("Message"), blank=True, null=True)
    date_sent = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)
        verbose_name = 'Formulaire de contact'
        verbose_name_plural = 'Formulaire de contact'

class Quote(models.Model):
    name = models.TextField(verbose_name=_("la citation"))
    actif = models.BooleanField(default=True)
    autor = models.CharField(verbose_name=_("auteur"), max_length=100)
    function = models.CharField(verbose_name=_("Fonction"), max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return str(self.autor)

class Client(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField( upload_to="images/clients")

    def __str__(self):
        return self.name
