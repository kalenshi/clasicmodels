from django.db import models


class Offices(models.Model):
    officecode = models.CharField(db_column='officeCode', primary_key=True, max_length=10)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addressline1 = models.CharField(db_column='addressLine1', max_length=50)
    addressline2 = models.CharField(db_column='addressLine2', max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50)
    postalcode = models.CharField(db_column='postalCode', max_length=15)
    territory = models.CharField(max_length=10)

    class Meta:
        db_table = "offices"

    def __str__(self):
        """
        Human-readable representation of the office

        Returns:
            str : the unique office code
        """
        return self.officecode
