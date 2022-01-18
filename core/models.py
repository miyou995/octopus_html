from telnetlib import RCP
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

class Contact(models.Model):
    name        = models.CharField(verbose_name=_('Nom complet'), max_length=100)
    phone       = models.CharField(verbose_name=_("Téléphone") , max_length=25)
    email       = models.EmailField(verbose_name=_("Email"), null=True, blank =True)
    subject     = models.CharField(verbose_name=_("Sujet"), max_length=50, blank=True,null=True)
    message     = models.TextField(verbose_name=_("Message"), blank=True, null=True)
    date_sent   = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
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


class Invoice(models.Model):
    client          =  models.CharField(max_length=300,verbose_name='Description')
    client_rc       = models.CharField(max_length=300,verbose_name='Description')
    client_nif      =models.CharField(max_length=300,verbose_name='Description')
    client_art      =models.CharField(max_length=300,verbose_name='Description')
    client_adresse  =models.CharField(max_length=300,verbose_name='Description')
    invoice_number  = models.IntegerField(verbose_name='Numéro de facture')

    created       = models.DateTimeField(auto_now_add=True, verbose_name=_("Crée"))
    updated       = models.DateTimeField(auto_now=True, verbose_name=_("Modifié"))
    note          = models.TextField(blank=True, null=True, verbose_name=_("Note"))
    paid          = models.BooleanField(default=False, verbose_name=_("Payé"))
    discount      = models.DecimalField( max_digits=10, decimal_places=2, default=0, verbose_name="Réduction")

    def __str__(self):
        return f'facture N°:  {self.id} doit {self.client}'

class InvoiceItem(models.Model):
    invoice    = models.ForeignKey(Invoice,related_name='items', verbose_name=(_("Facture")), on_delete=models.CASCADE)
    description = models.CharField(max_length=300,verbose_name='Description')
    price    = models.DecimalField( max_digits=10, decimal_places=2, verbose_name=_("Prix"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantité"))

    def __str__(self):
        return str(self.description)
    def get_cost(self):
        return self.price * self.quantity