from django.db import models
from django.urls import reverse

# Create your models here.


#model voor items tab
class item(models.Model):
    itemnr = models.IntegerField(max_length=6, blank=True)
    old_it_nr = models.CharField(max_length=6, blank=True)
    jobcode = models.CharField(max_length=10, blank=True)
    omschrijving = models.CharField(max_length=50)
    REF_nbr = models.CharField(max_length = 15, blank=True)
    unit = models.CharField(max_length=5, blank=True)
    eenheidsprijs = models.IntegerField(max_length=8)
    ehp_onderaannemer = models.FloatField(max_length=8, blank=True)
    #aantal = models.integerfield(max_length=10,blank=true) dit later toevoegen omdat dit berekend moet worden met waarden uit andere tabel, dus niet straightforward
    #total = zelfde als hiebovenvermeld, moet berekend worden dus niet straightforward
    categorie = models.CharField(max_length = 10, blank=True)

    def __int__(self):
        return self.itemnr

#model voor personeel tab, jacops aangeleverd door pxm - engineers tab
# eventueel verwijderen
class werknemer(models.Model):
    personeelsnummer = models.IntegerField(max_length=8)
    naam = models.CharField(max_length = 15)
    voornaam = models.CharField(max_length = 15)
    skills = models.CharField(max_length= 10)
    functie = models.CharField(max_length=20)

    def __str__(self):
        return self.naam + ' ' + self.voornaam

    def get_absolute_url(self):
            return reverse("EFF:employees")

class engineer(models.Model):
    name = models.CharField(max_length = 30)
    login = models.IntegerField(max_length=6)
    region = models.CharField(max_length = 5)
    district = models.CharField(max_length = 6)
    subdisctrict = models.CharField(max_length = 8)
    workteam = models.CharField(max_length = 25)
    company = models.CharField(max_length = 35)
    company_c = models.CharField(max_length = 35)

    def __str__(self):
        return self.name

# !!!!!! werkenemers zijn anders in aangeleverd door pxm dan in de billprp excel, ??? beide behouden en dan adhv pernr eruithalen?
