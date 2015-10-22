from django.db import models

class Hotels(models.Model):
    hotel_name = models.CharField(max_length=200)
    hotel_add = models.CharField(max_length=200)
    hotel_no = models.IntegerField(default=0)
    def __str__(self):
        return self.hotel_name




class menu_item(models.Model):
    menu_item1 = models.CharField(max_length=200)
    menu_item2 = models.CharField(max_length=200)
    menu_item3 = models.CharField(max_length=200)
    menu_item4 = models.CharField(max_length=200)
    menu_item5 = models.CharField(max_length=200)
    menu_item6 = models.CharField(max_length=200)
    menu_item7 = models.CharField(max_length=200)
    menu_item8 = models.CharField(max_length=200)
    menu_item9 = models.CharField(max_length=200)
    menu_item10 = models.CharField(max_length=200)
