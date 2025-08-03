from django.db import models  # Import Django's models module for ORM functionality


class SKU(models.Model):  # Define SKU model representing a stock keeping unit
    sku_code = models.CharField(max_length=100, unique=True)  # Unique code for SKU, max length 100
    name = models.CharField(max_length=255)  # Name of the SKU, max length 255
    description = models.TextField(blank=True, null=True)  # Optional description field

    def __str__(self):  # String representation of SKU object
        return self.name  # Return the name of the SKU


class MSKU(models.Model):  # Define MSKU model representing a master SKU
    msku_code = models.CharField(
        max_length=100, unique=True
    )  # Unique code for MSKU, max length 100
    name = models.CharField(max_length=255, default="Unnamed Product")  # Name of the MSKU, default value provided
    skus = models.ManyToManyField("SKU", related_name="mskus")  # Many-to-many relationship to SKU

    def __str__(self):  # String representation of MSKU object
        return self.name  # Return the name of the MSKU
