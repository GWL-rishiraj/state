from django.db import models

# Create your models here.


class Items(models.Model):
    item_type = (
        ('M', 'menufectured'),
        ('P','dealers'),
        ('S', 'Stock'),
    )
    name = models.CharField(max_length=20, blank = False)
    sku = models.IntegerField('verbos item',help_text = 'Unique SKU for products')
    item_type = models.CharField(max_length=20, choices=item_type,verbose_name='verbose item type')
    
    def __str__(self):
        return self.name