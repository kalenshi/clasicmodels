from django.db import models

from api.models.customers import Customers


class Orders(models.Model):
    ordernumber = models.IntegerField(db_column="orderNumber", primary_key=True)  # Field name made lowercase.
    orderdate = models.DateField(db_column="orderDate")  # Field name made lowercase.
    requireddate = models.DateField(db_column="requiredDate")  # Field name made lowercase.
    shippeddate = models.DateField(db_column="shippedDate", blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=15)
    comments = models.TextField(blank=True, null=True)
    customernumber = models.ForeignKey(Customers, models.DO_NOTHING, db_column="customerNumber")

    class Meta:
        db_table = "orders"

    def __str__(self):
        """
        Human-readable representation of the employees model

        Returns:
            str : the model in a readable string
        """
        return f"Order-{self.ordernumber}"
