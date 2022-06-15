from django.db import models

from api.models.product_lines import Productlines


class Products(models.Model):
    productcode = models.CharField(db_column="productCode", primary_key=True, max_length=15)
    productname = models.CharField(db_column="productName", max_length=70)
    productline = models.ForeignKey(Productlines, models.DO_NOTHING, db_column="productLine")
    productscale = models.CharField(db_column="productScale", max_length=10)
    productvendor = models.CharField(db_column="productVendor", max_length=50)
    productdescription = models.TextField(db_column="productDescription")
    quantityinstock = models.SmallIntegerField(db_column="quantityInStock")
    buyprice = models.DecimalField(db_column="buyPrice", max_digits=10, decimal_places=2)
    msrp = models.DecimalField(db_column="MSRP", max_digits=10, decimal_places=2)

    class Meta:
        db_table = "products"

    def __str__(self):
        """
        Human-readable representation of the employees model

        Returns:
            str : the model in a readable string
        """
        return f"Product-{self.productcode}"
