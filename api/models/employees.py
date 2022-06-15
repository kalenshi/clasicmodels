from django.db import models


class Employees(models.Model):
    employeenumber = models.IntegerField(db_column="employeeNumber", primary_key=True)
    lastname = models.CharField(db_column="lastName", max_length=50)
    firstname = models.CharField(db_column="firstName", max_length=50)
    extension = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    officecode = models.ForeignKey("Offices", models.DO_NOTHING, db_column="officeCode", related_name="office")
    reportsto = models.ForeignKey(
        "self",
        models.DO_NOTHING,
        db_column="reportsTo",
        blank=True,
        null=True,
        related_name="manages"
    )
    jobtitle = models.CharField(db_column="jobTitle", max_length=50)

    active = models.BooleanField(default=1, blank=True)

    class Meta:
        db_table = "employees"

    def __str__(self):
        """
        Human-readable representation of the employees model

        Returns:
            str : the model in a readable string
        """
        return f"Employee-{self.employeenumber}"
