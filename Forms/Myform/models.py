from django.db import models



class formsModel(models.Model):
    name    = models.CharField(max_length=255,verbose_name='name')
    email   = models.EmailField(max_length=254,verbose_name='email')
    message = models.CharField(max_length=255,verbose_name='Messagae') 
    number  = models.CharField(max_length=50,null=True ,blank=False)
    address = models.CharField(max_length=50,null=True,blank=False)
    City    = models.CharField(max_length=50,null=True,blank=False)
    country = models.CharField( max_length=50,null=True,blank=False)
    class Meta:
        verbose_name= "informations"
        db_table    = "idkkk"
        ordering    = ['-name']

    def __str__(self):
        return self.name
    

