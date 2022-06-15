from django.db import models


class Customers(models.Model):
    customernumber = models.IntegerField(db_column="customerNumber", primary_key=True)
    customername = models.CharField(db_column="customerName", max_length=50)
    contactlastname = models.CharField(db_column="contactLastName", max_length=50)
    contactfirstname = models.CharField(db_column="contactFirstName", max_length=50)
    phone = models.CharField(max_length=50)
    addressline1 = models.CharField(db_column="addressLine1", max_length=50)
    addressline2 = models.CharField(
        db_column="addressLine2", max_length=50, blank=True, null=True
    )
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True, null=True)
    postalcode = models.CharField(db_column="postalCode", max_length=15, blank=True, null=True)
    country = models.CharField(max_length=50)
    salesrepemployeenumber = models.ForeignKey(
        "Employees",
        models.DO_NOTHING,
        db_column="salesRepEmployeeNumber",
        blank=True,
        null=True,
        related_name="sales_rep"
    )
    creditlimit = models.DecimalField(
        db_column="creditLimit", max_digits=10, decimal_places=2, blank=True, null=True
    )

    class Meta:
        db_table = "customers"

    def __str__(self):
        """
        Human-readable representation of the customers model

        Returns:
            str : the model in a readable string
        """
        return f"Customer-{self.customernumber}"
