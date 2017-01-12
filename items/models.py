from django.db import models

# Create your models here.

STATUS_CHOICE = (
    ('Paused', 'Paused'),
    ('Draft', 'Draft'),
    ('Active', 'Active'),
)

class StatusModel(models.Model):
    status = models.CharField(
        max_length = 20,
        choices=STATUS_CHOICE,
        help_text='Status of the entity',
        default='Active'
    )
    class Meta:
        abstract=True
        
class Items(StatusModel):
    item_type = (
        ('M', 'menufectured'),
        ('P','dealers'),
        ('S', 'Stock'),
    )
    name = models.CharField(max_length=20, blank = False)
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    sku = models.IntegerField('verbos item',help_text = 'Unique SKU for products',db_index=True)
    item_type = models.CharField(max_length=20, choices=item_type,verbose_name='verbose item type')
    category = models.ManyToManyField('ItemCategories', verbose_name = "Item Categories")
    
    def __str__(self):
        return self.name
    
    def get_category(self):
        return " , ".join([c.name for c in self.category.all()])
    @property
    def getItemCategories(self):
        return [c.name for c in self.category.all()]
    
class ItemCategories(StatusModel):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name


# class Shops(models.Model):
#     name = models.CharField(max_length = 30)
#     item = models