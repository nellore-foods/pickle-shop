from django.db import models
from accounts.models import Customer, Outlet
from inventory.models import Product


class Order(models.Model):
    """
    Order Details for an order placed by a customer in a customer
    outlet.
    """
    STATUS_CHOICES = [
        # These are the ones I could think off of my head.  Again, this
        # might just be for testing.  In reality, a product will be
        # going though a bunch of other stages while transitioning from
        # "Order Placed" to "Order Delivered".  There's another "Order
        # Cancelled" branch for whenever the customer decides that she
        # doesn't like pickles anymore.
        #
        # This also seamlessly flows with the current concept of a
        # manual pick-up store where the "Pending" status means that
        # the order hasn't been picked up by the customer yet and
        # "Delivered" means that the item was paid for and picked up
        # successfully.

        ("P", "Pending"),
        ("D", "Delivered"),
    ]

    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default="P",
    )
    active = models.BooleanField(default=True)

    def __repr__(self):
        return (
            f"Order[ ",
                f"ID: {self.id}, ",
                f"Customer: {self.customer}, ",
                f"Date: {self.date}, "
                f"Amount: {self.amount}, "
                f"Status: {self.status}, ",
                f"Active: {self.active}, ",
            f"]"
        )

    def __str__(self):
        return (
            f"Order #{self.id} placed on {self.date} by {self.customer.name} ",
            f"({self.status})"
        )


class OrderItem(models.Model):
    """
    Distinct items associated with each order.
    """
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __repr__(self):
        return (
            f"OrderItems[ ",
                f"ID: {self.id}, ",
                f"Order: {self.order},",
                f"Product: {self.product}, ",
                f"Quantity: {self.quantity}, ",
            f"]"
        )

    def __str__(self):
        return (
            f"Item #{self.id} - {self,product.name} x{self.quantity} ",
            f"for order #{self.order.id}"
        )

