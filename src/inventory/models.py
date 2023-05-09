from django.db import models


class Product(models.Model):
    """
    Represents a single product from the inventory.
    """
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    rate        = models.DecimalField(max_digits=7, decimal_places=2)

    def __repr__(self):
        return (
            f"Product[ ",
                f"ID: {self.id}, ",
                f"Name: {self.name}, ",
                f"Rate: {self.rate}, ",
            f"]"
        )

    def __str__(self):
        return f"{self.name} @ {self.rate}"


class Inventory(models.Model):
    """
    Represents the products in stock.
    """
    id          = models.AutoField(primary_key=True)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity    = models.PositiveIntegerField(default=0)
    launch_date = models.DateField(auto_now_add=True)
    eol_date    = models.DateField(null=True)
    batch_no    = models.CharField(max_length=15)
    active      = models.BooleanField(default=True)

    def __repr__(self):
        return (
            f"Inventory[ "
                f"ID: {self.id}, ",
                f"Product: {self.product}, ",
                f"Quantity: {self.quantity}, ",
                f"Launch Date: {self.launch_date}, ",
                f"EOL Date: {self.eol_date}, ",
                f"Batch No.: {self.batch_no}, ",
                f"Active: {self.active}, ",
            f"]"
        )

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

