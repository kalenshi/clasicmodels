from django.db import models


class Productlines(models.Model):
    productline = models.CharField(db_column="productLine", primary_key=True, max_length=50)
    textdescription = models.CharField(db_column="textDescription", max_length=4000, blank=True, null=True)
    htmldescription = models.TextField(db_column="htmlDescription", blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "productlines"
