from django.db import models

from api.models.customers import Customers


class Payments(models.Model):
    customernumber = models.OneToOneField(Customers, models.DO_NOTHING, db_column='customerNumber',
                                          primary_key=True)  # Field name made lowercase.
    checknumber = models.CharField(db_column='checkNumber', max_length=50)  # Field name made lowercase.
    paymentdate = models.DateField(db_column='paymentDate')  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "payments"
        unique_together = (("customernumber", "checknumber"),)
