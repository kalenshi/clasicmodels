from django.db import models


class Orderdetails(models.Model):
    ordernumber = models.OneToOneField('Orders', models.DO_NOTHING, db_column='orderNumber', primary_key=True)
    productcode = models.ForeignKey('Products', models.DO_NOTHING, db_column='productCode')
    quantityordered = models.IntegerField(db_column='quantityOrdered')
    priceeach = models.DecimalField(db_column='priceEach', max_digits=10, decimal_places=2)
    orderlinenumber = models.SmallIntegerField(db_column='orderLineNumber')

    class Meta:
        db_table = "orderdetails"
        unique_together = (("ordernumber", "productcode"),)
